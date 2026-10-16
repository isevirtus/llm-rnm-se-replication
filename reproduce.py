"""Recompute the SE61 tables and tests offline. Never launches an LLM."""
from pathlib import Path
import argparse, hashlib, json, sys
import numpy as np
import pandas as pd

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'evaluator'))
from ordinal_engine import make_cpt
from ordinal_prediction_adapter import predict
from statistics_utils import metrics, summarize, holm, macro

def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False,allow_nan=False)+'\n',encoding='utf-8')
def compare(actual,expected,path='root'):
    if isinstance(expected,dict):
        for k,v in expected.items():
            if k=='scope': continue
            if k in actual:compare(actual[k],v,path+'/'+k)
            else:raise AssertionError('Missing '+path+'/'+k)
    elif isinstance(expected,list):
        assert len(actual)==len(expected),path
        for i,(a,e) in enumerate(zip(actual,expected)):compare(a,e,path+f'/{i}')
    elif isinstance(expected,(int,float)) and not isinstance(expected,bool):
        assert abs(actual-expected)<=1e-10*max(1,abs(expected)),(path,actual,expected)
    else:assert actual==expected,(path,actual,expected)

def run(refit=False):
    data=ROOT/'evaluator/data'; expected=ROOT/'evaluator/expected'
    out=ROOT/'reproduced';out.mkdir(exist_ok=True)
    manifest=read(ROOT/'manifest.json')
    for name,h in manifest['files'].items():
        p=ROOT/name;assert hashlib.sha256(p.read_bytes()).hexdigest()==h,('Modified input',name)
    refs=read(data/'references.json');answers=read(data/'answers.json');preds=read(data/'predictions.json');attempts=read(data/'attempts.json')
    tasks={t['task_id']:t for t in read(data/'tasks.json')}
    assert len(refs)==61 and len(answers)==2440 and len(attempts)==2444
    assert len({a['run_id'] for a in answers})==2440
    counts=pd.DataFrame(answers).groupby(['repetition','condition']).size()
    assert len(counts)==40 and counts.eq(61).all()
    trials=[];anchors=[];fit_cache={};max_rebuild=0.;max_refit=0.
    for a in answers:
        r=refs[a['node_id']];m=r['metadata'];p=np.array(r['reference_cpt']);q=np.array(preds[a['run_id']]['predicted_cpt']);f=preds[a['run_id']]['fit']
        assert q.shape==p.shape and np.isfinite(q).all() and (q>=0).all() and np.allclose(q.sum(1),1,atol=1e-10)
        if f:
            rows=[[mp[x] for mp,x in zip(m['parent_effect_rank_by_stored_index'],row)] for row in r['parent_rows']]
            rebuilt=make_cpt(rows,m['parent_cardinalities'],m['state_count'],f['family'],f['weights'],f['variance'])[:,m['child_semantic_rank_by_stored_index']]
            max_rebuild=max(max_rebuild,float(abs(rebuilt-q).max()))
        if refit:
            key=preds[a['run_id']].get('key',a['run_id'])
            if key not in fit_cache:fit_cache[key]=predict(tasks[a['task_id']],m,a['valid_rows'],a['family'])[0]
            max_refit=max(max_refit,float(abs(fit_cache[key]-q).max()))
        v=metrics(p,q,m['child_semantic_rank_by_stored_index']);held=[int(s.split(':')[1]) for s in m['held_out_row_ids']]
        row={k:a[k] for k in ['run_id','node_id','method','condition','prompt_design','rag','repetition']}
        row.update(network=m['source_network'],publication_family=m['publication_family'],stratum='scrum' if m['source_network']=='scrum_full_xml' else 'external',primary=m['compression_primary'])
        row.update({f'all_{k}':float(x.mean()) for k,x in v.items()})
        row.update({f'held_{k}':float(x[held].mean()) if held else None for k,x in v.items()});trials.append(row)
        if f and m['compression_primary']:
            idx=[int(s.split(':')[1]) for s in m['anchor_row_ids']];raw=np.array([a['valid_rows'][s] for s in m['anchor_row_ids']])
            anchors.append(dict(row,raw_anchor_tv=float(.5*abs(p[idx]-raw).sum(1).mean()),fitted_anchor_tv=float(.5*abs(p[idx]-q[idx]).sum(1).mean())))
    assert max_rebuild<1e-10, max_rebuild
    if refit:assert max_refit<1e-8,max_refit
    df=pd.DataFrame(trials);df.to_csv(out/'trial-metrics.csv',index=False)
    original=pd.read_csv(expected/'trial-metrics.csv').set_index('run_id')
    computed=df.set_index('run_id').loc[original.index]
    for col in ['all_tv','all_js_bits','all_ordinal_cdf','all_kl_bits','held_tv']:
        assert np.allclose(computed[col],original[col],rtol=1e-10,atol=1e-10,equal_nan=True),col
    keys=['condition','method','prompt_design','rag','repetition'];rep=[]
    for stratum in ['external','scrum']:
        for subset in ['all','primary']:
            g=df[df.stratum.eq(stratum)&(df.primary if subset=='primary' else True)]
            for key,part in g.groupby(keys):
                row=dict(zip(keys,key));row.update(stratum=stratum,subset=subset)
                row.update({k:float(v) for k,v in macro(part,['all_tv','held_tv']).items()});rep.append(row)
    rep=pd.DataFrame(rep);rep.to_csv(out/'replication-macros.csv',index=False)
    primary=[];secondary=[];descriptive=[]
    for stratum in ['external','scrum']:
        for subset,metric in [('primary','held_tv'),('all','all_tv')]:
            g=rep[rep.stratum.eq(stratum)&rep.subset.eq(subset)]
            w=g.groupby(['repetition','method'])[metric].mean().unstack('method').sort_index()
            item=dict(stratum=stratum,subset=subset,contrast='RNM minus direct',metric=metric,direct=float(w.direct.mean()),rnm=float(w.rnm.mean()),**summarize(w.rnm-w.direct))
            item['relative_difference_percent']=100*item['mean']/item['direct'];(primary if subset=='primary' else descriptive).append(item)
            if subset=='all':
                for method in ['direct','rnm']:
                    s=g[g.method.eq(method)]
                    for factor,left,right,name in [('rag',False,True,'RAG minus no-RAG'),('prompt_design','baseline','structured','structured minus baseline')]:
                        w=s.groupby(['repetition',factor])[metric].mean().unstack(factor).sort_index()
                        secondary.append(dict(stratum=stratum,method=method,contrast=name,metric=metric,**summarize(w[right]-w[left])))
    usage=pd.DataFrame([dict(a,**a['usage'],input_plus_output_tokens=a['usage']['input_tokens']+a['usage']['output_tokens']) for a in attempts])
    tokens=[];primary_ids={n for n,r in refs.items() if r['metadata']['compression_primary']}
    for subset in ['all','primary']:
        u=usage if subset=='all' else usage[usage.node_id.isin(primary_ids)]
        for metric in ['output_tokens','input_plus_output_tokens']:
            w=u.groupby(['repetition','method'])[metric].sum().unstack('method').sort_index()
            tokens.append(dict(subset=subset,metric=metric,contrast='RNM minus direct',direct_total=int(w.direct.sum()),rnm_total=int(w.rnm.sum()),savings_percent=float(100*(w.direct.sum()-w.rnm.sum())/w.direct.sum()),**summarize(w.rnm-w.direct)))
    for family in [primary,secondary,tokens]:holm(family,'t_p','t_p_holm');holm(family,'sign_test_p','sign_p_holm')
    stats=dict(primary=primary,secondary_prompt_rag=secondary,all_row_method_descriptive=descriptive,tokens=tokens)
    compare(stats,read(expected/'statistics.json'));save(out/'statistics.json',stats)
    adf=pd.DataFrame(anchors);anchor_tests=[]
    for stratum in ['external','scrum']:
        deltas=[]
        for _,g in adf[adf.stratum.eq(stratum)].groupby('repetition'):
            z=macro(g,['raw_anchor_tv','fitted_anchor_tv']);deltas.append(z.fitted_anchor_tv-z.raw_anchor_tv)
        anchor_tests.append(dict(stratum=stratum,contrast='Fitted minus raw anchor error versus reference, same configurations',**summarize(deltas)))
    holm(anchor_tests,'t_p','t_p_holm');holm(anchor_tests,'sign_test_p','sign_p_holm')
    compare(anchor_tests,read(expected/'anchor-comparison.json')['post_hoc_tests']);save(out/'anchor-tests.json',anchor_tests)
    report=dict(passed=True,nodes=len(refs),trials=len(answers),attempts=len(attempts),cells_per_replication=8,replications=5,all_trial_metrics_match=True,all_statistical_contrasts_match=True,anchor_tests_match=True,max_probability_rebuild_difference=max_rebuild,refitted_from_llm_anchors=refit,max_probability_refit_difference=max_refit if refit else None,no_model_requests=True)
    save(out/'verification.json',report);print(json.dumps(report,indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--refit',action='store_true',help='Also refit weights and variance from LLM anchors; reads no reference probabilities in the fitting call. Takes longer.')
    run(p.parse_args().refit)
