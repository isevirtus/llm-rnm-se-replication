# Current analysis: complete CPTs, all 61 SE nodes

This directory contains the main complete-table analysis. Start with [PROTOCOL.md](PROTOCOL.md), [PROPOSAL.md](PROPOSAL.md), and [ANALYSIS-AMENDMENT.md](ANALYSIS-AMENDMENT.md). `evaluator/expected` contains the earlier restricted non-anchor diagnostics; those are separate from the main endpoint.

All 61 conditional nodes from seven BNs are evaluated on every CPT row, including RNM anchors. There are five publication families. Both the node-weighted primary result and family-weighted sensitivity include the entire sample. No model calls or RNM fits were repeated.

## Reproduce

From the extracted package root, with the package's Python dependencies installed:

```powershell
python .\complete-table-20261016\analyze.py
python .\complete-table-20261016\generate_figure.py
```

The first command reads frozen reference/prediction arrays and request accounting, recomputes row metrics, aggregates five paired replication blocks, runs the specified tests, and checks the evidence hashes listed in `preservation-baseline.json`. It writes only within this directory. `verification.json` records successful validation; `statistics.json` is the numerical authority for the revised RQs. 

## Findings

Equal-node mean TV is 0.231711 for direct elicitation and 0.240422 for RNM: RNM minus direct is +0.008710, or +3.76%. The pointwise 95% paired-t interval is [0.007627, 0.009794]; Holm-adjusted paired-t p=0.0000478, and adjusted exact sign p=0.125. With five nonzero pairs, the minimum two-sided exact sign-test p is 0.0625 before adjustment, so rejection at 5% is impossible. Equal-family TV is 0.193708 versus 0.218878, with the same direction and the same sign-test limitation. RNM is closer for 31 of 61 nodes; larger losses elsewhere outweigh those gains.

Structured prompting reduces node-weighted direct TV by 0.004133 (Holm paired-t p=0.0255). This does not extend consistently across weighting rules or exact sign tests. Qualitative RAG demonstrates no benefit. RNM uses 40.14% fewer requested distributions and 12.12% fewer output tokens, but only 0.61% fewer total tokens. The total-token contrast does not reject under the paired-t test.

These are exploratory results for a fixed, availability-based benchmark and one model configuration. Five replication blocks measure repeatability on that benchmark, not uncertainty over all SE companies or BNs. The amendment was made after earlier results were inspected. Pointwise intervals and separate Holm families do not provide study-wide confirmatory inference or establish practical significance.

## Output map

- `trial-metrics.csv`: 2,440 retained complete-table trial scores.
- `condition-blocks.csv`, `condition-means.csv`: all eight conditions under both weighting rules.
- `node-means.csv`, `network-means.csv`: all 61 nodes and seven BNs; descriptive comparisons.
- `tokens-by-condition.csv`: repair-inclusive usage.
- `statistics.json`: five-block RQ1/RQ2/RQ3 contrasts, intervals, raw and Holm p-values.
- `figure-full-sample.tex`, `figure-data.json`: supplementary full-sample figure and its values.
- `preservation-baseline.json`, `verification.json`: evidence-preservation check.

This is evaluator-side material. Never put this directory, references, predictions, or the full package in experimental LLM sessions.
