# Model Changelog

## 0.1.0 — Baseline
- Created repository architecture.
- Established four neutral competing macro-market hypotheses.
- No live market evidence had yet been ingested.
- No forecasts had yet been issued.

## 0.2.0 — First live baseline (2026-08-08)
- Initialized state using an evidence cutoff of 2026-08-08 10:30 ET.
- Set hypothesis weights: H001 0.30, H002 0.32, H003 0.27, H004 0.11.
- Explicitly flagged stale high-yield spread input.
- Created nine precommitted forecasts across SPX, rates, oil, credit, and sector leadership.
- Added independent Skeptic report.

## 0.2.1 — First scored update (2026-08-10)
- Resolved P000001 before ingesting new evidence. Outcome: SPX 7,753.11; Brier 0.2401; log loss 0.673345; point MAE 3.11; 80% interval hit; no-change MAE 4.53. This single forecast did not justify a model revision.
- Ingested only evidence available after the Aug. 8 cutoff: the Aug. 10 oil shock, higher long yields/issuance pressure, near-record equity resilience, and strong aggregate earnings.
- Ran the Skeptic against H002 before updating weights.
- Changed hypothesis weights to H001 0.31, H002 0.28, H003 0.30, H004 0.11.
- Reduced H002 because its expected credit/earnings confirmation is absent so far; increased H003 because the commodity/inflation/term-premium channel remained active despite weak labor; modestly increased H001 because earnings/risk assets remain resilient.
- Refined the causal graph to make explicit that weak labor can lower the expected policy path while commodity shocks and Treasury-supply/term-premium pressure simultaneously keep long yields elevated.
- No causal credit is assigned to P000001 for these changes; the revision is linked to post-cutoff evidence rather than the forecast outcome.
