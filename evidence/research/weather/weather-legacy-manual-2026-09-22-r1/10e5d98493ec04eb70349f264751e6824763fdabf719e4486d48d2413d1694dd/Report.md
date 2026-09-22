# Weather hypothesis test report — partial pilot coverage, no registered temperature departure

Run ID: weather-legacy-manual-2026-09-22-r1 · Version: 1 · Status: completed with coverage and corroboration limits

This is an authorized manual dress rehearsal; no scheduled occurrence was consumed. Generated: 2026-09-22T19:02:12.300315+00:00. Evidence cutoff: 2026-09-22T18:32:18.824529+00:00. Requested week: 15–21 September 2026 UTC, ending 22 September exclusive. Lagged analysis window: 13–19 September, ending 20 September exclusive. Scientific code and workflow: `a90f8d71ece978f8a1cdbd9edbdd3c87c3c975d0` (workflow 1.0.0).

## Finding and decision relevance

The verified archive supports a **limited negative screening result**: none of the 24 available daily temperature comparisons across four pilot grid points passed the registered joint threshold, |descriptive z| ≥ 2.5 and |departure| ≥ 3°C. It does not establish normal conditions throughout the requested week, a global absence of extremes, or any energy or market effect.

Every point has six observed estimate days in the lagged window (13–18 September) and only four in the requested week (15–18 September). The requested 19–21 September values are absent. Independent arithmetic, raw-body checks and deterministic replay reproduce the available numbers. NASA POWER represents assimilated grid estimates, not station ground truth; the [source methodology](https://power.larc.nasa.gov/docs/methodology/meteorology/) describes the product family.

## Scope, sources and actual coverage

Measured coverage is the configured Houston (29.76, −95.37), Chicago (41.88, −87.63), Rotterdam (51.92, 4.48) and Frankfurt (50.11, 8.68) point proxies. These are neither population-weighted regions nor global sensors. Worldwide current official lead discovery was unavailable in this offline round. No fresh provider request or collector ran.

The restored archive has 68 captures: 44 POWER, 12 NWS point metadata and 12 NWS forecasts; 23,688 record-content versions and 29,376 capture appearances. Captures span 14 September 14:06:39.753521Z through 21 September 20:15:33.798992Z. The physical screen examined 22,020 as-of grid records without reaching its 100,000-record cap. The actual latest usable physical day is 18 September; the later read date does not make observations fresher. Known capture times are conservative availability bounds; original publication times remain unknown.

The complete requested-week denominator is seven days. All 12 point-variable series have 4/7 requested and 6/7 lagged-day coverage, with no invalid returned record in the lagged window. Absence is distinct from invalid values and from zero precipitation. Raw POWER headers identify UTC days, API v2.10.0, and GEOSIT/MERRA2/POWER lineage. No independent station, hydrological, facility or economic outcome was admitted.

## Shortlist and measured results

Weather-only ranking used coverage, historical controls, absolute temperature departure and persistence, with fixed geography. The strongest primary standardized temperature lead was Frankfurt on 15 September: **20.95°C**, **4.08°C above** the 145-day seasonal sample mean, but only **z = 1.04**. It fails the joint flag and is retained as a descriptive comparison, not an extreme-event finding. Other points' primary maximum absolute z were below 0.78. No positive case was forced. Rain and wind are descriptive, with no hazard threshold registered.

All values below summarize **six available UTC days, 13–18 September**, not a full seven-day total. HDD/CDD sum max(18−T, 0)/max(T−18, 0) from each daily mean in °C-days. Missing days are excluded without extrapolation.

| Grid proxy | Mean °C | HDD18 | CDD18 | Rain total mm | Mean 10m wind m/s |
|---|---:|---:|---:|---:|---:|
| Houston | 29.09 | 0.00 | 66.56 | 18.91 | 2.13 |
| Chicago | 20.34 | 0.00 | 14.06 | 17.82 | 4.43 |
| Rotterdam | 17.83 | 4.24 | 3.23 | 17.22 | 5.12 |
| Frankfurt | 17.91 | 4.74 | 4.18 | 25.27 | 2.48 |

## Hypotheses and completed tests

The plan was frozen at 18:33:57.373049Z on 22 September before archive calculations. This is exploratory descriptive analysis of retained evidence, not held-out confirmation or a historical first-release backtest.

| Hypothesis | Prediction / falsifier | Tests and verdict |
|---|---|---|
| W-H1: sustained unusual temperature departure | Repeated eligible departures survive registered comparisons; eligible no-departure results weaken it | W-T2–4 weaken the claim on the six measured pilot days. Full-week and global claim remains inconclusive. |
| W-H2: ordinary seasonal variability | Compatible prior same-point controls encompass values; persistent robust departures would contradict it | W-T4 is consistent with this alternative. It does not establish all-week normality or exclude unmeasured hazards. |
| W-H3: coverage or insufficient history prevents inference | Missing days or inadequate historical controls block interpretation; complete eligible coverage would falsify that limitation | W-T2 supports the full-week gap; W-T4 rejects baseline insufficiency for these captured comparisons, because five years are present. |
| W-H4: forecast-only risk or changing vintages explains a signal | An apparent signal is forecast-only or changes with retained versions; stable independent measurements would weaken it | W-T5 leaves realization untested. W-T6 finds stable numerical event values, but independent measurement corroboration is absent. |

W-T1 passed archive raw SHA-256/SQLite integrity, screening manifests and actual deterministic replay. Repeated scientific JSON fields match exactly after excluding the actual generation timestamp. W-T2 independently selected eligible natural-key versions using read-only SQL. W-T3 independently reproduced all 12 means, eight HDD/CDD totals and four rain totals; separately decompressed source bodies matched all **72** event point-variable-day values, units and UTC standard.

W-T4 uses previous calendar years 2021–2025, excluding the event period, with a primary ±15-calendar-day seasonal band. The temperature baselines contain 143–148 days and all five years, exceeding the 60-day/three-year minimum. Primary z ranges from −0.54 to +1.04. At ±7 and ±30 days the largest absolute temperature z is 1.20 and 0.90, respectively. None passes even the sensitivity threshold |z| ≥ 2.0 with the unchanged 3°C condition and 80% coverage rule. Requiring 100% weekly coverage blocks every point; that is an ineligible test, not a negative result. The 252 baseline eligibility calculations include missing target days and three variables; they are not 252 independent confirmations. The effective observed temperature sample remains 24 daily point comparisons with serial and spatial dependence.

W-T6 found 12 event natural keys with multiple record-content versions, but **zero changed numerical values among the 72 lagged event entries** across retained versions. Archive-wide content version changes must not be equated with changed measurements. No unknown historical forecast issue or first publication vintage was reconstructed.

## Forecasts, controls and uncertainty

The current screen preserves 30 NWS forecast periods for the two U.S. points, with issues from 20–21 September and valid intervals spanning 21 September 11:00Z through 28 September 11:00Z. Twenty-eight were captured before their valid start; two were captured during or after that start. Issue, capture and lead-time records remain separate. Forecast-period highs/lows are not POWER daily means, so **no forecast skill score or realized-hazard claim** was calculated. See the [NWS API documentation](https://www.weather.gov/documentation/services-web-api) for the product family; preserved exact queries are listed in the evidence register.

The baseline is an uncalibrated five-year sample, not an official climate normal or probability model. The same POWER product supplies the historical controls and event estimates. Independent arithmetic is a reproducibility check, not independent physical corroboration. Nearby stations, alternative models, hourly local-day transforms and full-week values are missing. Holiday, demand, infrastructure and financial effects have not been tested. Rain does not establish flooding; 10m wind does not establish turbine output. Terrestrial conditions cannot substitute for ionospheric evidence in a GNSS claim.

## Prior findings, corrections and next decisive evidence

The previous Weather report, `weather-weekly-2026-09-21`, hash `62f2e8c98123b39a7ee1dab9c2fddfa92b07d38c6ec3e47e925c1c4a1cfc7a1a`, correctly reported that it could not materialize measurement bytes. This separate manual report advances evidence availability and actual calculation; it does not erase the earlier access limit, supersede its historical knowledge state or backdate any result. Reading that prior report exposed only a high-level statement that its contemporary GEV report was an evidence gap; no GEV event result, Energy outcome or Market outcome informed this selection.

The next decisive evidence is completion of the missing 19–21 September physical values and compatible independently retained station measurements. A bounded later authorized report could resolve whether any newly observed pilot day crosses the same registered joint thresholds and whether a supported departure persists. No direction is forecast for unseen days. A false prediction would be recorded if a later preregistered directional claim failed; this round makes none. No additional collection or schedule is created here.

## Independent freeze, handoff and reproducibility

The Weather report is frozen before current Energy or GEV reports are opened. Exact freeze time and final report/manifest/envelope hashes are in the companion freeze record and envelope. Cross-domain linkage is pending a separate synthesis with actual frozen counterparts; no weather adjustment or impact claim has been made. Immutable persistence and Market staging/receipt are tracked externally by the owning workflow; this report does not assert that transport equals receiver acknowledgment.

The preserved package contains the original test plan, source register, raw audit, independent numeric audit, baseline sensitivity table, forecast chronology, command log, replay verification and source/config/code identities. Effective config SHA-256: `12ba5b9ab5bfaed6e201656a19f76c7f8c048a373592ed62f54d75cf119a4f3e`; workflow SHA-256: `95d22dcd628693e5ff1a6ae444a6f8b4a1f3721c70d075183a04ccf4cf60757e`. The source product is documented by the [POWER Daily API](https://power.larc.nasa.gov/docs/services/api/temporal/daily/). Raw captures remain in authorized private storage; this prose is safe for the approved report handoff.
