# Original Energy hypothesis report: lagged petroleum balances

Run: energy-legacy-manual-2026-09-30-repair-test-1

## Finding
All12 enabled petroleum series are readable, but their latest observation is the week ending September18, nominal reporting period September12–18. None has a period endpoint in the requested September23–29 window. The newest acquisition attempt succeeded for3of12 series and timed out for9; earlier verified values remain available for all12. Those are separate acquisition and observation-coverage denominators.

This is a completed bounded saved-evidence investigation, including explicit inconclusive results. Calculations are new; underlying acquisitions are reused. No provider was queried for this investigation. The same analyst saw operational metadata and descriptive results across the three families; selection and cross-domain interpretation are exploratory, not blinded confirmation. No current Market conclusions or prices were used. Each domain report is frozen separately before reconciliation. Hashes verify preserved bytes and computational consistency, not the truth of an economic or physical causal claim.

## Source timing and measured scope
Evidence cutoff: 2026-09-30T19:05:20.725243+00:00. The latest value versions were first seen September23 between19:26:16Z and19:27:11Z. Actual publisher release timestamps and historical publication vintages are unknown. Later successful checks on September28/29 do not make these September18 observations current-week measurements. The three September29 successes were refinery crude input, crude imports and jet-fuel product supplied; the other nine last succeeded September28. No failed source was retried here.

This is a U.S. petroleum pilot. European gas storage is disabled; LNG, electricity and natural-gas coverage are not supplied by this archive. Original Energy and suite Energy share EIA ancestry. Agreement between them is not independent confirmation.

## Executed measurements
Levels and changes refer to September18 versus September11. Stocks are thousand barrels; flows are thousand barrels/day; utilization change is percentage points.

| Series | Level | Exact7-day change | Seasonal robust score |
|---|---:|---:|---:|
| Commercial crude stocks | 426,398.0 | +2,969.0 | +0.552 |
| Gasoline stocks | 206,046.0 | -1,686.0 | -2.382 |
| Distillate stocks | 107,431.0 | -428.0 | -1.577 |
| Strategic petroleum reserve crude stocks | 284,552.0 | -405.0 | -2.109 |
| Refinery crude input | 16,811.0 | -519.0 | +0.910 |
| Refinery utilization | 94.0 | -2.8 | +0.731 |
| Crude production | 13,939.0 | -5.0 | +1.162 |
| Crude imports | 5,877.0 | -1,181.0 | -0.944 |
| Crude exports | 3,281.0 | -1,550.0 | -0.679 |
| Gasoline product supplied | 8,847.0 | +49.0 | -0.036 |
| Distillate product supplied | 3,975.0 | +474.0 | +0.310 |
| Jet fuel product supplied | 1,650.0 | -150.0 | -0.240 |

## Selection, tests and hypotheses
The strongest retained lead is gasoline stocks,206.046million barrels, down1.686million barrels(-0.812%) week over week, with the largest absolute seasonal score at-2.382. Secondary leads are the lower Strategic Petroleum Reserve level and refinery/trade changes. Selection is exploratory across12 related series; it does not imply a contemporaneous shortage.

1. Source arithmetic: all12 exact7-day changes and seasonal median/MAD scores were recomputed independently. All24 latest/comparator cells were reparsed from hash-verified original EIA HTML. Each seasonal comparison uses55 prior-event-only observations. The baseline is a reconstructed current-vintage history, not a first-release backtest.
2. Threshold sensitivity: zero of12 scores exceed absolute3,3.5 or4.5. Two exceed2(gasoline stocks and SPR). The result is sensitive to a chosen lower threshold and does not estimate a calibrated false-positive rate. Zero flags are not evidence of normal current supply, especially with no current-week endpoints.
3. Demand versus refinery/trade explanations: gasoline product supplied rose49thousand barrels/day(0.557%), while refinery crude input fell519thousand barrels/day and utilization fell2.8percentage points. Crude production fell only5thousand barrels/day, imports fell1,181 and exports fell1,550. These concurrent components permit several ordinary balance explanations; product supplied is a consumption proxy, not direct end-user demand.
4. Partial crude-balance diagnostic: production+imports−exports−refinery input equals-276thousand barrels/day, or-1.932million barrels over7days. Commercial plus SPR stocks instead rose2.564million barrels. The4.496million-barrel residual identifies omitted adjustments/transfers/other accounting components; it is not an unexplained physical shortage. A complete official balance table and definitions are required before causal attribution.
5. Supply disruption, seasonality and revisions: a commercial crude build of2.969million barrels weakens a simple across-the-board crude depletion narrative for that old source week, but cannot refute regional disruption or identify its cause. Seasonal comparators and source revisions are retained; missing independent operational evidence leaves competing explanations inconclusive.
6. Weather and price controls: no valid time/geography/exposure match was established to the weather report’s September21–25 samples, and no price/margin/outage outcome was collected. No weather adjustment, inflation/growth effect, demand elasticity or market return is estimated.

## Verdict and decisive evidence
The stored September18 statistics are reproduced and usable as explicitly lagged context. They do not establish a current shortage, demand shock or trading signal. The next decisive evidence is the missing later source period, complete compatible petroleum balance components and independent operational/exposure controls. No evidence or cooldown was reset to force a positive outcome.

## Sources and reproducibility
[EIA weekly petroleum statistics](https://www.eia.gov/petroleum/supply/weekly/), [commercial crude history](https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=WCESTUS1&f=W) and [gasoline-stock history](https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=WGTSTUS1&f=W) identify the original publisher. The package includes all12 series URLs, raw hashes, exact observed vintages, failed/successful capture metadata, baseline values, raw-cell verification and independent arithmetic. Scientific workflow/code: energy@28ea17c51a61f97e17aea6a4ac044a19a434fd98. No frozen report or forecast is overwritten.

## Packaging correction, version2
This one-off manual test report replaces an unpublished frozen draft identified by SHA-256 62d08baca4cdb0c4a61860d14589b7be55cea3453e5d7befe27f47feb673e554. The correction supplies the manual-test envelope classification and preserves all scientific results, source dates and evidence cutoffs. No new investigation or source acquisition occurred.
