# Chrome version differences and leave-one-node-out diagnostics

Post-hoc descriptive reaggregation of the original 25 primary targets (14 Scrum; 11 Chrome). No model requests, RNM fitting, probability edits, new hypothesis tests, or changes to original results are performed.

## Reproduce

From the extracted replication package, run:

```powershell
python posthoc-node-influence-20261016/analyze.py
python posthoc-20261016/build_supplement.py
```

The first command only reads the frozen primary trial scores, original statistical summary, and variable names. It checks that its original baseline agrees within 1e-12 and writes only to this directory. The second rebuilds the readable supplement using the saved earlier diagnostics and this section; it does not rerun the computational fitting analyses.

## Estimator

Remove one primary target at a time and re-average remaining targets within its network. Chrome 40 and Chrome 42 each retain one-half weight. The four prompt/evidence cells and five replication blocks remain equally weighted. Non-anchor configurations and predictions are unchanged. These omissions are influence diagnostics, not a revised sample, cross-validation, independent observations, or a new significance analysis.

| Network | Primary targets | Direct TV | RNM TV | RNM minus direct |
|---|---:|---:|---:|---:|
| Chrome 40 | 6 | 0.2069 | 0.2102 | +0.0033 |
| Chrome 42 | 5 | 0.2377 | 0.2933 | +0.0556 |
| Scrum | 14 | 0.3184 | 0.2761 | -0.0423 |

| Stratum | Omissions | Minimum remaining difference | Maximum remaining difference |
|---|---:|---:|---:|
| Scrum | 14 | -0.0471 | -0.0344 |
| Chrome | 11 | +0.0168 | +0.0375 |

Every omission preserves its stratum's original direction in all five blocks. Chrome 42 Major Contributors contributes 53.2% of the original net Chrome contrast under the original weights. Omitting it and renormalizing within its network leaves a difference of +0.0168. This is descriptive concentration, not a causal attribution or justification for excluding that target.

## Files

- `network-summary.csv` and `network-blocks.csv`: three network means and their 15 original replication summaries.
- `leave-one-node-out.csv`: all 25 omission summaries; `delta` is RNM minus direct primary non-anchor TV.
- `leave-one-node-out-blocks.csv`: 125 omission-by-replication estimates.
- `summary.json`: estimator, summary results, concentration calculation, and relative input hashes.
- `verification.json`: completeness, baseline reproduction, and input preservation checks.
- `supplement-section.tex`: generated section appended by the supplement builder.

The original primary sample remains intact. No p-values or confidence intervals are computed for these diagnostics. Reference CPTs remain evaluator-side material and must stay inaccessible to experimental LLM sessions.
