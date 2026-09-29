# Industry — weekly investigation, September 29, 2026

## Summary

**Final verdict:** **retained aggregate output does not show persistent broad contraction; a physical capacity constraint is not supported; demand and sector breadth remain inconclusive.**

This bounded investigation reused the exact reviewed G.17 cells first retained on September 22 from the Federal Reserve release published September 18. No publisher source was called in this run. The current runtime lacked the old raw bodies, but the prior frozen package and the limited reviewed extract passed integrity verification. The live access policy selected that verified reuse over a redundant network request. Consequently, every numerical conclusion below concerns the retained March–August 2026 release vintage; it is not a September 29 measurement or a claim of current publisher availability.

Two exploratory tests were executed after the plan was frozen: a three-month output persistence comparison with shorter-window sensitivity, and an endpoint production/utilization identity decomposition. Prior Industry results had already been inspected, so this work is exploratory and repetition or extension of one release, not independent confirmation.

## Coverage

| Requested indicator | Actual coverage |
|---|---|
| Industrial and manufacturing production | **Measured narrowly:** six retained monthly G.17 aggregate index levels, March–August 2026 |
| Capacity and utilization | **Partial:** six utilization rates per aggregate, two historical means, and an algebraic endpoint capacity proxy |
| Factory orders, shipments, inventories and unfilled orders | **Unmeasured:** no eligible M3 numerical cells; a prior same-source acquisition remains unresolved and was not replayed |
| Durable and core capital goods | **Unmeasured** |
| Manufacturing PMIs and components | **Unmeasured:** no eligible retained PMI cells |
| Semiconductors | **Unmeasured:** no eligible SIA/WSTS cells and no unit/price/end-use controls |
| Steel, cement, chemicals and machine tools | **Unmeasured or unimplemented:** no independent physical-sector cells |
| Geography and frequency | United States industrial aggregates; monthly data, not weekly observations |
| Source vintage | G.17 published September 18, retained September 22; original publisher-body bytes unavailable in this runtime |

The source window contains 26 retained numeric cells: six monthly total-industry production levels, six manufacturing production levels, six total-industry utilization rates, six manufacturing utilization rates, and two 1972–2025 utilization means.

## Hypotheses and tests

### H1 — Persistent aggregate contraction

**Competing hypotheses**

- Broad industrial demand or activity was contracting persistently.
- A one-month movement reflected timing, composition, disruption, rounding or revision rather than a persistent decline.
- Aggregate production was stable or rising while narrower sectors weakened.

**Predeclared discriminator**

If persistent contraction characterized the retained window, the June–August mean would be below March–May for both manufacturing and total industry. A reasonable shorter-window comparison should not reverse that result. A July–August decline by itself is insufficient.

**OBSERVATION:** Manufacturing averaged 97.8667 in March–May and 98.3000 in June–August, an increase of **0.4428%**. Total industry averaged 102.3000 and 102.9667, an increase of **0.6517%**. An edge sensitivity comparing March–April with July–August was also positive: **0.5627%** for manufacturing and **0.8811%** for total industry. Manufacturing declined **0.2033%** from July to August, while total industry rose **0.0971%**.

**INFERENCE:** The retained aggregate window weakens a persistent broad-contraction interpretation. The August manufacturing dip is real within the rounded retained cells, but it does not overturn the three-month or two-month comparisons.

**LIMIT:** Six aggregate months cannot establish sector breadth, persistence over a business cycle, or demand causation. There is no 36-month baseline, year-ago matched window, motor-vehicles exclusion, workday control or sector panel. The publisher’s unrounded change calculations may differ from arithmetic on displayed rounded levels.

**Verdict:** **persistent aggregate contraction weakened**.

### H2 — Tight physical capacity

**Competing hypotheses**

- Production was approaching a constrained capacity base.
- Output rose while capacity also expanded, producing only modest utilization movement.
- Benchmark revisions or sector composition affected the ratio.
- Individual industries faced bottlenecks even though aggregate utilization remained moderate.

**Predeclared discriminator**

Use the same-release identity (U=P/C) to separate endpoint log changes in production, an implied capacity proxy and utilization. A strong physical-constraint claim would additionally require utilization near an appropriate historical range and independent downtime, order-book, lead-time, price or plant evidence.

**OBSERVATION:** From March to August, manufacturing production rose about **0.8180% in logs**. Its algebraically implied capacity proxy rose about **0.4209%**, leaving a **0.3971%** log rise in utilization, or **0.3 percentage point** in the published rate. Total-industry production rose **1.3672% in logs**, implied capacity rose **0.4455%**, and utilization rose **0.9217% in logs**, or **0.7 percentage point**.

August manufacturing utilization was **75.7%**, **2.5 percentage points below** its published 1972–2025 mean. Total-industry utilization was **76.3%**, **3.1 points below** its historical mean.

**INFERENCE:** Output rose faster than the derived capacity proxy, so utilization tightened modestly. But the available aggregate evidence does not support a physical bottleneck claim: utilization remained below its long-run mean and no independent constraint measure was available.

**LIMIT:** The capacity proxy is (P/U) calculated from retained rounded aggregates, not a separately published capacity series. This endpoint identity cannot identify plant closures, usable capacity, benchmark revisions or sector mix. It supplies arithmetic decomposition, not causal evidence.

**Verdict:** **physical capacity constraint not supported by the available aggregate evidence**.

### H3 — Demand, inventories and breadth

**Planned discriminator:** Match M3 orders, shipments, inventories and unfilled orders by compatible industry and price basis; then compare semiconductor and materials quantities with independent ancestry.

**RESULT:** **blocked/untested.** No eligible M3, ISM, SIA/WSTS, USGS cement, steel, chemical or machine-tool numerical cells were available. A prior Census acquisition remains unresolved, so it was not relabeled or retried. Missing observations are not negative findings.

**INFERENCE:** Aggregate G.17 output alone cannot determine whether demand weakened, inventories accumulated involuntarily, semiconductor demand accelerated, or physical-sector breadth improved.

## Reproducibility and checks

The primary calculation used Decimal arithmetic from the exact retained numeric strings. A separate Fraction calculation transcribed the source cells independently and reproduced the three-month changes exactly as rational values: **325/734%** for manufacturing and **2000/3069%** for total industry. Exact endpoint ratios independently verified the (P/U) identity. The small reported log residuals are floating-point conversion noise below (2	imes10^{-14}) percentage point.

All calculated series share the same G.17 representation and common upstream ancestry. They are not independent confirmations. Re-executing retained inputs adds analytical checks but no new evidence weight and no freshness.

## Interpretation for downstream use

**OBSERVATION:** The retained aggregate indexes rose on both primary and shorter-window comparisons, while manufacturing slipped slightly in August.

**INFERENCE:** A narrative of persistent broad U.S. industrial contraction is not supported by this narrow window. A description of modest aggregate expansion with a late manufacturing soft patch is closer to the measured evidence.

**ASSUMPTION:** Interpreting the retained aggregates as economically representative assumes their current-vintage construction and broad weights are appropriate for the question. The missing sector, orders and price controls make that assumption material.

**SPECULATION:** Demand composition, supply disruptions or investment cycles could explain sector divergence, but the present evidence cannot choose among them.

No market forecast, causal coefficient or calibrated recession probability is estimated. Market should treat this as one dated G.17 contribution and deduplicate it against any other report using the same release.

## Limitations

- No new source representation was acquired; the latest durable numerical evidence remains the September 18 G.17 release retained September 22.
- Original publisher-body bytes are unavailable here. The representation hash verifies the prior tool extract, and the frozen package verifies the retained selection, not original publisher-body identity.
- Six monthly observations per aggregate are below the method’s desired 36-month baseline.
- No year-ago, motor-vehicles-excluded, sector-breadth, price, workday, weather, strike or revision-vintage sensitivity.
- The capacity proxy is an algebraic derivative of rounded P and U, not independent capacity evidence.
- M3 orders/shipments/inventories, PMI components, semiconductor units/prices/end markets, and materials quantities are unavailable.
- No current cross-domain reports were consulted before freezing this Industry conclusion. Prior Industry work and its retained evidence were necessarily inspected, so the analysis is exploratory.
- Shared G.17 ancestry counts once regardless of how many calculations or reports cite it.

## Sources

- [Federal Reserve G.17 Industrial Production and Capacity Utilization](https://www.federalreserve.gov/releases/g17/current/default.htm) — retained reviewed extract covering March–August 2026 aggregate indexes and utilization, published September 18 and retrieved September 22. Original publisher-body bytes were not preserved in this runtime.
- [Census Manufacturers’ Shipments, Inventories, and Orders](https://www.census.gov/manufacturing/m3/index.html) — no eligible numerical cells; not used as evidence.
- [ISM Manufacturing PMI reports](https://www.ismworld.org/supply-management-news-and-reports/reports/ism-pmi-reports/) — no eligible numerical cells; not used as evidence.
- [Semiconductor Industry Association market data](https://www.semiconductors.org/policies/tax/market-data/) — no eligible numerical cells; not used as evidence.
- [USGS Cement Statistics and Information](https://www.usgs.gov/centers/national-minerals-information-center/cement-statistics-and-information) — no eligible numerical cells; not used as evidence.

## Changes from prior eligible Industry work

The central three-month output comparisons reproduce the prior retained-evidence finding and therefore add no independent evidence. This report adds a predeclared shorter-window sensitivity and an explicit March–August (P/U) endpoint decomposition. Those additions strengthen the arithmetic description but do not solve the missing demand, sector or bottleneck identification. No earlier report is superseded.

## Next decisive evidence

The most useful next evidence is a dated, compatible M3 panel for orders, shipments, inventories and unfilled orders; a longer G.17 sector history with motor vehicles excluded; separately published capacity levels or revision detail; and independent plant, price or lead-time evidence. Semiconductor conclusions require units, price/mix and end-market inventory context; materials breadth requires actual physical quantities. These needs create no retry schedule or new acquisition authority.

