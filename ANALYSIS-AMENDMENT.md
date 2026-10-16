# Complete-table analysis amendment — 16 October 2026

The author requested complete-table comparison across all 61 SE nodes in all seven BNs. This amendment is specified after inspecting earlier results and before calculating the new aggregate outputs. It is exploratory, not preregistered. Historical collection, fits, trial scores, and statistics remain immutable.

RQ1: Does LLM-assisted RNM improve complete-CPT agreement compared with direct elicitation across the full sample?
RQ2: How do structured prompts and qualitative RAG affect complete-CPT agreement across the full sample?
RQ3: How does RNM trade complete-CPT agreement against requested distributions and computational effort across the full sample?

Primary endpoint: mean row TV within each of 61 nodes, then equal node weights. For the RNM-minus-direct contrast, average all four prompt/evidence combinations equally within each of five matched replication blocks. All anchors and non-anchors contribute, including one-parent nodes and nodes whose prompts cover all rows. Reference probabilities never enter experimental fitting.

Sensitivity endpoint: mean within nodes, equal node weights within each BN, equal BN weights within each publication family, then equal weights over all five publication families. This includes all 61 nodes. It changes the estimand, not the sample. Report differences explicitly.

Inference: paired t tests and pointwise 95% t intervals on five replication-block differences (df=4); two-sided exact sign tests as small-sample sensitivity. No node/row pseudoreplication. Holm correction across two RQ1 weighting contrasts; across eight RQ2 contrasts (two methods x two factors x two weighting rules); across two RQ3 token contrasts (output and input+output). Confidence intervals are not simultaneous. Families are separate and provide no study-wide multiplicity guarantee. No equivalence margin; non-significance is not equivalence. Replications do not support population inference to new companies/networks.

Presentation: eight full-sample condition means; seven-network complete-table breakdown, descriptive without network significance testing; complete-table secondary distances (JS, ordinal CDF, smoothed KL). Main token analysis uses all 61 nodes and all attempts, including four repairs. Existing non-anchor, anchor, search and direction diagnostics remain supplementary and labeled with their specific subsets. No new model requests or RNM fits.

Preservation: all existing non-paper artifacts remain byte-identical; new calculations and this amendment live in complete-table-20261016. The frozen historical protocol/expected results remain under evaluator/expected; this amendment governs the revised paper's endpoint and weighting.
