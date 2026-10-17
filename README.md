# LLM elicitation of SE BN CPTs — current full-sample analysis

Private author-review replication package. All three RQs now evaluate all 61 nodes in seven BNs; the agreement endpoint includes every CPT row, anchors and non-anchors. The paper leads with the overall comparison and reports all seven BNs to explain variation.

## Start here

Read [COMPLETE-TABLE-ANALYSIS.md](COMPLETE-TABLE-ANALYSIS.md), [PROTOCOL.md](PROTOCOL.md), and [PROPOSAL.md](PROPOSAL.md). Download and extract `replication-package.zip`. From its root, with Python and the listed dependencies available:

```powershell
python complete-table-20261016/analyze.py
python complete-table-20261016/generate_figure.py
```

The archive's historical root README and `evaluator/expected` remain unchanged for provenance. Their non-anchor headline analysis is superseded by `complete-table-20261016` for the current paper. `reproduce.py` and `reconstruct_reference.py` still reproduce the historical evidence; neither makes model calls. The current analysis reads saved predictions without refitting.

## Current findings

Node-weighted complete-table TV is **0.2317 direct versus 0.2404 RNM**, a **3.76% increase** with RNM. Equal publication-family weighting retains the direction. Both paired-t contrasts reject after Holm adjustment, but exact sign tests do not with five replications. RNM is closer on 31 of 61 nodes; larger losses elsewhere outweigh those gains. All eight conditions and every BN are reported. Structured prompting has limited support for direct elicitation; qualitative RAG demonstrates no benefit. RNM uses 12.1% fewer output tokens and 0.61% fewer total tokens.

Scope, endpoint, weighting, and inference are exploratory choices after inspection of earlier results. These comparisons do not establish universal company probabilities, practical decision value, or calibration. The saved original answers, references, predictions, and token records are unchanged: all 3,161 existing non-paper files pass byte-for-byte preservation checks.

## Files

- `seai-paper.pdf`: eight-page paper including 24 references.
- `seai-supplement.pdf`: detailed construction, all-condition statistics, and explicitly restricted historical diagnostics.
- `paper-source.zip`: editable ACM sources; compile `main.tex` and `supplement.tex` separately. Official template unchanged.
- `replication-package.zip`: frozen data, collection inputs, original analyses, new full-sample analysis, manuscript, independent review records, and reproducibility scripts.
- `complete-table-verification.json`: successful current metric, accounting, and preservation checks.
- `verification.json`: earlier full-refit validation, retained unchanged.
- `POSTHOC-ANALYSES.md` and `NODE-INFLUENCE.md`: historical supporting diagnostics, not the current primary endpoint.
- `manifest.json` and `SHA256SUMS.txt`: archive-content and delivery hashes.

## Isolation and access

This repository remains private for author review. The archive includes reference CPTs and evaluator outputs; do not expose it to experimental LLM sessions. The original collection-only inputs preserve reference isolation. No new LLM requests or RNM fits were made for this amendment.

The export preserves original answer text and hashes plus operational receipts with local paths/session identifiers removed. Full client event streams are not distributed, so numerical analyses reproduce but the entire historical access-control audit cannot be repeated from this export alone. No publisher PDFs, authentication files, or authoring conversations are included. No public redistribution license or anonymous reviewer access is asserted.

## Wording clarification: uneven representation

The Abstract, Introduction, Method, and Results now introduce the unequal contribution of nodes before explaining equal-study weighting. Scrum and Chrome supply 52 of 61 nodes and therefore dominate the node-weighted mean. Giving each of the five source studies equal weight checks whether that concentration changes the overall direction; direct elicitation still has lower mean error. This is uneven representation of source studies, not imbalance in outcome classes. The author's latest abstract closing edit is preserved. All numerical analyses, data, and the supplement remain unchanged.

## Abstract clarification: structured prompting

The abstract now explains that structured prompts clarified conditioning, framed probabilities as hypothetical frequencies, and requested consistency checks. The paper remains eight pages and the abstract is 246 words. All numerical analyses and the supplement are unchanged.

## Abstract clarification: qualitative RAG

The abstract now explains that qualitative RAG supplied short passages on domain relationships without reference probabilities or numerical parameters. The paper remains eight pages and the abstract is 239 words. All numerical analyses and the supplement are unchanged.

## Introduction source citations

The Introduction now cites the source study for each of the five application areas covered by the seven BNs. The paper remains eight pages. All numerical analyses and the supplement are unchanged.

## Related Work organization

Section 2 now opens with a roadmap, reviews semi-automatic CPT construction in Section 2.1, and discusses LLM construction in Section 2.2, closing with our contribution and Table 1. Current author edits to the Introduction are preserved. The paper remains eight pages. All numerical analyses and the supplement are unchanged.

## Method flow and condition descriptions

Section 3 now introduces the factorial design, describes the seven BNs and evaluated CPTs, separates shared inputs from method-specific outputs, and explains each prompt/evidence combination. Reference construction mechanics remain in the supplement. The paper remains eight pages. All numerical analyses and the supplement are unchanged.

## RNM background explanation

Section 2.1 now focuses on RNM, explaining ordinal intervals, parent aggregation, child-state probability mass, parameter roles, fitting, and representational assumptions, followed by brief alternatives. The paper remains eight pages. All numerical analyses and the supplement are unchanged.

## Prompt examples and RQ-led results

Section 3 adds simplified prompt excerpts and a verified Cohesion RAG card. Section 4 explains the tables and figures through the three RQs. The accidentally removed related-work comparison table and its cross-reference are restored as requested. The paper remains eight pages. All numerical analyses and the supplement are unchanged.

## Discussion interpretation and implications

Section 5 interprets all three RQs against the literature and distinguishes research and practitioner implications. It separates reconstruction compatibility, the information supplied by prompting and RAG, and elicitation burden from token usage. The paper remains eight pages. All numerical analyses and the supplement are unchanged.

## Study-specific threats to validity

Section 6 now links each study-specific threat to its affected conclusions, existing safeguards, and residual uncertainty. Reference validity is explicit alongside construct, internal, conclusion, and external validity. The paper remains eight pages. All numerical analyses and the supplement are unchanged.
