# Weather hypothesis report: partial late-September pilot coverage

Run: weather-legacy-manual-2026-09-30-repair-test-1

## Finding
The saved pilot supports a partial description of September 21–25, not a complete current-week weather verdict. Each of four grid proxies has only three of seven requested UTC dates, September 23–29, and five of seven lagged analysis dates, September 21–27. Both fractions fall below the existing 80% completeness rule. Zero automated candidates must not be interpreted as normal weather or absence of hazards.

This is a completed bounded saved-evidence investigation, including explicit inconclusive results. Calculations are new; underlying acquisitions are reused. No provider was queried for this investigation. The same analyst saw operational metadata and descriptive results across the three families; selection and cross-domain interpretation are exploratory, not blinded confirmation. No current Market conclusions or prices were used. Each domain report is frozen separately before reconciliation. Hashes verify preserved bytes and computational consistency, not the truth of an economic or physical causal claim.

## Scope, selection and dates
Evidence cutoff: 2026-09-30T19:05:20.725243+00:00. Latest estimated observation date is September 25; the latest NASA POWER capture is September 28 at21:35:22.787554Z. Selected current value versions were first observed between September24 19:47:05.597387Z and September28 21:35:22.787554Z. Actual publisher publication timestamps remain unknown. POWER records are gridded assimilated estimates sourced through GEOSIT/MERRA2/POWER, not station ground truth. The measured geography is Houston, Chicago, Rotterdam and Frankfurt grid proxies; it is not global coverage or population-weighted demand.

The independent weather shortlist was Houston warmth/cooling exposure, Frankfurt low accumulated rainfall, and Chicago 10-m wind. These are descriptive candidates within existing pilot exposure choices; none establishes an unusual sustained event or economic impact. The main investigation is coverage and robustness across all four proxies, rather than forcing a positive lead. Global new-source discovery and independent station verification were outside the saved-evidence test.

## Executed measurements
All figures below cover the five available UTC days September21–25; missing dates are not filled with zero or extrapolated.

| Grid proxy | Mean temperature C | Rainfall mm over5days | Mean10m wind m/s | HDD18 C-days | CDD18 C-days |
|---|---:|---:|---:|---:|---:|
| eu_germany_frankfurt | 14.342 | 0.05 | 2.256 | 18.29 | 0.00 |
| eu_netherlands_rotterdam | 16.642 | 0.96 | 3.224 | 6.79 | 0.00 |
| us_gulf_houston | 28.904 | 11.30 | 1.802 | 0.00 | 54.52 |
| us_midwest_chicago | 16.658 | 1.21 | 5.460 | 6.71 | 0.00 |

## Tests and competing explanations
1. Data integrity: the exact collector snapshot and every preserved file passed manifest/restore checks. All60 current point-variable-date cells were independently compared with the original saved publisher JSON cells. All12 point-variable summary metrics were independently recomputed from the archive.
2. Coverage artifact versus sustained departure: missing September26–29 requested dates prevent a whole-week verdict. A coverage gap is supported; a sustained current-week physical anomaly is inconclusive.
3. Seasonal variability: the deployed1830-day historical horizon supplies144–148 matched days across five prior calendar years for each temperature-date comparison. Maximum absolute descriptive z is1.432. An exploratory sensitivity using all saved prior-year seasonal rows gives max absolute z1.469 for a15-day seasonal band,1.598 for10days and1.675 for5days. No comparison crosses the provisional2.5 threshold. These are serially dependent descriptive comparisons, not calibrated probabilities or official climate normals.
4. Degree-day sensitivity: Houston five-day CDD totals are64.52,54.52 and44.52 C-days at bases16,18 and20C. Frankfurt HDD totals are8.29,18.29 and28.29 C-days. Exposure magnitudes depend on the explicit base; no utility-load response is inferred. Rain and10-m wind remain descriptive, not flood or turbine-output estimates.
5. Forecast-only risk:24 retained NWS forecast periods were captured before their valid starts. Houston issue time is September28 18:22:18Z; Chicago issue time is21:16:41Z; captures are21:35:23.109256Z and21:35:23.269430Z. Valid intervals span September29 11:00Z through October5 11:00Z. Issue time is not asserted to be first publication time. Compatible realized verifying targets are unavailable, so forecast skill is not scored; high/low period forecasts are not daily means.
6. Source/model revision and economic linkage: preserved versions and provenance can be audited, but independent event-time station controls and compatible energy/transport outcomes were not obtained. Those hypotheses remain inconclusive or not tested. Agreement among nearby model-derived values would not supply independent sensing.

## Verdict and decisive evidence
The evidence supports a partial archive description and known coverage limitations. It neither identifies an extraordinary weather shock nor establishes normal conditions for the missing days. Confidence is high in reproduced stored arithmetic and low in any current-week physical or economic generalization. Needed next evidence is complete eligible September23–29 weather observations, independent station corroboration, and predeclared compatible exposure/outcome controls. No forecast, trading or attribution recommendation is made.

## Sources and reproducibility
[NASA POWER](https://power.larc.nasa.gov/) supplies the saved gridded values; [NWS Houston forecast](https://api.weather.gov/gridpoints/HGX/63,95/forecast) and [NWS Chicago forecast](https://api.weather.gov/gridpoints/LOT/76,73/forecast) identify the retained forecast products. Their live pages may now differ. The evidence package preserves source hashes, original URLs, capture/issue/valid times, raw-cell audit, calculation inputs/results and the reproduction script. Scientific workflow/code: weather@a90f8d71ece978f8a1cdbd9edbdd3c87c3c975d0. No earlier forecast or report is overwritten.

## Packaging correction, version2
This one-off manual test report replaces an unpublished frozen draft identified by SHA-256 09e37c71d5200e4eab0980ab48fa962839365a522c79c7179da56c079504266f. The correction supplies the manual-test envelope classification and preserves all scientific results, source dates and evidence cutoffs. No new investigation or source acquisition occurred.
