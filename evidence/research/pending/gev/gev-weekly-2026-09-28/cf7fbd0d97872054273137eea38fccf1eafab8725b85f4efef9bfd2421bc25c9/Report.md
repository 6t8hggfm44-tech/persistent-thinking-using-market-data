# GEV weekly investigation — September 28, 2026

## Summary

**OBSERVATION:** Retained aircraft position-data discontinuities and satellite catalog flags reproduce. **INFERENCE:** This investigation does not establish an aircraft maneuver, navigation interference, a satellite maneuver, military attribution or economic loss. Physical and operational hypotheses remain inconclusive; missing controls are not evidence of normal conditions.

This is the final bounded investigation for `gev-weekly-2026-09-28`, completed by an explicitly authorized later continuation. The original event window remains September 21, 2026 at 15:03:12.081641 UTC through September 28 at 15:03:12.081641 UTC. Both usable export mirrors were created after that morning endpoint. The findings below are a **later-read retrospective supplement**, not information verified or available to this worker at the morning start. The interrupted morning investigation had not produced a verified final report. No earlier market forecast may be credited with these findings.

## Coverage

The aircraft packet contains six daily bounded selections, September 21–26: 15 candidates each, 90 total. All 90 reproduced from the unchanged included trace bytes. Filtering to the original rolling event window excludes five earlier September 21 cases and retains **85 candidates involving 78 aircraft identifiers**: 27 Baltic/Nordic, 29 Eastern Mediterranean and 29 Gulf. Daily retained counts are 10, 15, 15, 15, 15 and 15 respectively. These are selected data-pattern counts, not 85 independent physical incidents or a representative traffic rate.

September 27 is missing from the verified exact source index; the current partial September 28 is not in the complete-day aircraft packet. Each daily review selected at most five candidates per region. There were no additional weekly omissions among those daily selections, but omitted daily candidates and complete-day ranking were not reconstructed. Saved counters total 13,204,539 retained regional rows and 23,660 aircraft-region groups; these counters were not reproduced from complete daily archives and the groups are not unique weekly aircraft. Geographic scope is a three-region pilot, not global surveillance.

The satellite screening export contains 328 current satellite observations and 1,332 baseline satellite records. Its screening window is September 21 at 20:38:30.955325 UTC through September 28 at 20:38:30.955325 UTC, different from the original window. All 81 candidate event times fall within the original window; this does not restore its missing earlier interval or rerun the original-window baseline. Exact saved-input replay reproduced **78 element-discontinuity, two catalog-stale and one catalog-conflict candidates**. All 78 discontinuities exceeded only the RAAN change threshold, not the inclination or mean-motion threshold. They are related catalog-derived flags, not independent spacecraft events. Current aircraft observations in that export are zero; its 250,000-record historical aircraft baseline is capped and cannot establish complete coverage.

The verified collector accounting snapshot reports 4,958,159,785 bytes against a 107,374,182,400-byte ceiling (4.62%). The total equals 223,343,788 stored archive bytes plus 4,734,815,997 reserved history bytes. This is a dated storage/control snapshot, not current API spending or a complete live health check. Its CelesTrak human-review block remains unresolved; no provider collection or control reset was performed. Successful archive transport does not resolve that separate provider issue.

## Shortlist and selected case

Ranking is exploratory: descending retained candidate duration, then event ID. It measures investigation value within the retained sample, not calibrated likelihood or global severity.

| Lead | Region/date | Retained span | Review rationale |
| --- | --- | ---: | --- |
| air-e6d00d319f405d043dda | Baltic/Nordic, September 22 | 30.78 seconds | Four positions, three qualifying pairs, no position-source switch; selected for internal consistency checks. |
| air-7eb6724f1389f838848d | Gulf, September 23 | 30.36 seconds | Multiple discontinuities, but a source switch weakens interpretation. |
| air-ff3ab90419318a7210d8 | Eastern Mediterranean, September 22 | 26.46 seconds | Multiple pairs without a source switch; short duration and unknown ages remain. |

All three are observed data candidates. Potential relevance is the reliability of positioning information used in transport and situational awareness; no operational impact is measured. None establishes military activity. Precise physical locations and trajectories are not independently verified.

## Hypotheses and tests

The continuation plan recorded competing hypotheses before opening the new artifacts. Candidate ranking and numerical sensitivity choices were exploratory after data inspection; they are not held-out confirmation tests.

**H1 — reproducible position-data discontinuities. Supported at the measurement-product level.** Exact artifact size/hash checks, safe inventories and the pinned retained-case verifier passed. Both source-index and collector-state SHA-256 values also match exact immutable repository bytes. These checks bind stored products, not original radio observations or publisher truth. Satellite saved-input replay reproduced all 81 flags.

**H2 — measurement, processing, source transition or asynchronous-field effects. Plausible and unresolved.** Of the 85 in-window aircraft candidates, 36 contain a position-source switch and all 85 have unknown position-field age. A strict known-age-only filter leaves zero cases, not a healthy control population. The selected case remains entirely MLAT, so an explicit source-label switch alone cannot explain its three pairs; MLAT estimation, processing and asynchronous fields remain alternatives. Ordinary satellite element refitting and RAAN evolution remain alternatives to a maneuver.

For selected case `air-e6d00d319f405d043dda`, four retained positions span 30.78 seconds. Independent haversine arithmetic, using radius 6,371,008.8 metres, yields:

| Adjacent interval | Reported-coordinate separation | Implied speed |
| ---: | ---: | ---: |
| 8.93 seconds | 8,004.70 metres | 896.38 metres/second |
| 14.32 seconds | 30,529.92 metres | 2,131.98 metres/second |
| 7.53 seconds | 7,779.20 metres | 1,033.09 metres/second |

Attached reported speed is about 244 metres/second, but its age is unknown. Coordinate-derived and reported-field disagreement is an internal inconsistency, not independent sensing. The pinned engine maximum is 2,131.9744 metres/second; the approximately 0.003 metres/second difference reflects Earth-radius/epoch-arithmetic choices. With the minimum separation fixed at five kilometres, speed thresholds of 600, 800, 1,000 and 2,000 metres/second retain three, three, two and one pairs. Sensitivity preserves a numerical discontinuity; it cannot establish true movement. Thirty seconds does not establish a sustained regional outage.

**H3 — physical disruption, navigation interference, unusual operations or economic transmission. Inconclusive; decisive tests blocked.** No independent event-time receiver/RF/onboard records, matched unaffected controls or operator disruption records were available. Satellite epoch-aligned propagation, covariance and independent ephemeris tests were not performed. There are no verified reroutes, delays, cargo losses, freight-price changes or affected economic denominators in this evidence. Attribution and intent are not tested. No forecast, weight or trading recommendation follows.

## Workflow and audit

P01 scope/window and completion criteria are retained. P02 is a partial offline capability/provenance audit, with no live GEV feed query. P03 is bounded aircraft/satellite discovery with the shortlist above; global contextual discovery remains incomplete. P04 preserves the original window and continuation plan, with exploratory selection disclosed. P05 verifies the two existing exports and retained histories; complete daily archives remain outside the materialized subset. P06 completes the feasible date/source/age/coverage audit. P07 executes numerical checks and sensitivity, with matched comparisons blocked. P08 mapping is blocked because an authorized live GEV writer is unavailable. P09 records hypotheses, confounders and falsifiers. P10 completes feasible deterministic/internal tests while causal tests stay blocked. P11 independently recalculates counts and geometry and limits the verdict accordingly. P12 produces this report and its immutable reproducibility package; Market transport and acknowledgment are separate mutable records.

Prior GEV report descriptions and workflow metadata were exposed before this continuation; no claim of blinded historical comparison is made. No quantitative week-over-week trend is asserted because sample and availability support differ. No current weather, energy or Market findings were used to select this independent conclusion. Cross-domain synthesis must align actual versions, event support and availability and deduplicate shared upstream products.

## Limitations

Confidence is high in reproduction of the included product-level numbers, limited in coverage, and insufficient for physical or economic conclusions. The position schema interpretation is not provider-version pinned. Unknown ages, nonrandom daily selection, regional sampling, incomplete baseline and day-boundary gaps prevent calibrated incidence rates. Repeated traces, catalog records and independent calculations on the same product do not supply independent sensors. Hash-only references do not supply omitted raw bodies. The live export is a screening subset rather than the full historical database.

## Sources

- adsb.lol retained historical aircraft products, through the existing private daily-review archive; [provider](https://www.adsb.lol/). Weekly mirror created September 28 at 20:13:07.835863 UTC. Raw selected traces were available and replayed; complete source-day packages were not reloaded.
- CelesTrak selected catalog products in the existing GEV screening export; [provider](https://celestrak.org/). Export mirror created September 28 at 20:40:51.369244 UTC. Catalog ancestry is shared; the mirror does not prove current provider accessibility.
- [Pinned scientific method](https://github.com/6t8hggfm44-tech/satellite-research/tree/e9105bf38cdca6e78955f03844a2c894c9abd793), also the executed scientific engine version. Private artifact, source-index, collector-state, code hashes and limited calculations are retained in the private package. Public source links identify publishers; they are not substitutes for the original retained bytes.

## Next decisive evidence

For the selected aircraft case: matched event-time independent tracking with documented position/field ages and unaffected receiver controls, then operator records to test actual disruption. For satellite leads: epoch-aligned propagated residuals with covariance and independent orbital information before interpreting element changes physically. Complete-day and missing-day material would improve coverage but cannot substitute for independence. These are evidence requirements, not instructions to bypass source restrictions or start another collector.
