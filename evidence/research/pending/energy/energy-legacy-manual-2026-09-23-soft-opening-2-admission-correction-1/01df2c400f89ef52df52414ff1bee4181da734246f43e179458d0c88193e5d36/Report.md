# Original Energy: lagged product builds challenge broad scarcity

## Summary

**OBSERVATION:** In the latest retained EIA week ending September 11, commercial crude stocks fell 0.640 million barrels while gasoline rose 0.794 million and distillate rose 1.585 million barrels. Refinery utilization declined 1.0 percentage point to 96.8%. These mixed movements weaken a broad petroleum-scarcity interpretation. Stronger final consumption, a causal supply shock and economic transmission remain unproven.

## Coverage

The requested calendar week is September 16–22 UTC; none of the twelve measured series has a period endpoint inside it. All latest endpoints are September 11, with a nominal flow week September 5–11; stocks remain end-period levels. The September 22 collector captured twelve successful EIA responses, but a new capture did not create a new reporting period. The report worker invoked no collector and preserved all source state.

The newest completed private snapshot is bound to state `dbe8a975366bd0accb14c85e4383174c7cd9574d`. All 166 snapshot files and the exact outer digest, inner manifest and control receipt were verified before restoration. Deployed Energy code `28ea17c51a61f97e17aea6a4ac044a19a434fd98` produced the screen at the fixed September 23 01:10:05 UTC evidence cutoff. Its current-vintage histories are not original-release backtests. Twelve enabled US weekly petroleum series are measured; credentialed European gas is disabled, and LNG/electricity extensions are not measured by this producer.

## Hypotheses and tests

The shortlist was crude-stock draw, distillate stock/product-supplied divergence, and refinery utilization. Distillate was selected as the clearest test of whether a stock narrative survives a demand-proxy comparison. Original rules fixed one-week and four-week same-series comparisons, units and the missing-control boundary before numerical extraction. Selection is exploratory, and shared EIA series are one statistical family.

| Indicator | September11 | One-week change | Four-week change |
|---|---:|---:|---:|
| Commercial crude stocks | 423.429 million bbl | −0.640 million | −5.386 million |
| Gasoline stocks | 207.732 million bbl | +0.794 million | −1.646 million |
| Distillate stocks | 107.859 million bbl | +1.585 million | +2.240 million |
| Distillate product supplied | 3.501 million bbl/day | −0.177 million | −0.452 million |
| Crude exports | 4.831 million bbl/day | +1.414 million | +0.765 million |
| Refinery utilization | 96.8% | −1.0 percentage point | −0.4 percentage point |

Distillate stocks rose 1.491% on the week while its product-supplied proxy fell 4.812%; over four weeks, stocks rose 2.121% and supplied fell 11.434%. Thus the simple claim that falling availability broadly demonstrates accelerating petroleum consumption is contradicted by this product's observed directions. It does not follow that end-user consumption fell by the supplied percentage: product supplied is a disposition proxy and estimates can reflect timing or trade.

Crude exports rose 41.381% on the week, imports rose 3.429%, domestic crude production was nearly flat (−0.0215%), and refinery inputs fell 1.456%. A deliberately incomplete production + imports − exports − refinery-input calculation gives −8.113 million barrels over seven days, versus the measured −0.640 million commercial-stock change. The 7.473 million-barrel residual demonstrates that this roster does not close an accounting balance; omitted adjustments, timing and stock definitions prevent using it as proof of a supply shock.

**H1, broad scarcity:** weakened by simultaneous product builds. **H2, ordinary trade/refining/product mix:** consistent but not causally identified. **H3, stronger final demand:** untested; the distillate proxy points the opposite way, while gasoline supplied rose 2.889%. **H4, weather or operational disruption:** untested because matched exposure, outages and outcome controls were not acquired. The unchanged provisional seasonal screen returns zero candidates at its 3.5 robust-score rule; that is not a calibrated absence-of-risk probability.

All twelve series' weekly/four-week differences and percentages were recomputed from exact retained rows; an independent reviewer confirmed 48 numerical checks. The archive/screen and the saved numerical package are separately verified. Relative utilization change (−1.0225%) is not confused with its −1.0 percentage-point movement. No new source observation is claimed relative to the September22 investigation; it remains an independently versioned earlier report.

## Limitations

Shared EIA methods, unknown original publication vintages, current-vintage historical reconstruction, estimates and release lag limit inference. No price, margin, inflation, GDP or cargo-volume response was tested. National fuel data cannot be weather-adjusted using one city grid point without frozen weights. Suite Energy reuses this same EIA family and receives no additional independent evidence vote. No completed earlier report is overwritten.

## Sources

[EIA commercial crude stocks](https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=WCESTUS1&f=W), [distillate stocks](https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=WDISTUS1&f=W), [distillate product supplied](https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=WDIUPUS2&f=W), and the nine other EIA series identified with exact source URLs/capture hashes in the private source register. Snapshot receipt, code/configuration and numerical rows are pinned in the manifest.

## Next decisive evidence

A newer actual reporting period, a complete compatible petroleum balance, dated facility/outage evidence and independent demand/exposure controls could discriminate mechanisms. Cross-domain linkage requires independently frozen versions and matched physical outcomes; the present data do not establish it. No collection or monitoring schedule is added.
