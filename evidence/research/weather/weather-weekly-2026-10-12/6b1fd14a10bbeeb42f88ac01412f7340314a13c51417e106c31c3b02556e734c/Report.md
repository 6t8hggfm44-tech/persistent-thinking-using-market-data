# Weather hypothesis test report — no qualifying anomaly in configured sample

Run ID: weather-weekly-2026-10-12 · Version: 2 · Status: complete — negative relative to the registered threshold; broader conclusion inconclusive

Generated at: 2026-10-12T17:18:25.975599986Z · Evidence cutoff: 2026-10-12T17:14:01.078675441Z · Requested event week: 2026-10-05T17:14:01.078675441Z to 2026-10-12T17:14:01.078675441Z · Actual archive coverage: lag-adjusted UTC days 2026-10-03 through 2026-10-08; requested-week values available for 2026-10-05 through 2026-10-08

Workflow and installed code commit: `a90f8d71ece978f8a1cdbd9edbdd3c87c3c975d0` · Independent Weather freeze: 2026-10-12T17:18:25.975599986Z, manifest SHA-256 `8925ec77816a109555e77b88e7afb54c091e4d60246eb29d1b4f8549c0bd80eb` · Prior exposure to GEV, Energy, or Market outcomes: none

## Finding and decision relevance

**OBSERVATION:** The registered screen found zero qualifying weather-anomaly candidates among four configured NASA POWER point-grid proxies. No temperature point-day met both the absolute-departure threshold of 3 C and the absolute z-score threshold of 2.5. Leave-one-location-out candidate counts were also zero.

**INFERENCE:** A sustained, spatially coherent departure in this configured sample is weakened. Ordinary seasonal or local variation remains a plausible explanation for the observed values. Mild warmth around Rotterdam and Frankfurt is retained as context, but its standardized departures did not satisfy the registered rule.

**ASSUMPTION:** The five-year same-source seasonal baseline is useful for a provisional screen. It is not a climate normal and does not establish conditions outside the four sampled points.

**SPECULATION:** None. This report makes no claim about energy demand, generation, transport, prices, losses, or market effects.

## Scope and coverage

The verified private collector snapshot contained 180 captures and 25,035 record versions. The deterministic screen examined 22,032 latest records. The scientific footprint was four fixed NASA POWER point-grid proxies near Houston, Chicago, Rotterdam, and Frankfurt, plus NWS forecast grids near Houston and Chicago. NASA POWER values are gridded assimilated estimates, not station observations; NWS values are forecasts.

Each of the 12 point-variable combinations had six of seven days in the lag-adjusted analysis window (coverage 0.857) and four of seven days in the requested week. The lag was handled explicitly: unobserved days were neither imputed nor called normal. All 72 point-variable-day baseline checks were usable using prior calendar years 2021–2025 and a ±15-day seasonal window. POWER publication time is unknown, so first collector capture is the conservative availability bound.

## Shortlist and selection

The weather-only shortlist retained two leads. First, Rotterdam and Frankfurt showed the largest positive temperature deviations on 2026-10-06 and 2026-10-07, respectively. Second, 30 preserved NWS forecast periods described prospective Houston and Chicago weather. The European lead was selected for threshold testing because it was the strongest measured departure. The forecasts were preserved separately and not mixed with realized daily means. No lead became a supported anomaly candidate.

Primary source context: [NASA POWER Daily Point API](https://power.larc.nasa.gov/docs/services/api/temporal/daily/), [NASA POWER meteorology methodology](https://power.larc.nasa.gov/docs/methodology/meteorology/), [Houston NWS grid forecast](https://api.weather.gov/gridpoints/HGX/63,95/forecast), and [Chicago NWS grid forecast](https://api.weather.gov/gridpoints/LOT/76,73/forecast).

## Measurement-level results

All values below use six available UTC daily values; totals are incomplete seven-day totals. Degree days use an 18 C base and sum available daily means without extrapolation.

| Point proxy | Mean temperature (C) | Range (C) | HDD18 (C-day) | CDD18 (C-day) | Precipitation total (mm) | Mean 10 m wind (m/s) |
|---|---:|---:|---:|---:|---:|---:|
| Houston | 25.92 | 24.83–26.83 | 0.00 | 47.52 | 30.37 | 3.06 |
| Chicago | 16.26 | 15.61–17.50 | 10.42 | 0.00 | 0.12 | 4.70 |
| Rotterdam | 16.37 | 14.17–17.75 | 9.80 | 0.00 | 5.10 | 3.87 |
| Frankfurt | 15.63 | 13.01–16.70 | 14.24 | 0.00 | 12.43 | 2.04 |

The largest absolute departure was Frankfurt on 2026-10-07: 16.70 C versus a 12.45 C seasonal baseline, +4.25 C, z=1.51. The largest z-score was Rotterdam on 2026-10-06: 17.75 C versus 14.16 C, +3.59 C, z=1.83. Both missed the required z-score threshold.

## Hypothesis verdicts

| Hypothesis | Prediction / falsifier | Tests actually completed | Current verdict | Next decisive evidence |
|---|---|---|---|---|
| H01: sustained spatially coherent departure | At least two locations show persistent same-direction departures; falsified by sparse or unstable departures | T01, T02, T04 | Weakened | Complete compatible daily coverage over a future registered window and broader geography |
| H02: ordinary seasonal/spatial variation | Seasonal controls weaken the apparent signal | T02, T04 | Plausible, with sample limitation | Longer official baseline or station-level matched controls |
| H03: source/timing/coverage artifact | Findings depend on incompatible units, incomplete days, or mixed vintages | T01, T03 | Integrity-artifact explanation weakened; timing/coverage limitation remains | Known POWER publication timestamps and complete requested-week values |
| H04: forecast risk without verified realization | Forecast vintages exist but compatible verifying targets do not | T03 | Inconclusive / unscored | Same-variable, same-interval realization preserved after the forecast issue |

## Executed tests

T01 verified the collector control commit, provenance receipt, artifact hash, safe extraction, snapshot manifest, source lineage, units, timestamps, and all 485 archived files. It separated lag-adjusted coverage from requested-week coverage.

T02 ran the registered dual-threshold screen over 24 temperature point-days, using same-point prior-year seasonal controls. The deterministic output and an independent calculation agreed exactly; candidate count was zero.

T03 preserved forecast issue, capture, valid interval, and lead-time information. It did not compute a score because NWS 12-hour high/low forecast periods are not compatible with NASA POWER UTC daily-mean assimilated temperatures.

T04 repeated candidate counting under each one-location exclusion. All four variants retained zero candidates, so no qualifying result depended on a single sampled point.

## Forecast versus realization

Thirty NWS forecast periods were retained from issue vintages on 2026-10-11 for Houston and Chicago. They were prospective at capture. No forecast score or realization claim is reported: the available forecast statistic and interval do not match the available realized statistic and UTC interval. Reconstructing a compatible target after the cutoff would violate the predeclared test.

## Independent corroboration and controls

The four realized point series share NASA POWER ancestry and therefore are not independent providers. The two NWS forecast grids are an independent forecast source family but do not corroborate realized NASA POWER values. Controls were same-source, same-point, same-variable, prior-calendar-year seasonal windows. Grid proxies may differ from station or regional conditions; this report does not extend point results to whole regions.

## Sensitivity, corrections and audit

The registered thresholds, lag, seasonal window, point set, and baseline rule were not changed after measurement inspection. Removing any one point did not change the zero-candidate result. The strongest contrary observation—mild European warmth—was retained and quantified rather than discarded. The report identity was corrected from an unregistered packaging label to the registered recurring legacy Weather pattern; scientific evidence and claims are unchanged. The deterministic screen was independently recomputed without a mismatch.

## Limits and next predictions

This null screen cannot exclude unsampled regional extremes, station-level events, hazards outside temperature/precipitation/10 m wind, or events published after the cutoff. Requested-week coverage was only four of seven days. The short archive baseline is not a climatological normal.

For a future registered run, a decisive update would require either (1) at least two configured locations meeting both the 3 C and |z|=2.5 thresholds with at least 80% compatible coverage, or (2) a preserved NWS forecast matched to a same-variable, same-interval realized target. Those checks should use only evidence available by that future cutoff.

## Frozen handoff and reconciliation status

Independent Weather findings were frozen before any GEV, Energy, or Market report was opened. The corrected identity package's freeze-input manifest SHA-256 is `8925ec77816a109555e77b88e7afb54c091e4d60246eb29d1b4f8549c0bd80eb`. Cross-domain reconciliation was not performed because no counterpart conclusions were opened; there was no scientific post-freeze rewriting. Delivery staging, receiver acknowledgment, and canonical persistence remain separate operational states.

## Sources and reproducibility

The reproducibility package records the public Weather workflow commit `a90f8d71ece978f8a1cdbd9edbdd3c87c3c975d0`, private collector state commit `b33a5a0998c00b577aab0e2b87ea5d1fff671e15`, artifact SHA-256 `0b34345bbb5c22b6e994ac356986825ca6f0f2bfc9fb1c5db422f6d185e21879`, snapshot-manifest SHA-256 `f72dcf1f86ec511f88abe07dcf7968dbcf1f786c64d178561e00eed124b79f7a`, screen-summary SHA-256 `a443e33ad1e4c0203211f125ed28f582c83758b43028558ed55d2867e88b398b`, and configuration snapshot SHA-256 `8aeaf24bcc4460bad96c67e4fcdccac5d55f1008fe3f446fd7eeb8cc23dfdab3`. Exact capture IDs and raw-body hashes are in the private source register and verified collector archive. Raw source bodies remain in authorized private storage and are not included in the public handoff.
