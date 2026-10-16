# Post-hoc offline sensitivity analyses

These analyses use saved answers only. They do not replace the original experimental predictions, references, inferential tests, or token totals. The reference-informed fits contain reference CPTs and must remain inaccessible to future experimental sessions.

## Reproduce

From the extracted replication package:

```powershell
python posthoc-20261016/summarize_evidence.py
python posthoc-20261016/sensitivity.py --workers 6
python posthoc-20261016/build_supplement.py
```

The fitting script creates a local cache and can resume incomplete computation. It makes no LLM or network calls. Exact original row order is preserved; every primary RNM frozen fit must reproduce its saved table within 1e-10. The stronger search retains incumbents and checks that fit loss does not increase. It is not a global-optimality certificate. Detailed choices are in `analysis-plan.json` and the source. Original files are hash-checked before/after.

## Non-anchor TV of alternative pipelines

| Pipeline | Scrum | Chrome |
|---|---:|---:|
| Original direct | 0.3184 | 0.2223 |
| Original RNM | 0.2761 | 0.2517 |
| Uniform | 0.4525 | 0.3739 |
| Direct anchors, paired RNM family | 0.2924 | 0.2456 |
| RNM anchors, family by anchor fit | 0.2787 | 0.2413 |
| RNM anchors, stronger search | 0.2761 | 0.2517 |
| RNM anchors, expanded bounds | 0.2761 | 0.2530 |

## Reference-informed complete-table TV

| Search | Scrum | Chrome |
|---|---:|---:|
| All families, stronger search | 0.0560 | 0.1592 |
| Expanded bounds | 0.0559 | 0.1589 |
| Expanded bounds and direction enumeration | 0.0260 | 0.1322 |

These latter diagnostics optimize and evaluate against complete references. They must not be described as validated predictions, error floors, or improvements to the original blinded experiment. No new hypothesis tests or corrected token totals are introduced. Additional CPU work is outside the original collection-cost endpoint.

## Files

- `alternative-trials.csv`, `alternative-summary.json`, `alternative-predictions.json`: all saved-response variants, their fitted parameters and predictions.
- `reference-informed-fits.json`, `reference-best-by-node.csv`, `reference-summary.json`: all-family, bound, and direction diagnostics.
- `descriptive-evidence.json`, `baselines-and-packets-by-node.csv`, `primary-node-effects.csv`: baselines, secondary metrics, selected examples, packet coverage, and node-level effects.
- `verification.json`: preservation checks and computational validation.
- `paper/supplement.tex` (at package root): anonymous readable report with full procedures, examples, evidence cards, and node/replication differences.

## Data dictionary

In `alternative-trials.csv` and `alternative-summary.json`, `anchor_tv` means error against **reference probabilities on the original anchor configurations**, while `held_tv` and `all_tv` score reference agreement on non-anchor and all configurations. In each stored `fit` object, `anchor_tv` is the optimizer's **fitting residual against its supplied target judgments**. These quantities differ: the alternative pipeline targets are LLM judgments; reference-informed targets are complete reference tables. The reference-informed summary uses `all_tv` for model selection. Do not interpret its `held_tv` as out-of-sample error, since those rows also entered its objective.

Examples select the node nearest each stratum's median per-node effect, then the all-middle aligned anchor. They are illustrative and do not represent the largest observed benefit or harm. Secondary metrics and baselines are descriptive, post-hoc additions.
