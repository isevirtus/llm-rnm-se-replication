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
- `seai-paper.pdf`: eight-page manuscript, including all 24 references.
- `seai-supplement.pdf`: expanded methods and supporting results; compile `supplement.tex` from the source archive.
- `verification.json`: full RNM refit and numerical reproduction result.
- `manifest.json`: hashes of files inside the replication archive.
- `SHA256SUMS.txt`: hashes of these top-level delivery files.

## Keep reference CPTs hidden from experimental sessions

**This repository and its archives are evaluator-side material. Never clone or extract them on an experimental LLM computer/profile.** Reference CPTs, results, and manuscript conclusions are present. A subfolder is not an access boundary.

For collection, transfer only the `collection/` directory from the extracted package to a separate computer/profile with no references, evaluator, authoring conversations, or connected research sources. The preserved working formal kit has the actual historical 77-target schedule; the analysis filters to the 61 retained SE targets. Starting that kit makes new hosted-model requests; it is not needed to reproduce the results offline.

## Provenance and limits

The exported package preserves original answer text and hashes plus operational receipts with local paths/session identifiers removed. Full client event streams are not distributed: numerical analyses can be reproduced, but the entire historical access-control audit cannot be repeated from this export alone. The detailed README documents this boundary.

No public artifact, anonymous reviewer access, or third-party redistribution license is asserted. This repository is private for author review. No original publisher PDFs, authentication files, or authoring conversations are included. The manuscript has not been submitted to a conference.

## Current paper: eight pages (16 October 2026)

The main paper is **8 pages including references**, with a **9-page supplement**. The official ACM class, fonts, margins, and spacing are unchanged. The paper retains all three RQs, the 61-node/seven-BN sample and 25-target primary rationale, eight conditions, the qualitative RAG card and RNM anchor example, two explanatory figures, separate Scrum and Chrome findings, Chrome version and leave-one-node-out summaries, statistical qualifications, token accounting, and a substantive conclusion. All 24 verified references remain cited.

The supplement carries the detailed RNM equations and parameterizations, numerical reconstruction and fitting settings, retrieval scoring, secondary metrics, alternative-fit and direction diagnostics, per-node results, complete condition means, and statistical tables. Main-text pointers identify these supporting details. Related-work and introductory repetition was shortened while preserving the comparative table and explanation-first narrative.

The published Scrum framework is cited and distinguished from the evaluated XML implementation. The raw-versus-fitted and worked-row figures are reproducible with `paper/generate_figures.py`; figure values are unchanged. Offline sensitivity and node-influence analyses remain in their separate directories. See `POSTHOC-ANALYSES.md` and `NODE-INFLUENCE.md` for their reproduction commands and limits. The current paper supersedes earlier longer drafts.

Both PDFs compile in Overleaf. The existing desktop source compiles, the strict source audit passes with 24 references, and all pages were visually checked. Independent scientific review found no remaining actionable issues after a caption clarification.

All 3,161 existing non-paper files are byte-identical to the preceding delivery. No new experimental model calls, RNM fits, statistical tests, or substituted results were introduced. The original answers, reference CPTs, predictions, test results, token counts, and saved sensitivity analyses are unchanged. The package remains private for author review.
