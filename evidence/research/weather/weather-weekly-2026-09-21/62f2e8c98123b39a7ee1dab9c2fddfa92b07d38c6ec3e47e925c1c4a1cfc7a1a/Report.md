# Weather hypothesis test report — 14–20 September 2026 evidence gap

Run ID: weather-weekly-2026-09-21 · Version: 1 · Status: complete evidence-gap report

Generated at: 2026-09-21T17:18:48Z · Evidence cutoff: 2026-09-21T17:18:22Z · Requested event week: 2026-09-14T00:00:00Z to 2026-09-21T00:00:00Z

Workflow and installed scientific code: weather commit `a90f8d71ece978f8a1cdbd9edbdd3c87c3c975d0` (workflow 1.0.0) · Independent Weather freeze: recorded with this package · Prior exposure: the current GEV report was known to be an evidence-gap report; no GEV anomaly, Energy result, or Market outcome was used to select a Weather lead.

## Finding and decision relevance

**OBSERVATION:** the collector control record says its 20 September bounded Weather pass completed with 12 successful requests and no reported failed request. Its private snapshot manifest inventories 60 Weather captures, 23,648 normalized record versions, and 27,908 capture-to-record appearances as of 2026-09-20T18:29:34Z.

**OBSERVATION:** those are collector and manifest metadata, not the Weather values themselves. The weekly worker could not materialize the current private artifact bytes: the authorized artifact reference yielded HTTP 403 in this cloud runtime. The one permitted official NASA POWER alternative read was also inaccessible through the available web retrieval route. The SQLite database and compressed raw bodies therefore were not independently restored or verified here.

**INFERENCE:** no measurement-level temperature, precipitation, wind, degree-day, anomaly, forecast-realization, or economic-impact conclusion can be supported for the requested week in this run. This is an evidence-gap result, not evidence of ordinary weather and not evidence of an extreme event.

## Scope and coverage

The registered measured scope was the four configured NASA POWER grid proxies near Houston, Chicago, Rotterdam, and Frankfurt, with NWS forecasts configured for the two U.S. points. The intended variables were daily mean temperature in °C, corrected precipitation in mm/day, 10 m daily mean wind in m/s, and HDD/CDD at an 18 °C base using UTC days.

Actual value coverage analyzed: **none**. The metadata-only snapshot covers a private Weather archive created on 20 September, but hashes and row counts do not expose event dates, values, missingness, vintages, or forecast issue/valid times. Requested-week coverage, the lag-adjusted seven-day window, usable-day denominators, baseline readiness, and forecast lead times remain unverified.

The broader global-context shortlist could not be completed from primary evidence within the bounded access route. No warning, station, reanalysis, or national-authority lead was treated as realized weather.

## Shortlist and selection

No defensible measurement lead was selected. The four pilot points remained candidates only by predeclared exposure rationale, not because their values were observed. The current private collector metadata showed successful acquisition activity, but interpreting that as a weather signal would confuse process status with evidence.

The strongest valid case was therefore the access and reproducibility gap itself: current private evidence appears to exist, but it was not readable and integrity-checkable by this weekly worker. No positive candidate was manufactured from metadata.

## Measurement-level results

No Weather metric was calculated. In particular:

- temperature departures and descriptive seasonal z-scores: **not tested**;
- HDD/CDD at 18 °C: **not calculated**;
- precipitation totals: **not calculated**; missing values were not treated as zero;
- 10 m wind summaries: **not calculated**;
- requested-week and lag-adjusted coverage: **not established**;
- forecast-versus-realization: **not tested**.

The manifest-reported counts are archive structure, not independent confirmations of any weather condition.

## Hypothesis verdicts

| Hypothesis | Registered prediction / falsifier | Tests actually completed | Verdict | Next decisive evidence |
|---|---|---|---|---|
| H01: sustained departure | Adequate coverage plus a persistent threshold-exceeding departure | T01 blocked; no values | Untested | Verified restore of current snapshot, then deterministic screen |
| H02: ordinary seasonal/spatial variation | Values remain within thresholds or vary materially across points | T01/T02 blocked; no values | Untested | Same-point seasonal comparison with usable denominators |
| H03: source/vintage/coverage artifact | Candidate changes across vintage, boundary, or coverage checks | Metadata lineage inspected; value-level T02/T03 blocked | Inconclusive | Verify every archive byte and SQLite lineage before interpretation |
| H04: forecast risk without verified realization | Eligible forecast exists but lacks compatible verification | T04 blocked; issue/valid records unreadable | Untested | Pre-valid-interval issue plus compatible observation |

## Executed tests

**T03 archive-integrity audit (prospective, partial).** The weekly worker verified the repository identity of the collector control record and manifest text. The manifest records a 31,989,760-byte Weather SQLite object with SHA-256 `916028cafa6edcece97e89302df1c562cf02aa0c123bafb8c75ffb02a67f4a01`, 60 referenced raw objects, and logical table fingerprints. This does not satisfy the registered test: the SQLite and raw gzip bytes were not materialized, so SQLite `integrity_check`, logical-row reproduction, raw-body hashing, and fileset equality were not executed.

**Access-route test.** The private artifact byte request returned HTTP 403. Under the live access-resolution policy, one bounded official NASA POWER alternative was selected; the available web retrieval route reported that the API URL was inaccessible. No blind retry, credential change, provider bypass, collector restart, or additional schedule was attempted.

**T01/T02/T04.** Not executed because the required values and forecast vintages were unavailable. Sample sizes and missing counts are unknown rather than zero.

## Forecast versus realization

No NWS forecast body, issue time, capture time, valid period, lead time, or compatible verifying statistic was readable. No forecast score was calculated. A current or late forecast cannot reconstruct an unavailable historical issue.

## Independent corroboration and controls

No station, second model, warning verification, or reanalysis value was admitted as corroboration. NASA POWER would be an assimilated grid estimate rather than station ground truth. The four points are illustrative proxies, not population-weighted regions or global coverage. Energy demand, production, transport, damage, and Market effects were not inferred.

## Sensitivity, corrections and audit

Threshold, seasonal-window, coverage, vintage, and UTC/local-day sensitivities were blocked before calculation. Audit confirmed that:

- archive metadata was not substituted for actual bytes;
- process success was not substituted for scientific success;
- hashes were not treated as proof of cloud byte availability;
- missing values were not treated as normal observations;
- no Weather finding was selected from cross-domain outcomes;
- the older 14 September missed occurrence remains a separate pending record and was not reopened.

No numerical claim required correction because no numerical Weather claim was made.

## Limits and next predictions

This report cannot exclude meaningful weather departures during 14–20 September. It also cannot establish that any departure occurred. The next decisive evidence is a verified, safely restored current collector snapshot or a permitted official extract with dates, units, vintages, values, and missingness. A future already-authorized occurrence may use such evidence under its own gate; this report creates no retry or catch-up authority.

## Frozen handoff and reconciliation status

The independent Weather conclusion is frozen as: **current measurement evidence was unreadable in this runtime, so all substantive Weather hypotheses remain untested or inconclusive.** The final private package and its hashes are immutable under the producer repository. Only this reviewed report, its shareable envelope, and transport packet may be staged for Market. Staging is not canonical receipt; Market acknowledgment remains for its next existing cycle. No cross-domain reconciliation was performed because there was no Weather measurement finding to link.

## Sources and reproducibility

- Weather workflow and scientific code: public repository commit `a90f8d71ece978f8a1cdbd9edbdd3c87c3c975d0`.
- Effective pilot configuration SHA-256: `12ba5b9ab5bfaed6e201656a19f76c7f8c048a373592ed62f54d75cf119a4f3e`.
- Workflow definition SHA-256: `95d22dcd628693e5ff1a6ae444a6f8b4a1f3721c70d075183a04ccf4cf60757e`.
- Archive verifier SHA-256: `3fc87c73138430c56eb49b2093a32254ac2fa70819ae9e5f550f292fb4526800`.
- Access-resolution policy commit: `7915305d493bb890b538972b8590d2d988161184`; helper SHA-256: `e3ef9a9bcd0dcb67b262ee663efbdcfa54819f5162596973b94accac5985a048`.

Raw Weather evidence remains in authorized private collector storage and is not included in this package or public handoff.
