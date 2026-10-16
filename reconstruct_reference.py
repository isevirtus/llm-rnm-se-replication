"""Reconstruct and check the frozen 42-node Scrum XML reference offline."""
from pathlib import Path
import json,sys,hashlib
import numpy as np
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'evaluator'))
sys.path.insert(0,str(ROOT/'evaluator/reference-construction'))
from reconstruct_full_scrum import reconstruct

if __name__=='__main__':
    folder=ROOT/'evaluator/reference-construction'
    original=json.loads((folder/'scrum-reference.json').read_text(encoding='utf-8'))
    source=folder/'scrum-source.xml'
    assert hashlib.sha256(source.read_bytes()).hexdigest()==original['source_sha256']
    current=reconstruct(source,ROOT/'reproduced/reference')
    assert current['assumptions']==original['assumptions']
    old={n['id']:n for n in original['nodes']}; assert len(current['nodes'])==42
    maximum=0.
    for n in current['nodes']:
        o=old[n['id']];assert n['states']==o['states'] and n['parents']==o['parents']
        assert [r['parent_state_indices'] for r in n['rows']]==[r['parent_state_indices'] for r in o['rows']]
        maximum=max(maximum,float(abs(np.array([r['probabilities'] for r in n['rows']])-np.array([r['probabilities'] for r in o['rows']])).max()))
    assert maximum<1e-12
    report={'passed':True,'nodes':42,'conditional_nodes':25,'conditional_rows':249,'max_probability_difference':maximum,'agena_export_equivalence_certified':False}
    (ROOT/'reproduced/reference-validation.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))
