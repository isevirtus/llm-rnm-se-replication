# Revised proposal: LLM-assisted construction of complete SE CPTs

## Motivation and contribution

BNs support transparent SE decisions under uncertainty but require costly probability elicitation. We compare two ways to use an LLM for constructing the complete CPTs that a BN user ultimately receives: directly elicit every row, or elicit selected judgments and use RNM to fit and reconstruct all rows. The study tests this accuracy–effort tradeoff across the entire eligible SE sample, rather than making table completion beyond anchor rows the primary task.

## Research questions and directional expectations

1. **RQ1:** Does LLM-assisted RNM improve complete-CPT agreement compared with direct elicitation across the full sample? The directional expectation was lower error with RNM through structured aggregation. Every row, including anchors, contributes to the comparison.
2. **RQ2:** How do structured elicitation prompts and qualitative RAG affect complete-CPT agreement across the full sample? The expectation was improved agreement from explicit elicitation guidance and contextual evidence.
3. **RQ3:** How does RNM trade complete-CPT agreement against requested distributions and computational effort across the full sample? Fewer requested probability vectors and output tokens were expected; total tokens are measured rather than inferred from vector counts.

These are exploratory expectations, not preregistered confirmatory hypotheses. The current endpoint, weighting, and statistical plan were chosen after inspecting earlier analyses. RQ4/domain comparison is outside the current paper.

## Sample and design

The sample contains 61 ordinal conditional nodes in seven published SE BNs: Scrum (25), Chrome 40 (15), Chrome 42 (12), APS (3), SESSI (1), software logs 3 (4), and software logs 4 (1). They represent five publication families. Complete references cover 421 CPT rows; RNM requests 252 anchor distributions per prompt/evidence combination and replication. One-parent nodes and nodes with every row elicited remain in the sample because fitting can alter the elicited distributions.

The completed 2×2×2 design crosses method (direct/RNM), prompt (baseline/structured), and evidence (no RAG/qualitative RAG), with five replications using GPT-6 Astra at medium effort. Numerical references remained hidden from experimental sessions and RNM fitting. This revision reuses saved responses and predictions without recollection or refitting.

## Expected contribution and limits

The contribution is a reproducible evaluation of complete-table construction pipelines, including agreement, sensitivity to benchmark weighting, and measured token use. The primary estimand gives nodes equal weight. Equal publication-family weighting checks a different full-sample estimand. All seven BNs are shown to explain variation, without treating network-specific differences as the main question.

Reference agreement is not company-level predictive validity or probability calibration. The availability-based sample, small tables, model configuration, reconstructed Scrum reference, and five repeated blocks limit generalization. Local expert validation and held-out outcome evaluation remain necessary before deployment. Detailed execution and analysis rules are in [PROTOCOL.md](PROTOCOL.md).
