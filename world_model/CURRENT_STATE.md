# Current Market State

**Model version:** 0.2.15
**Status:** September 25 Friday review complete; no forecast resolved; four pending upstream packets canonically archived; modest hypothesis reweight; no new forecast durably registered
**Analysis cutoff:** 2026-09-25T21:16:11Z

The [Friday review](../evaluations/2026-09-25-weekly-review.md) preserves scoring, benchmark/calibration audit, source ancestry, Skeptic review, model changes and the learning assessment. [Cycle evidence](../evidence/2026-09-25-cycle.md) separates observations from inference. The dated [v0.2.15 change record](../meta/model_changes/2026-09-25-v0.2.15.md), [weight record](../meta/hypothesis_weights/2026-09-25-v0.2.15.json), and [receipt supplement](../evidence/research/INDEX-2026-09-25-supplement.md) preserve the pieces that the connected write path would not safely merge into cumulative read-modify-write files during this run.

## Evidence and interpretation

No forecast expired before evidence intake, so the probability ledger remains **22 resolved forecasts**, mean **Brier 0.212214** and mean **log loss 0.614555**. The sample remains below the precommitted 30-resolution threshold; learning is not established.

Four complete pending packets were first canonically received at 2026-09-25T21:16:11Z: Freight weekly v2, Agriculture weekly, Geopolitics weekly and Suite Energy weekly. Their staged bytes and hashes were independently verified and their exact report/envelope blobs were archived under canonical paths. They add no fresh macro observation: Freight reuses Port LA cells; Agriculture lacks required WASDE balance cells; Geopolitics lacks a verified current-window original event document; Energy acquired no new release. Repeated source ancestry earns no duplicate vote.

Post-cutoff evidence points to stronger near-term real activity than the delayed-recession branch expected: initial claims were 197K; August new-home sales were 684K with July revised up to 643K; August core capital-goods orders rose 1.6%; and Atlanta Fed GDPNow estimated Q3 real GDP growth at 5.0%. The housing revision specifically weakens the earlier inference built on the original July 607K print.

The same state is not fully benign. Final September Michigan sentiment was 48.1 while one-year inflation expectations rose to 4.6%; the official September 24 10-year Treasury par yield was 5.18%; and Brent still settled above $104 on Friday despite falling on the day. These jointly strengthen the inflation/policy-constraint branch without uniquely identifying fiscal impulse or realized future inflation.

## Hypotheses and forecasts

- H001 Soft landing: **0.36**
- H002 Late-cycle recession: **0.12**
- H003 Fiscal/inflation regime: **0.40**
- H004 Productivity boom: **0.12**

Model v0.2.15 adds no new causal edge. It formalizes a revision-awareness rule: later official data revisions may change present-state evidence weight, but frozen forecasts retain their original information cutoffs and first-release resolution rules. The July new-home-sales revision is the trigger.

P000029 remains frozen at **66%** for first-release September headline CPI >= +0.4% m/m, point +0.5%, 80% interval +0.1% to +0.9%, resolving October 14, 2026 at 08:30 ET. P000004 and P000005 remain unresolved. An attempted new probabilistic core-PCE record was rejected by the connected write path, so no P000030 is claimed or counted.

## Learning status

Recent probability vintages remain numerically better than early ones, but targets/horizons differ, dependence is substantial, S&P point skill versus matched no-change is slightly negative, and 80% interval coverage remains 90.9%, suggesting conservative intervals. **Insufficient evidence to assess learning** remains the only supported conclusion at n=22.

## Operational boundary

Canonical receipt time is actual Market receipt, not producer availability or staging time. Missing documents/tables remain gaps. Shared Port LA and EIA evidence are deduplicated by causal ancestry. No historical forecast is rewritten.

The cumulative `evidence/research/INDEX.md`, `meta/MODEL_CHANGELOG.md`, and individual hypothesis files remain unchanged because the connector rejected safe in-place read-modify-write operations. Their dated supplements above are authoritative for this cycle until a later reconciliation merges them without changing history.

No trade recommendation is produced. The next important watch is the September 30 core-PCE release; the highest-information durably registered forecast remains P000029 for October 14 headline CPI.
