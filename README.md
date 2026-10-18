# LLM construction of software-engineering BN probability tables

Replication materials for **Large Language Models for Bayesian Network Parameterization in Software Engineering: Direct Elicitation versus Ranked Nodes**.

## Study and primary endpoint

The sample contains 61 ordinal conditional nodes from seven BNs in five publication families: Scrum, Chrome 40 and 42, APS, SESSI, and Software logs 3 and 4. Eight conditions cross direct/RNM elicitation, baseline/structured prompts, and no-RAG/qualitative-RAG evidence. Five replications provide 2,440 completed trials and four format repairs. Collection used Codex CLI 0.162.1, requested model `gpt-6-astra`, effort `medium`, on 15–16 October 2026.

The main comparison includes **every CPT row, including anchors**, with equal node weights. Equal publication-family weighting is a sensitivity analysis. Paired tests use five replication blocks, not nodes or rows as independent observations. Results concern agreement with fixed reference CPTs, not predictive calibration or company decision quality. Scope and analysis choices followed inspection of results; inference is exploratory.

Direct mean TV is 0.231711 and RNM mean TV is 0.240422 (RNM minus direct +0.008710). The paired-t contrast is significant under its assumptions. With five pairs, the smallest possible two-sided exact sign-test p is 0.0625; its non-rejection at 5% cannot contradict the consistent direction. No practical-error threshold or downstream utility evaluation establishes practical superiority or equivalence.

## Reading and offline reproduction

`seai-paper.pdf` is the eight-page article; `seai-supplement.pdf` contains detailed methods and analyses. `paper/main.tex` uses the official ACM class and bibliography style. Install Python 3.10+ and the dependencies, extract `replication-package.zip`, then run from its root:

```powershell
python -m pip install -r requirements.txt
python reproduce.py
python complete-table-20261016/analyze.py
python scalability-20261018/estimate.py
python log-node-diagnostic-20261018/diagnose.py
```

These commands need no hosted-model account or new LLM request. `reproduce.py` checks saved evidence and reproduces the earlier restricted diagnostics. **`complete-table-20261016/statistics.json` is the authority for the paper's three full-sample RQs.** The complete-table script recomputes all 2,440 trial metrics, five-block comparisons, and repair-inclusive token accounting. The scalability script separates exact anchor counts from conditional token projections. The log-node diagnostic examines saved raw judgments and fitted tables and reports full-sample single-node influence. Original responses and numerical results are retained.

Optional `python reproduce.py --refit` repeats bounded optimization from saved LLM anchors. The fitter uses judgments and predefined state mappings; reference probabilities enter scoring only. Hosted-model generation is not guaranteed reproducible. `python reconstruct_reference.py` checks the declared numerical reconstruction of the archived 42-node Scrum model, including 25 conditional tables; it does not certify agreement with AgenaRisk's exporter.

## Contents

| Location | Purpose |
|---|---|
| `paper/` | Article, supplement, modular LaTeX, bibliography and official template dependencies. |
| `evaluator/data/` | Reference CPTs, saved answers and predictions, task definitions, attempts and minimal launch receipts. |
| `evaluator/responses/` | Original answer text, including format-repair attempts. |
| `evaluator/ordinal_engine.py` and adapter | RNM integration, bounded fitting, and state-order mapping. |
| `complete-table-20261016/` | Main full-sample scores, statistical tests, protocol and analysis specification. |
| `scalability-20261018/` | Observed token costs, regression coefficients and conditional larger-CPT scenarios. |
| `log-node-diagnostic-20261018/` | Software-log node diagnosis and descriptive influence across all 61 nodes. |
| `posthoc-20261016/`, `posthoc-node-influence-20261016/` | Restricted 25-node reconstruction diagnostics; these are not the main endpoint. |
| `evaluator/expected/`, `evaluator/historical-analysis/` | Earlier numerical analyses and their specifications, retained for traceability. |
| `evaluator/reference-construction/` | Reference construction source and metadata. |
| `collection/` | Reference-free collection kits, including the actual broader 77-target schedule and smoke test. |
| `manifest.json` | SHA-256 hashes of the distributed contents. |

## Reference isolation and interpretation

This is **evaluator-side material**: do not expose the repository or full archive to experimental LLM sessions. New collection requires a separate computer/profile with only the appropriate reference-free collection files, fresh sessions, and the documented controls. The original collection schedule includes 16 targets excluded from the 61-node SE analysis; running it makes new hosted-model requests and is unnecessary for offline reproduction.

Scrum references are numerical reconstructions from archived XML parameters and expressions. Other CPTs describe the contexts of their published studies; SESSI uses the original elicited Appendix A3 table. Third-party datasets retain their own rights. Publisher PDFs, credentials, authoring conversations and internal manuscript reviews are excluded.

Launch receipts omit local paths and session identifiers. Original raw-file hashes remain in attempt records, but full event streams are not distributed. The package supports numerical reproduction and saved-answer inspection, not an independent replay of the original access-control audit.
