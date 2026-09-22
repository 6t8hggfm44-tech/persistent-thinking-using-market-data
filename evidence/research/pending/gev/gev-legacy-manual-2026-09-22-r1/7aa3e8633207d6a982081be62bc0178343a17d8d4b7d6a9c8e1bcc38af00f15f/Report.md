# GEV manual rehearsal — archived anomaly investigation

Final bounded hypothesis-test report · gev-legacy-manual-2026-09-22-r1

The saved aircraft positions contain reproducible coordinate discontinuities. They do not establish actual unusual motion, navigation interference, attribution or transport harm. Satellite catalog-change flags likewise do not establish maneuvers. This run repairs the earlier retrospective-aircraft access gap and independently tests selected archived evidence; it is not a new week of observations.

## Scope and chronology

The requested rolling window remains **September 15, 2026 18:31:48.717047 UTC through September 22 18:31:48.717047 UTC**, fixed at the original manual start. The interrupted investigation continued under explicit authorization. The actual cloud download and byte verification of the two GEV archives completed **September 22 at 19:00:18.523672 UTC**. This later access is not backdated into the original cutoff.

The cached retrospective packet was created September 22 at 15:09:28 UTC from an index cutoff at 04:33:25 UTC. It describes complete UTC archive days September 14–20. Daily provider event times, original daily acquisition/review cutoffs, this mirror's creation and our actual read time remain separate in the private source register. The second screening packet was created September 21 at 19:40:06 UTC for September 14 19:37:40 through September 21 19:37:40 UTC. Both existed before the original manual start; neither covers the full requested rolling week.

No collector, provider request, full-day history replay or global reranking was invoked. The permitted pilot regions are Baltic/Nordic, eastern Mediterranean and Gulf, with selected satellite catalog groups. Broader global discovery and independent operational evidence were unavailable within the archive-only scope.

## Coverage and checks

| Input | Actually verified | Remaining limit |
| --- | --- | --- |
| Retrospective aircraft | All 90 retained cases reproduced from original trace bytes across September 14, 16–20; 75 cases within the requested window, 25 per pilot region | September 15 missing from the packet's exact daily index; September 21 and current partial September 22 absent from this weekly packet; 15 September 14 cases excluded |
| Live-capture aircraft export | 19,510 current rows plus capped 250,000-row baseline; full saved screening replay passed | Sparse September 14–16 observations; no later aircraft rows in that export; the baseline is partial |
| Satellite export | 1,012 catalog records plus 218 baseline records; all 264 element-change comparisons independently recomputed | Limited catalog groups and historical depth; fitted estimates, not independent physical positions |
| Exact replay | All 288 saved screening candidate records and 90 cached retained cases reproduced | Reproduction verifies those inputs/calculations, not omitted cases, original global ranks or whole-week coverage |

The September 15 retrospective gap does not mean no other September 15 evidence exists: the separate live format contains sparse snapshots. Those snapshots cannot replace a missing dense daily history. Later index metadata is not treated as readable September 21 bytes. Saved daily selections are bounded convenience samples; missing days and unknown exposure cannot become a prevalence denominator or a finding of normality. Historical raw observations and source replicas can overlap and are related evidence.

## Ranked leads and selected case

1. **September 17 Baltic/Nordic, air-c8cc24a3cd15c4fe3fe8.** The strongest reproducible measurement-level case: four all-MLAT positions over 27.91 seconds contain three flagged pairs, a maximum 39.300 km displacement and 4,752.074 m/s coordinate-implied speed. Attached groundspeeds are about 226–227 m/s. The same-source result makes a source-switch-only account insufficient, but the attached fields have unknown ages and are not independent sensors. This is a data-reliability lead relevant to transport monitoring, not evidence of actual supersonic movement.
2. **September 16 Gulf, air-d5157b70ec2cd33ad3b8.** Four positions over 17.91 seconds produce three flagged pairs, all involving ADS-B/MLAT method transitions. The maximum displacement is 138.808 km and implied speed 67,711.049 m/s. Requiring the same known position method removes all three pairs. This supplies a mechanism-sensitive comparison, not a matched healthy control.
3. **September 19 eastern Mediterranean, air-ffa56521da8c5eb4415e.** Three MLAT positions span 24.32 seconds; maximum displacement is 9.502 km and speed 735.195 m/s. The case disappears at an 800 m/s threshold. It illustrates sensitivity of a retained lead to an uncalibrated threshold; attached speeds and actual ages are unavailable.
4. **Satellite catalog drift and residual tail.** In the requested window, 244 element-change flags span 81 catalog identifiers: 243 exceed only the node-longitude (RAAN) threshold; one also exceeds mean-motion change. Ordinary drift, epoch separation, catalog fitting and angular conditioning are viable explanations. These flags guide catalog-quality review; they do not establish a military or commercial incident.

Selection was exploratory and recorded before the independent arithmetic. Prior saved detector results were visible when choosing leads. No fresh event-time physical observations were collected.

## Executed discriminating tests

Independent spherical geometry recalculated **92 flagged aircraft pairs across 75 in-window retained cases**. Of these, 50 pairs have the same known source method and 42 cross methods; **46 cases retain at least one same-source pair** at the default 600 m/s and 5 km thresholds. All actual numeric position ages are unknown. A serializer's clear stale flag is not an age of zero: requiring numeric freshness leaves zero eligible pairs, so this control is blocked rather than a clean negative.

At 800 m/s and 5 km, 67 pairs in 52 cases remain, including 25 same-source pairs in 23 cases. At a 10 km minimum, 54 pairs in 39 cases remain, including 15 same-source pairs in 13 cases across the tested 400–800 m/s thresholds. Changing maximum pair gap from 120 to 60 seconds changes none of these retained results. These are sensitivity counts within already selected cases, not discovery rates in the population. All retained cases are short coordinate jumps; a persistence test is not applicable to this retained set and says nothing about omitted population behavior.

Satellite differences were independently recomputed with shortest wrapped RAAN differences and exact catalog epochs. An additional exploratory baseline test, planned before execution, required at least three earlier same-object/source epoch increments, available before the current catalog retrieval, excluding conflicting epochs and gaps above seven days. Only **93 of 244** in-window flags qualify; 151 lack sufficient history. Among the 92 eligible RAAN-only flags, the median absolute residual from prior median drift is **0.000762 degrees/day**, while the maximum is **624.304 degrees/day**. The large tail is retained explicitly; a small median does not resolve all cases. Thirty-eight in-window flags have absolute inclination below 5 degrees, where node-angle comparisons warrant special caution. No calibrated residual threshold, orbital propagation, covariance model or independent tracking was supplied.

## Hypotheses, implications and limitations

Measurement/processing explanations remain consistent with the evidence. Source transitions explain the loss of some flags under source filtering, while the selected all-MLAT case demonstrates that switching alone cannot explain all retained geometry. A real-motion hypothesis is unconfirmed because independent positions, receiver/solver health, raw-radio decoding and usable field ages are missing. External navigation disruption and physical satellite maneuvers remain untested. Catalog drift compatibility does not prove an absence of maneuvers.

No operational outage, cargo flow, facility impact, price response or military attribution is established. There is no supported trading signal. The decisive next evidence would be independent event-time positions and receiver/solver chronology for the selected aircraft, and identity-resolved propagated orbital residuals with uncertainty and independent tracking for satellites. Another copy of the same provider is not independent corroboration.

The earlier September 21 version-2 GEV report tested the same live/satellite export but could not read the retrospective daily-review bytes. This run successfully reads and reproduces the cached retrospective subset and adds the stated sensitivity and historical-rate tests. Repeated satellite-export results share the same ancestry, not fresh corroboration. Prior reports and consumed scheduled occurrences remain intact.

The numerical GEV tests finished before current Weather/Energy findings were read. During envelope preparation, Weather's frozen claims were read; the Energy worker then delivered its frozen findings before this narrative was frozen. **The narrative was therefore not blinded.** The unchanged pre-exposure test-output hashes and exposure order are retained privately. No Weather or Energy values enter GEV's tests or provide corroboration. Exact read/message arrival times were not separately instrumented; the exposure is bounded between 19:06:22.935982 and 19:07:26.484478 UTC.

## Completion and reproduction

P01–P07 completed the bounded scope, source audit, selection, plans, preserved inputs and numerical analysis with the stated gaps. P08 GEV map publication was blocked by unavailable authorized writer/rendered application. P09–P11 completed competing hypotheses, feasible tests, arithmetic checks and limitations; independent physical/operational tests remain blocked. P12 preserves this final report and private reproducibility package; recipient transport and acknowledgment are tracked separately.

The scientific workflow and executed detector are satellite-research commit e9105bf38cdca6e78955f03844a2c894c9abd793; cached verifier code is pinned separately. Private artifacts include plans, source identities, archive verification, numerical inputs, scripts and test results. The small included reproduction inputs reproduce the central arithmetic; complete original detector replay still requires the exact preserved private source archives. Temporary artifact transport can expire, and hashes alone cannot restore bytes.

The cache's historical accounting snapshot recorded 2,644,952,439 bytes used including reservations out of a 107,374,182,400-byte shared ceiling (about 2.46%); 104,729,229,961 bytes remained. This is an export-time accounting record, not a current billing meter or a fresh full-store measurement. No quota was reset or increased. The report is eligible for Market's next normal intake after verified transport; completion here is not evidence of scheduled execution or recipient acknowledgment.
