# Current Market State

**Model version:** 0.2.17 (reviewed, unchanged)
**Latest fully persisted, independently validated scientific review cutoff:** 2026-09-30T19:56:01Z
**Run:** market-repair-test-2026-09-30-1
**Status:** The 15-producer repair test remains fully persisted and independently validated; the later post-close cycle is branch-only and awaiting incorporation into main

**OBSERVATION — persistence correction, 2026-10-01:** The last fully persisted validated state is Market commit `4ff6dbaf2be94132fa8d8579ec066c7a24da0359`, with scientific primary commit `62e5701680993f13a7c60b5e5f3d88e2d3479ba0` and cutoff `2026-09-30T19:56:01Z`; see the [repair analysis](../evaluations/2026-09-30-repair-test-1.md) and [validation receipt](../evaluations/2026-09-30-repair-test-1-validation-receipt.json). The later run `2026-09-30-post-close-regular-cycle`, with cutoff `2026-09-30T21:44:21Z`, is preserved on branch `market-cycle-2026-09-30-post-close` at commit `924ddcf5c286588f472fea336e36e04ce485554f`. Its full promotion was blocked; see the [persistence note](../evidence/2026-09-30-post-close-cycle.md). The corresponding evaluation and canonical Trade intake record remain absent from main. This corrects the prior status claim without promoting branch artifacts, changing historical cutoffs or receipt times, or altering forecasts or the model.

Weights remain **H001 0.36 / H002 0.14 / H003 0.38 / H004 0.12**. H003 remains the narrow leader. The branch-only post-close review reports no further reweight.

P000030 was already resolved before the later branch-only cycle: first-release August core PCE +0.2% versus frozen >=0.3%; Brier 0.3844 / log loss 0.967584. The branch-only review reports that no additional forecast expired after the prior 19:56:01Z cutoff. The validated ledger therefore remains **27 resolved records / 23 probability forecasts**, mean Brier **0.219700** and mean log loss **0.629904**. **INSUFFICIENT EVIDENCE TO ASSESS LEARNING** remains mandatory below n=30.

The regular Trade packet was first fully read by Market at `2026-09-30T20:03:49Z`, after the validated repair-test cutoff. That actual receipt time is preserved. Its canonical intake artifacts remain branch-only and are not incorporated into main. The branch record reports that exact report/envelope hashes and byte lengths match the staged packet. Its Port of Los Angeles August values are the same observations already known from prior Trade/Freight reports; stale European material and missing Asian/global quantity coverage add no independent macro vote.

The branch-only review considered final September 30 U.S. market closes and the decline in market-implied October hike odds only as downstream state variables. They do not independently identify the causal regime.

Active unresolved IDs remain **P000004, P000005, P000029, P000031**. No new forecast is added because P000031 and P000029 already provide the highest-information near-term discrimination.

**Highest-information watch:** October 2 first-release September Employment Situation / P000031.
