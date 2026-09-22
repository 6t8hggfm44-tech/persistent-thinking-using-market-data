# GEV September 21 — retrospective evidence addendum

Final bounded hypothesis-test addendum · Version 2 · `gev-weekly-2026-09-21-v2`

## Finding

The saved observation export is now readable, and its frozen detector replay reproduces **all 288 candidate records**. This repairs part of the September 21 report's observation-access gap. It does **not** establish 288 real-world anomalies, complete weekly coverage, a navigation disruption, a satellite maneuver or an economic effect.

Two aircraft flags are reproducible coordinate discontinuities in **one processed MLAT trace**. Independent arithmetic and checks against the preserved source rows confirm the numbers; unknown measurement ages, repeated attached motion fields and absent independent positions prevent a physical interpretation. Most satellite flags are changes in catalog node longitude between different epochs, not epoch-aligned orbital residuals. Large node-longitude differences in near-equatorial records correspond to much smaller changes in catalog plane orientation.

No physical cause, attribution, military intent, transport disruption or trading signal is established. The absence of such a conclusion is **not** a finding that conditions were normal.

## Scope, chronology and what changed

This is the expressly requested offline follow-up, not a new scheduled occurrence, a catch-up batch or a replacement of historical knowledge. The [original evidence-gap report](https://github.com/6t8hggfm44-tech/-Energy/blob/af136cecd7f71475725c17473acca379c0561299/cloud/legacy-weekly/reports/gev/gev-weekly-2026-09-21/fcee736d287b2aeee83e9baa41f7c94026a8887db6c5649b0c9eef327a389b2d/Report.md) remains intact and accurate about the bytes available to that investigation. Its completed occurrence, prior delivery and earlier pending approvals are unchanged.

The original requested interval was **September 14, 2026 15:08:32.346251 UTC through September 21 15:08:32.346251 UTC**. The later export instead screened September 14 **19:37:40.270000 UTC** through September 21 **19:37:40.270000 UTC**. Its window shifts both endpoints by **4 hours, 29 minutes, 7.924 seconds**. It therefore cannot fill the original interval's leading gap. The tested candidate records fall before the original cutoff; their presence in a later-accessed packet is not evidence that this analyst knew them at the original report time.

The export was created September 21 at **19:40:06 UTC**, after the original report. This addendum's calculations were executed September 22 UTC. Source capture times are separate: the selected aircraft trace was received September 15 at 01:28:49 UTC, while the latest included satellite capture was September 20 at 23:16:38 UTC. The successful cloud download and offline calculations required no running Mac. They do not isolate the cause of the earlier HTTP 403 or guarantee future artifact access.

## Actual coverage and integrity

| Input | Verified coverage | Limit |
| --- | --- | --- |
| Aircraft current inputs | 19,510 records; 1,415 identifiers; September 14: 13,557 rows, September 15: 5,931, September 16: 22 | Last position September 16 at 02:59 UTC; **no aircraft rows September 17–21 in this export** |
| Aircraft baseline | 250,000 records from September 12–14; 1,958 identifiers | Deterministic input cap reached; only three days, not a full 30-day baseline |
| Satellite current inputs | 1,012 catalog records; 128 identifiers; capture dates September 15–20 | Selected `stations`, `weather`, `gps-ops` groups; fitted elements, not direct physical positions |
| Satellite baseline | 218 records | Limited historical catalog context, not a calibrated maneuver baseline |
| Snapshot opportunities | 52 saved fresh snapshot responses against 6,045 nominal collection slots in the shifted export window | This is a collection-slot denominator, **not aircraft visibility, regional prevalence or healthy-airspace coverage** |

Discovery is constrained to the supplied export: Baltic/Nordic, eastern Mediterranean and Gulf samples, selected traces extending outside those regions, and the named catalog groups. No global search or fresh provider query was performed. Separate complete daily-history/review-cache receipts for September 14 and 16–20 exist in storage metadata, but those retrospective aircraft datasets are **not included** in this packet and were not analyzed here. Missing export rows do not mean the durable daily archives are absent. September 15 remains absent from that daily-history index.

Baseline event/epoch times precede the original window, but some historical records were retrieved later. They are retrospective baselines, not information necessarily available at the window's beginning or untouched held-out controls. No historical control is backdated; the selected aircraft has no matched prior baseline in this export anyway.

Integrity checks verified the outer ZIP, inner ZIP, all **53 inventoried files** plus the manifest, safe extraction, and exact pinned aircraft/satellite code. The package contains **35 cited source bodies**, not the full SQLite/raw archive. The referenced collector-state bytes and its reformatted included copy match semantically. Historical seed and SQLite counts remain upstream provenance claims in this packet; this run did not reopen the full seed or independently count the original database. Whole shared-store capacity was not remeasured.

## Selected leads and executed tests

The highest-value aircraft lead is the pair of nearby discontinuities on one track. Catalog-plane geometry and same-epoch inconsistencies supply separate diagnostic leads, not confirmed physical events. Selection and sensitivity work are exploratory; aggregate coverage and then candidate records had already been seen. Prior saved review notes were read and are disclosed, not presented as fresh independent discoveries.

### Aircraft: source-bound discontinuities, unresolved cause

| September 14 UTC pair | Displacement | Time gap | Coordinate-implied speed | Attached groundspeed |
| --- | ---: | ---: | ---: | ---: |
| 22:48:59.09–22:49:06.74 | 5.929 km | 7.65 s | 775.1 m/s | 248.0 m/s |
| 22:49:23.78–22:49:29.73 | 5.591 km | 5.95 s | 939.7 m/s | 248.0 m/s |

OBSERVATION — All four linked positions match the corresponding original processed trace rows. Independent unit-vector geometry reproduces the detector distances to numerical precision. All four have the same publisher and MLAT label; the serializer does not flag them stale. **Actual position and metadata-field ages remain unknown**, not zero. The attached speed, altitude and track repeat across the four records; those fields are not independent motion measurements.

The default jump screen uses a minimum 5 km displacement, speed greater than 600 m/s, and adjacent intervals of 1–120 seconds. There are 12,172 eligible adjacent pairs in the saved current set, including 12,118 with the same known source/method. Both flagged pairs survive the same-source requirement. Changing only the exploratory speed threshold to 500, 600, 800 and 1,000 m/s yields **2, 2, 1 and 0** candidates respectively. A strict known-position-age filter leaves **zero eligible pairs**, so it cannot establish a clean negative. No same-aircraft/region prior baseline rows were present for this selected case.

INFERENCE — A simple source-switch explanation is weakened for these two pairs, but same-source processing, MLAT solution error, retained fields and equipment effects remain viable. Two pairs from one trace are not two independent physical incidents. They establish reported-coordinate inconsistency, not actual supersonic motion, interference or intent. The discriminating next evidence would be independent event-time positions and receiver/solver timing and calibration information, not a larger count of copies of this same feed.

### Satellites: catalog diagnostics, not maneuver detections

Independent arithmetic reproduces all **264 element-discontinuity flags** across 81 identifiers. Of these, **263 exceed only the raw node-longitude (RAAN) threshold**; one also exceeds the mean-motion-change threshold. Epoch gaps range from 2.97 to 72.55 hours, with a 17.03-hour median; 24 comparisons span at least 48 hours. An absolute element threshold over unequal elapsed times is not an epoch-aligned physical-change test.

In the **42 flagged comparisons below 1 degree inclination**, raw RAAN differences range from −168.3161 to +126.6781 degrees. The independently calculated angular separations of their catalog plane normals range only **0.00061–0.10394 degrees** (median 0.00397 degrees). This demonstrates why a large node-angle change near an equatorial plane cannot be read as an equally large plane rotation. It is a geometric diagnostic between catalog estimates, not orbit propagation, a calibrated residual or proof of no maneuver.

The audit also verifies **14 same-source, same-object, same-epoch conflicting catalog groups** across 13 identifiers and **8 stale-element flags**, with ages 74.7–697.4 hours at retrieval. All conflicting epoch groups are excluded from the discontinuity comparisons. These are product-consistency and freshness findings, not 22 additional physical events. Several source labels share CelesTrak ancestry and do not establish independent sensing. In addition, **77 flags belong to 23 groups sharing identical two-epoch element solutions across different catalog IDs**: only 210 distinct element-pair signatures occur among the 264 flags. This shows potential dependence, possibly including co-orbiting assemblies; it does not prove duplicate objects or catalog errors.

Three bounded catalog leads were retained: (1) ID 100712 changes mean motion from 15.95981559 to 15.49182662 revolutions/day over 24.2732 hours, warranting independent identity/orbit checks; (2) ID 40267 has a −168.3161-degree RAAN change but only 0.01813-degree catalog-plane-normal separation, illustrating coordinate sensitivity; (3) ID 53239 has seven pairwise RAAN rates between −6.079409 and −6.078864 degrees/day, illustrating nearly constant catalog drift rather than seven demonstrated physical events. These are diagnostic selections, not a ranked list of military or commercial incidents.

No SGP4 propagation, new J2 residual calculation, independent tracking, covariance assessment, service-notice test or operator confirmation was performed. Prior saved J2 review notes were acknowledged but not revalidated as a result of this addendum. Ordinary orbit evolution/refitting and product effects remain alternatives; the available checks do not prove a physical maneuver or its absence.

## Hypothesis verdicts and completion

| Claim | Verdict within this evidence |
| --- | --- |
| Saved aircraft coordinates contain discontinuities | **Supported at processed-data level** by raw-row matching, independent geometry and replay |
| Those two jumps are merely source switches | **Weakened**: no method/publisher switch in either pair; other artifacts remain unresolved |
| Large satellite RAAN flags establish large plane changes | **Weakened** for near-equatorial comparisons by plane-normal geometry; physical changes remain untested |
| Catalog conflicts/staleness occurred in saved products | **Supported at product level**, not independent physical-event evidence |
| Physical disturbance, military activity or trade harm occurred | **Not tested/unsupported**: independent physical and operational evidence is missing |

P01 scope and P04 versioned plan were recorded. P02 was a partial offline capability/provenance audit; P03 was bounded export-based triage, not global discovery. P05 reused verified saved inputs without acquisition. P06 checked integrity, core source-row correspondence, time, coverage and missingness; full raw normalization was not repeated. P07 quantified data deviations. P08 live GEV map writing was unavailable and not attempted. P09 stated competing explanations; P10 executed replay, geometry, threshold, source-continuity, epoch and catalog diagnostics while environmental/operational tests stayed blocked. P11 independently checked central arithmetic and causal language. P12 preserves this final addendum and reproducibility records; transport status is tracked separately.

ASSUMPTION — The saved source labels and element conventions describe processed provider products; they do not certify independent physical truth. SPECULATION — No actor, mission, causal event or monetary estimate is supplied. Earlier conversation summaries and saved GEV review notes were prior exposure. No new weather/energy report was read to fit these conclusions, and no cross-domain synthesis or forecast was made.

## Preservation, reproduction and remaining dependency

Method and executed detector pin: [satellite-research `e9105bf`](https://github.com/6t8hggfm44-tech/satellite-research/tree/e9105bf38cdca6e78955f03844a2c894c9abd793). The private evidence package includes plans, exact code identities, independent audit scripts and results, source ancestry and correction notes. Raw archives and private operational state are not part of the public report packet.

The exact inner evidence ZIP is 39,966,775 bytes, SHA-256 `dd8f5c46566b49f717e9fd1d2e0254bc9c8d5baf7ea8834bc9cfe3518e04a872`; its outer access artifact is 39,972,223 bytes, SHA-256 `48a93858a4a7cebedc65b7a34d889573a9ec62397e3fffbfc6f55296bcd9ed3d`. Full replay requires those exact private inputs; the temporary access artifact expires September 23, 2026 at 19:40:08 UTC. This report does not promise later transport availability. Selected derived results remain in the immutable private report package; hashes alone cannot restore missing bytes.

The remaining substantive gap is access to the separately stored retrospective daily-review bytes and the missing original-window beginning, followed by their own verified reproduction and independent controls. No such extra acquisition/export or repeated weekly run is claimed here. No collector, cadence, permission, billing, pending approval or market forecast was changed. Any safe public packet is staged for Market's next existing cycle, not acknowledged or canonical merely by being staged. New knowledge must not be backdated into the original report or earlier forecasts.
