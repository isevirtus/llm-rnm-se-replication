# Current protocol: full-sample complete-table evaluation

## Status and provenance

This is the current analysis protocol for the revised manuscript. Collection is complete. It supersedes the historical restricted non-anchor endpoint and headline Scrum/Chrome-only comparisons; it does not overwrite historical collection or analysis records. See [ANALYSIS-AMENDMENT.md](ANALYSIS-AMENDMENT.md) for the change record. The scope, endpoint, weights, and tests are exploratory choices made after earlier results were inspected.

## Scope and conditions

Include all 61 retained SE conditional nodes from seven BNs and five publication families. References contain 421 conditional rows. For each node, cross direct/RNM, baseline/structured prompting, and no-RAG/qualitative-RAG, yielding eight conditions. Five matched replication blocks give 2,440 retained trials. Four format repairs bring usage accounting to 2,444 attempts. Do not rerun completed valid trials for this revision.

The collection requested `gpt-6-astra`, `medium` effort through Codex CLI 0.162.1 on 15–16 October 2026. Each request used a fresh session, with shuffled order within replications; temperature and generation seed were unspecified. Reference CPTs, XML/CMP sources, full papers, evaluator code, and authoring conversation were inaccessible. Tools, browsing, connectors, and memory were disabled. The archived collection materials preserve exact prompts, row lists, definitions, directions, evidence packets, and request order.

## Elicitation and construction

Both methods receive the same definitions, states, professional-role framing, and parent influence assumptions. Direct elicitation returns every CPT row. RNM returns predetermined anchor distributions and an aggregation family (weighted mean, weighted minimum, weighted maximum, or minimum–maximum mixture); deterministic reference-blind fitting estimates weights and variance. With one parent, the direction-aligned parent value supplies the mean. Anchor selection uses state configurations without reference probabilities. All-low, all-high, all-middle, one-high/rest-low, and one-low/rest-high configurations are deduplicated.

RNM maps states to equal intervals in [0,1], reverses negative influences, and averages normalized truncated-normal probabilities over five endpoint-inclusive points per parent interval. The saved fits minimize mean anchor TV to LLM answers with eight deterministic starts. Original parameter bounds, integration and optimization settings remain unchanged; the paper supplement and original evaluator code contain exact equations and settings. This analysis consumes the saved fitted predictions and performs no new fit.

Structured prompts add conditional-event clarity, hypothetical counts among 100 comparable cases (fractional counts allowed), evidence/assumption separation, and consistency checks. The hypothetical cases supply no observations. RAG supplies fixed qualitative cards matched by context and variable tags, up to three positive-scoring cards; packets contain 24–103 words, median 72. Cards exclude reference probabilities and numerical parameters. Both evidence arms already receive definitions, so this tests additional qualitative context, not live retrieval or company data. Input budgets are not equalized.

The Scrum reference is reconstructed from archived XML parameters and expressions (42 nodes, three states; 25 conditional targets), which differs from the published framework's 44-node/five-state description. Other references are complete stored CPTs; SESSI uses its source's original elicited table. No independently certified AgenaRisk export validates the Scrum reconstruction.

## Validity and preservation

Collection required exact row/state sets, finite probabilities in [0,1], and normalization within 1e-6. At most one fresh-session format repair was permitted without reference feedback. All trials yielded valid responses, with no fallback distributions. Original predictions, responses, references, and usage logs remain immutable. Validate all 3,161 pre-existing non-paper file hashes before accepting new aggregate outputs. Keep evaluator material hidden if future collection occurs.

## Outcomes and aggregation

The primary distance is row total variation, TV(p,q)=0.5×sum(abs(p−q)). Average **all rows within each node**, including RNM anchors and non-anchors. Keep one-parent and all-anchor nodes. These rows evaluate the final table, and fitting on LLM judgments does not expose reference probabilities.

The primary full-sample score gives the 61 node scores equal weight. The sensitivity first averages nodes within each BN, then BNs within each publication family, then all five families equally. Both include all 61 nodes; they answer different weighting questions. Do not silently average only Scrum/Chrome or pool rows so large CPTs dominate. Report all seven BN means descriptively and node-level effects without network-specific significance claims.

RQ1 averages all four prompt/evidence combinations equally within each replication and compares RNM minus direct. RQ2 compares structured minus baseline and RAG minus no RAG within each method, averaging the other factor. Report all eight condition means under both weights. Secondary descriptive metrics are JS divergence in bits, mean absolute ordinal-CDF distance over c−1 cutpoints, and KL with 1e-8 additive smoothing and renormalization, using the same complete-table weights. Do not label CPT KL as joint-distribution KL.

RQ3 counts requested vectors before repairs and sums reported tokens over every attempt. Total=input+output; cached-input and reasoning-output counts are subsets. Compare output and total tokens using replication totals. Latency and offline fitting time are descriptive. Do not infer monetary cost under subscription access.

## Statistical comparisons

Use the five matched replication-block differences, not nodes, rows, or requests as independent observations. For each contrast, report the effect, pointwise 95% paired-t interval (df=4), two-sided paired-t p-value, and exact two-sided sign p-value. Use separate Holm families: two RQ1 weighting contrasts; eight RQ2 contrasts (two methods × two factors × two weights); two RQ3 token contrasts. Intervals are not simultaneous and separate families do not provide study-wide confirmatory control.

Five blocks cannot establish normality, stationarity, or independence. Even five concordant signs give raw p=0.0625. No equivalence or practical-effect margin was prespecified. Distinguish failure to reject, effect size, and practical importance; do not extrapolate fixed-benchmark block uncertainty to new organizations or all BNs.

## Supporting diagnostics and reporting

Historical non-anchor, raw/fitted-anchor, alternate-fit, Chrome-version, and leave-one-node-out diagnostics remain clearly labeled supporting analyses, often restricted to 25 compression-subset nodes. They neither replace full-table predictions nor define the main RQ endpoint. The main figure and tables cover every BN and the overall weighted comparison.

Run `python complete-table-20261016/analyze.py` from the package root. Inspect `verification.json`, `statistics.json`, and the complete condition/node/network CSVs. `generate_figure.py` regenerates the current main figure. Preserve historical `evaluator/expected` unchanged and identify this directory as the current analysis when distributing the package.
