# LLM elicitation of software engineering Bayesian-network CPTs

Private author-review replication package for **Direct Elicitation versus Ranked Nodes**: 61 ordinal SE targets, eight conditions, five replications, 2,440 initial trials and four format repairs. The primary analysis reports Scrum and Chrome separately.

## Start here

1. Download `replication-package.zip` and extract it into an empty folder. The archive preserves the full folder structure and contains its own detailed README and SHA-256 manifest.
2. From that extracted folder, with Python 3.10 or newer:

```powershell
python -m pip install -r requirements.txt
python reproduce.py
python reconstruct_reference.py
```

3. Optionally repeat all RNM optimization from the saved LLM anchors:

```powershell
python reproduce.py --refit
```

No model requests are made by these three entry points. The scripts also shown at the repository root are for convenient inspection; run them inside the extracted package, where their data and modules reside.

## Verified results

All 2,440 trial metrics, statistical contrasts, and same-anchor tests reproduce. Rebuilding and fully refitting the RNM probabilities both yielded maximum difference 0.0 against the saved predictions. The separate XML reconstruction reproduces all 42 Scrum nodes (25 conditional tables) exactly under the declared numerical conventions. This does not certify AgenaRisk exporter equivalence.

Primary TV: Scrum 0.3184 direct versus 0.2761 RNM; Chrome 0.2223 versus 0.2517. Both differences survive Holm-adjusted paired t-tests over five replication blocks; neither exact sign test rejects. RNM reduces output tokens 12.1% across all targets, but total tokens only 0.61%. Scope selection and testing were post hoc.

## Files

- `replication-package.zip`: collection kits, saved answers and attempt records, frozen references, fitting/scoring code, protocols, expected results, complete manuscript sources, and validation reports.
- `paper-source.zip`: editable anonymous ACM manuscript and unchanged official class/style; compile `main.tex` with pdfLaTeX and BibTeX.
- `seai-paper.pdf`: compiled manuscript for author review.
- `verification.json`: full RNM refit and numerical reproduction result.
- `manifest.json`: hashes of files inside the replication archive.
- `SHA256SUMS.txt`: hashes of these top-level delivery files.

## Keep reference CPTs hidden from experimental sessions

**This repository and its archives are evaluator-side material. Never clone or extract them on an experimental LLM computer/profile.** Reference CPTs, results, and manuscript conclusions are present. A subfolder is not an access boundary.

For collection, transfer only the `collection/` directory from the extracted package to a separate computer/profile with no references, evaluator, authoring conversations, or connected research sources. The preserved working formal kit has the actual historical 77-target schedule; the analysis filters to the 61 retained SE targets. Starting that kit makes new hosted-model requests; it is not needed to reproduce the results offline.

## Provenance and limits

The exported package preserves original answer text and hashes plus operational receipts with local paths/session identifiers removed. Full client event streams are not distributed: numerical analyses can be reproduced, but the entire historical access-control audit cannot be repeated from this export alone. The detailed README documents this boundary.

No public artifact, anonymous reviewer access, or third-party redistribution license is asserted. This repository is private for author review. No original publisher PDFs, authentication files, or authoring conversations are included. The manuscript has not been submitted to a conference.

## Revision: offline sensitivity analyses (16 October 2026)


The revised paper adds a uniform baseline, secondary metrics, matched direct-anchor fits, aggregation-family selection by anchor fit, stronger searches, expanded bounds, and reference-informed direction diagnostics. Read `POSTHOC-ANALYSES.md` for the results and reproduction commands; source, saved fitted tables, and verification records are in `posthoc-20261016/` inside the archive. `paper/supplement.tex` contains full procedures, example distributions, qualitative cards, and node-level effects.

The Scrum benefit and Chrome disadvantage persist across the saved-response alternatives. Complete-reference searches are in-sample best-found approximations, not validated predictions, global optima, or RNM error floors. The revised interpretation concerns the tested pipeline.

All 3,129 protected original evidence and collection files remain byte-identical. No new LLM calls were made. The original predictions, reference CPTs, statistical tests, and token totals are unchanged. `posthoc-verification.json` documents preservation and checks; `validation/revision-20261016-reproduction.json` inside the package records another successful reproduction of all original trial scores and statistical contrasts. The original `verification.json` remains the earlier full-refit validation record.

These additions are explicitly post hoc and descriptive; no new p-values or collection-cost totals are substituted. The package remains evaluator-only and the repository remains private for author review.

## Revision: Chrome versions and leave-one-node-out checks (16 October 2026)


The main paper now reports Chrome 40 and Chrome 42 separately and summarizes all 25 single-target omission checks. The six-page supplement contains the version means, complete omission tables, and aggregation details. See `NODE-INFLUENCE.md` for the portable reproduction command and interpretation.

Chrome 40's primary RNM-minus-direct TV is +0.0033, compared with +0.0556 for Chrome 42. Every omission preserves the original direction in all five blocks: Scrum remains favorable to RNM and Chrome unfavorable. The results are descriptive post-hoc influence diagnostics, not significance tests, cross-validation, or a revised sample. All original predictions, reference tables, statistical tests, and token totals are unchanged; no new model calls or fitting were performed for this revision.

The archive includes `posthoc-node-influence-20261016/analyze.py`, all 125 omission/block records, 25 omission summaries, 15 network/block records, network means, input hashes, and verification outputs. The paper and supplement compile; the official template remains unchanged. Newer author edits to the abstract were preserved.


## Revision: motivation, scope, and terminology (16 October 2026)

The Abstract preserves the author's opening and clarifies the relationship between the 61-node/seven-BN sample and the 25 multi-parent primary targets. Application areas introduce the reference contrasts. The Introduction now moves from transparency and limited data in SE decisions to BNs, CPT-construction cost, semi-automatic methods, LLM elicitation, and the study's three RQs. Seven verified references were added; the cited WSA/RNM comparison is explicitly a preprint. BN/BNs and RAG are used consistently after definition.

This is a prose and bibliography revision only. All non-paper replication artifacts remain byte-identical to the previous delivery, including original results and both post-hoc analysis directories. The official LaTeX template is unchanged. The expanded author-review paper is nine pages (including references), with a six-page supplement; an eight-page submission target still requires a separate condensation pass. No new model calls, fits, or inferential tests were performed.


## Revision: related-work comparison (16 October 2026)

Section 2 now compares five LLM-assisted BN studies with this experiment in Table 1. The table distinguishes elicitation granularity, numerical versus qualitative evidence, evaluation materials, and numerical CPT agreement versus modeling/usability or downstream endpoints. The accompanying synthesis positions the study as a comparison of sparse LLM anchors plus RNM reconstruction against complete-table elicitation, together with prompt/RAG treatments and computational effort. It acknowledges prior LLM-plus-fitting approaches. The virtual-survey reference is explicitly identified as a preprint.

Independent review resolved three scope clarifications. The paper compiles successfully and its table and page flow were visually inspected. The author-review paper is 10 pages including references; the unchanged supplement is 7 pages. The eight-page target still requires a separate condensation pass. The official template, author-edited abstract, and all other substantive sections are unchanged.

All 3,161 non-paper replication files remain byte-identical to the preceding delivery. Original collection, responses, CPTs, statistical analyses, token totals, and offline sensitivity analyses are unchanged. No new model calls, fits, or statistical tests were performed.


## Revision: explained results and published Scrum provenance (16 October 2026)

The Results now follow the three research questions through the method contrast, prompting and qualitative RAG, and token accounting. Two vector figures show replication-level effects and anchor fitting, followed by explained Cohesion and Major Contributors CPT examples. The examples are explicitly selected contrasting illustrations, not representative cases. Full condition means and statistical tables are in the supplement. Figure data and `paper/generate_figures.py` reproduce the plots from saved predictions without fitting or testing.

The paper now cites the published SEKE 2017 Scrum framework (DOI 10.18293/SEKE2017-139). It distinguishes the publication's 44-node, five-state description from the evaluated 42-node, three-state XML. Operational hash, reconnect, and collection-history details are in `paper/collection-audit.md`. The material disclosure about post-result scope and statistical-plan selection remains in Threats to Validity.

The paper has 10 pages including references; the expanded supplement has 7 pages. Both compile and the revised plots, tables, and page flow were visually inspected. The main paper still needs a separate condensation pass for the eight-page target. The official template, author-edited abstract, and comparative related-work section are preserved.

All 3,161 existing non-paper artifacts remain byte-identical. Original experimental results, reference CPTs, saved answers, predictions, tests, and token totals are unchanged. No new model requests, RNM fits, or statistical tests were performed. Independent review found no major issues; three minor interpretation refinements were resolved.


## Revision: author comments and expanded Conclusion (16 October 2026)

The latest manuscript addresses all 16 author comments on the Abstract, Introduction, and Method. The Abstract follows context, aim, method/sample, results, and implications. The Introduction motivates structured prompting and qualitative RAG before introducing the factorial design, explains why 25 nodes test reconstruction on unqueried configurations, and cites the BN knowledge-engineering rationale. Method explains the LLM's requested outputs, single-parent treatment, parent influence directions, and an actual qualitative evidence card. The same explanation-first approach was applied across the manuscript. Conclusion now synthesizes the findings, interpretation, token tradeoff, SE implications, study scope, and specific future work.

This revision supersedes the previous note that the Abstract and Introduction were unchanged. It incorporates the preceding narrative revision's two figures, explained CPT examples, published Scrum-framework citation, and expanded supplement. The main draft is 10 pages, and the supplement is 7 pages. A separate condensation pass is still required for the eight-page target; the official template has not been modified. The built-in compiler and Overleaf compilation passed, and the revised pages were visually inspected. Independent review found no actionable issues; the strict source audit passed with 24 references.

All 3,161 existing non-paper files are unchanged. No new model calls, RNM fits, statistical tests, or substituted results were introduced. The package remains private for author review.
