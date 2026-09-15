# GEV weekly hypothesis test results — September 14, 2026

Run **gev-weekly-2026-09-14**, version **1**. Final hypothesis-test report; results are retrospective and exploratory. Requested event window: **September 7, 15:02:14.818119 UTC through September 14, 15:02:14.818119 UTC** (168 hours). The investigation began on time; completion occurred later. Report generation and market receipt times are recorded separately in the envelopes. Workflow and screening code: satellite-research commit **e9105bf38cdca6e78955f03844a2c894c9abd793**, verified against main at run start. Executed module hashes are retained in the screening package.

**The 50 screening flags do not establish 50 physical anomalies.** Twenty orbital flags closely match ordinary secular precession. Two additional orbital flags have large changes in a poorly conditioned angle near the equator, but small geometric plane-normal differences whose physical cause remains unresolved. Aircraft discontinuities are reproducible in processed records, yet none meets the stricter known-freshness eligibility rule. No military attribution, economic loss or trading signal is established.

## Ranked leads and selection

Rank reflects evidence quality and feasible investigation, not threat probability.

| Rank | Lead and evidence class | Finding and why it matters |
|---|---|---|
| 1 | Orbital catalog changes — observed through GEV | 22 provisional flags. Selected because frozen paired elements support discriminating tests of ordinary precession, angle conditioning and duplicate solutions. Useful for reducing false space-activity alerts; does not establish unusual operations. |
| 2 | Aircraft coordinate discontinuities — observed through GEV | 23 events across 12 identifiers. Processed positions contain jumps; unknown field freshness and provider effects prevent a verified navigation or trajectory conclusion. Relevant to the reliability of transport monitoring. |
| 3 | Hawaii SARSAT ground-service outage — operator report | NOAA reports loss of Hawaii MEO/LEO ground-terminal communication on September 8 and subsequent restoration. This concerns distress-alert resilience, not anomalous satellite motion. No rescue delay or transport loss is verified. |
| 4 | Taipei FIR routing restrictions — published operational context | Scheduled restrictions intersect five dates in the requested window. A feasible future test would compare actual route distance and delay against matched unaffected flights. A published restriction is not observed disruption. |
| 5 | Sentinel-6A product interruption — republished operator report | EUMETSAT ground-segment alerts describe data interruption. Closure of the selected alerts was not verified; no persistent spacecraft failure is established. Relevant to availability of ocean-monitoring inputs. |

For Hawaii, NOAA's reported endpoints, 07:40–10:56 UTC, imply **196 minutes**; the same update gives **206 minutes**, a ten-minute inconsistency. The update attributes the interruption to a brief power outage during Hurricane Lowell and says GEOSAR remained nominal. That is operator attribution, not an independently tested weather mechanism. [Opening notice](https://ospo.noaa.gov/data/messages/2026/09/MSG_20260908_1027.html), [restoration update](https://ospo.noaa.gov/data/messages/2026/09/MSG_20260908_1211.html).

Taiwan CAA supplement 15/26 lists July–September scheduled restrictions. September 8–11 and 14 intersect this week; the published closure interval is 02:00–03:00 UTC and affected routing starts at 01:20 UTC. Actual NOTAM activation, flight diversion, delay and cost were not measured. [CAA supplement](https://ais.caa.gov.tw/eaip/AIRAC%20AIP%20AMDT%2002-26_2026_05_14/eSUP/15-26_2026_07_01/SUP-en-GB.html).

For Sentinel-6A, embedded alerts 13831 and 13829 place onset on September 7 at 19:55 and 20:33 UTC. Alert 13829 was still described as ongoing in the September 8 update. NOAA wrapper dates conflict with some embedded advisory dates. A separate closure for alert 13819 does not close these later alerts. NOAA republishes EUMETSAT, so the two names are not independent confirmation. [HR alert](https://www.ospo.noaa.gov/data/messages/2026/09/MSG_20260907_0050.html), [LR alert](https://ospo.noaa.gov/data/messages/2026/09/MSG_20260907_0045.html), [update](https://www.ospo.noaa.gov/data/messages/2026/09/MSG_20260908_0634.html).

## What the data actually covers

Global discovery extended beyond the collection pilot. Measured collection remains bounded: Baltic/Nordic, eastern Mediterranean and Gulf aircraft snapshots; a rotating aircraft trace cohort; and selected stations, weather and GPS operational satellite catalogs. It is not global continuous surveillance.

The frozen screen contains **229,959 aircraft records** (3,056 identifiers), **217 satellite element records** (124 identifiers) and **306 acquisition requests**. All requests were retrieved on September 14, between 04:53:04 and 14:59:39 UTC. Some retrospective aircraft traces describe earlier events. Element epochs are reference times for fitted orbits, not dates of direct satellite observations.

| UTC date portion inside the requested window | Requests captured | Aircraft event records |
|---|---:|---:|
| September 7, after 15:02:14 | 0 | 0 |
| September 8 | 0 | 0 |
| September 9 | 0 | 0 |
| September 10 | 0 | 0 |
| September 11 | 0 | 0 |
| September 12 | 0 | 60, from one aircraft |
| September 13 | 0 | 120,913, from 64 aircraft |
| September 14, before 15:02:14 | 306 | 108,986 |

These eight UTC date portions total exactly seven elapsed days. There are no regional snapshots before September 14; that day has 70 per pilot region. Five-minute snapshot cadence cannot establish the two-minute continuity required for jump tests. Dense traces support selected comparisons, not uninterrupted regional coverage. No available evidence establishes normal conditions during missing intervals.

No input set reached the 250,000-record cap. The fixed 30-day pre-window baseline ends at the requested window's start and contains **zero records and zero days**: rarity, seasonality and historical false-positive rates are untested. The screen produced **23 aircraft jumps, 22 orbital-element changes and five stale-catalog flags**. The stale entries exceed a provisional 72-hour epoch-age screen (approximately 73.6–657.3 hours); that does not establish spacecraft failure.

Live connector probes after run start returned five aircraft records from a feed reporting 13,398 total and five station records from 20 total. The aircraft snapshot was about 249 seconds old. These were capability probes, not fully paginated global samples or additional weekly observations. Shell runtime discovery failed while the read-only connector succeeded; a current browser address was not established through that shell route.

## Hypotheses and executed tests

The plan was saved at **September 14, 15:06:09.879339 UTC**, after inspecting screening candidates but before follow-up orbital calculations. All 22 orbital-change events were included. This is a mixed exploratory design, not a held-out validation. The one-degree low-inclination boundary and 0.01°, 0.05°, 0.1° residual screens are diagnostic choices, not calibrated maneuver thresholds.

| Hypothesis | Discriminating test and result | Verdict |
|---|---|---|
| H1: ordinary orbital precession explains the non-equatorial RAAN flags | Compare wrapped changes with first-order J2 drift over each pair's epoch gap. All 20 non-equatorial events have absolute residuals below 0.01°; the largest using prior elements is **0.00837831°**. Prior, next, averaged-element and averaged-rate variants all remain below each tested screen. | **Supported within the approximate diagnostic.** Does not prove an absence of maneuvers. |
| H2: near-equatorial angle conditioning exaggerates apparent change | GOES-18's RAAN changes **−3.7934°**, but its geometric plane-normal separation is **0.01319419°**. GOES-19 changes **−22.8734°**, but the corresponding separation is **0.01786260°**. J2-adjusted geometric residuals remain about 0.01319375° and 0.01786079°. | **Supported for angle exaggeration.** The remaining difference's physical cause is **inconclusive**. |
| H3: identifier counts overstate independent orbital evidence | Compare exact paired epoch and geometric-element signatures. **22 identifiers reduce to 13 distinct paired signatures**, including groups of five CSS-associated and six ISS-associated labels. | **Supported for repeated catalog solutions.** Does not prove docking or shared physical identity. |
| H4: these flags establish unusual maneuvers or operational disruption | Seek epoch-matched independent tracking, covariance and operator confirmation. None was obtained. Raw geometry alone is insufficient. | **Inconclusive**; the physical attribution test is blocked. |

The diagnostic uses WGS-72 constants: μ = 398600.8 km³/s², Earth radius 6378.135 km and J2 = 0.001082616. Mean motion gives approximate semimajor axis; the secular nodal rate is −1.5 J2 n (R/p)² cos(i), with p = a(1−e²). A separately written vector calculation reproduced the central results within **7.82 × 10⁻¹⁴ degrees** and independently recovered 13 signatures. This is implementation verification using the same measurements, not independent sensing. [NASA orbital-precession and plane-angle reference](https://science.nasa.gov/wp-content/uploads/2023/05/GDC_OrbitPrimer.pdf), [CelesTrak SGP4 constants/reference](https://www.celestrak.org/software/tutorials/sgp4.php).

This calculation is **not SGP4 propagation or precision orbit determination**. It treats catalog mean motion approximately as Keplerian, omits un-Kozai recovery and several perturbations, and does not transform epoch-dependent TEME orientations into a common precision frame. The reported plane angles are geometric diagnostics of catalog elements, not measured physical maneuvers. No covariance or validated uncertainty model is available.

A bounded official-source search found a GOES-18 calibration notice for September 14, 15:00–15:10 UTC, with its scan at 15:03–15:05, after the event cutoff. It neither confirms a maneuver nor explains the preceding element pairs. Search incompleteness cannot establish an absence of operations. [NOAA calibration notice](https://ospo.noaa.gov/data/messages/2026/09/MSG_20260908_1453.html).

Aircraft audit T5 reproduced the 23 event maxima using separate vector geometry and checked the two strongest selected pairs against hashed original processed trace responses. There are **31 triggering pairs**: 12 events involve position-method transitions and one involves a publisher transition. Ten events remain entirely same-labeled-source before applying freshness requirements, weakening a source-switch-only explanation. **All 23 events have unknown position and field age; zero events qualify under the known-fresh, same-source rule.** An empty eligible sample is inconclusive, not evidence that navigation was healthy. No original radio measurements, independent position truth or GNSS-cause test was available.

## Confidence, limitations and practical implications

Confidence is high in reproducibility of the saved arithmetic and packet integrity; moderate in the approximate ordinary-precession explanation; low in any physical or operational attribution. Shared upstream catalogs and processed aircraft feeds limit independence. The conclusion corrects a tempting initial reading: raw RAAN changes and numerous object labels are not evidence of numerous unusual spacecraft actions.

The actionable research result is improved alert interpretation. Retain the two near-equatorial cases for better orbital evidence and the aircraft cases for fresh-position controls. The Hawaii report is the clearest external service-resilience lead, with a resolved outage and an unresolved duration discrepancy. None of these results establishes a price, supply, inflation, margin or military effect. Linking them to those outcomes requires independently documented operational exposure and an appropriate comparison.

This is the first completed weekly collection round. The earlier Finland GNSS investigation remains a separate historical case; no material new Finland-specific causal result is established here. Weather and energy reports for this occurrence were not complete at finalization. No cross-domain causal reconciliation was performed, and later reports must not be treated as evidence available at this report's earlier event cutoff.

Next decisive evidence is: precise epoch-aligned states and covariance with operator/tracking corroboration for the two GOES cases; known-fresh positions and matched unaffected aircraft for navigation hypotheses; actual route/throughput or service logs for operational effects; and a mature historical baseline. These are requirements for future tests, not requests to expand collection automatically.

## Reproducibility and operational status

The saved detector replay passed and reproduced all 50 candidates. The coverage audit verified all **36 screening manifest entries and 20 exported original response bodies**. Full normalized detector inputs are included, but **146 additional distinct original bodies remain outside this frozen package** in the local collector archive; normalization of every input cannot be independently reproduced from this package alone. Web evidence includes source-linked indexed/extracted text where direct pages failed; it is not claimed as raw HTTP byte capture.

At screening freeze, the collector held 166 compressed response blobs totaling **29,863,354 bytes**, representing 120,522,268 uncompressed body bytes. The configured raw-data limit is 10 GiB and minimum disk reserve 1 GiB; a later operational check found approximately 17.4 GB free. This does not budget all future database growth. The service was running with a completed recent cycle, but an earlier autostart diagnostic still reports **“No module named satresearch.”** Automatic restart reliability remains unresolved; an interrupted collector may need attention. No collector, launcher, cadence or thresholds were changed.

Analyst review decisions were saved: **20 explained at the mean-element diagnostic level; 30 need more data**. These labels do not establish physical causes. A source-only GEV case is prepared separately where supported; no terrestrial position or ground track is asserted, and publication/display verification is unavailable in this round.

The local evidence package contains the source register, shortlist, case record, hypothesis plan, actual test results, coverage audit, independent calculation, review decisions and screening replay. The final manifest verifies the included files. Raw records and private machine configuration remain local. Market Model Cycle receives the complete final report and shareable envelope; its acknowledgment and durable persistence are tracked separately. Canonical intake preserves uncertainty and actual receipt time and does not alter earlier frozen forecasts or model weights.
