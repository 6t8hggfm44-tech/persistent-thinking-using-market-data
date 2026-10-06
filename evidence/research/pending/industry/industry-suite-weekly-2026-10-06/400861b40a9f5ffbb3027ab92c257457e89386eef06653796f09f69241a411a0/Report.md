# Industry — weekly investigation, October 6, 2026

## Summary

**Final verdict:** **retained aggregate output still does not show persistent broad contraction, while nominal global semiconductor sales accelerated sharply; neither result establishes a broad physical-demand boom, and an aggregate capacity constraint is not supported.**

This exploratory investigation reused integrity-verified G.17 evidence covering March-August 2026 and acquired one bounded representation of the SIA market-data page. The SIA summary reports July global semiconductor sales of **$146.8 billion**, up **6.4% month over month** and **135.1% year over year**. However, the June comparator is **$137.9 billion** in the September 4 summary versus **$134.5 billion** in the August 6 summary, a **$3.4 billion (2.53%)** cross-release difference. That makes release-vintage control material. Nominal sales do not measure physical units, fabrication geography or final demand.

The earlier G.17 pattern is unchanged: June-August means exceed March-May by **0.4428%** for manufacturing and **0.6517%** for total industry. August utilization remains **2.5 percentage points** below the manufacturing 1972-2025 mean and **3.1 points** below the total-industry mean. Census M3 remains unavailable because an earlier reservation is unresolved and was not replayed.

## Coverage

| Indicator | Actual coverage |
|---|---|
| Industrial and manufacturing production | Six monthly G.17 aggregate index levels, March-August 2026, current release vintage retained September 22 and rechecked September 30 |
| Capacity utilization | Six monthly rates per aggregate plus published 1972-2025 means; implied capacity is algebra only |
| Semiconductor sales | Ten reviewed cells from SIA/WSTS release summaries: May-July 2026 and 2026-Q2, global nominal USD |
| Orders, shipments, inventories, unfilled orders | Unmeasured; unresolved Census reservation preserved |
| PMI breadth | Unmeasured; no eligible numeric cells |
| Cement and other physical materials | Unmeasured; no reviewed physical-quantity table |
| Frequency/geography | Monthly U.S. aggregates plus monthly/quarterly global semiconductor sales; no weekly interpolation |

The frozen input set uses 26 G.17 cells and 10 SIA cells. Full connected-tool output remained runtime-local; retained records contain only reviewed limited cells and context.

## Hypotheses and tests

### H1 — Persistent aggregate contraction

**OBSERVATION:** Manufacturing averaged 97.8667 in March-May and 98.3000 in June-August, a **0.4428%** increase. Total industry rose from 102.3000 to 102.9667, or **0.6517%**. A March-April versus July-August sensitivity remained positive at **0.5627%** and **0.8811%**, respectively. Manufacturing fell **0.2033%** from July to August.

**INFERENCE:** Persistent broad contraction is weakened in the retained window. The August manufacturing decline is a soft patch, not enough to overturn the multi-month comparisons.

**ASSUMPTION:** The current-vintage aggregate construction is adequate for this narrow descriptive question. It is not adequate to identify sector breadth or demand causation.

**Verdict:** **weakened**.

### H2 — Binding physical capacity

**OBSERVATION:** From March to August, manufacturing output rose **0.8214%** while its algebraic capacity proxy rose **0.4218%**; utilization increased **0.3 point**. Total output rose **1.3766%**, implied capacity **0.4465%**, and utilization **0.7 point**. August utilization remained **2.5 points** and **3.1 points** below the published manufacturing and total-industry long-run means.

**INFERENCE:** Output rose faster than implied capacity, but aggregate utilization was not unusually high. Without independent downtime, order-book, lead-time, price or plant evidence, a binding capacity constraint is not supported.

**Verdict:** **not supported**.

### H3 — Semiconductor demand signal

**OBSERVATION:** The September 4 SIA summary reports July global sales of **$146.8 billion** versus **$137.9 billion** in June. Exact arithmetic gives **6.4540%**, consistent with the displayed **6.4%** after rounding. The displayed year-over-year rate is **135.1%**. Yet the prior August 6 summary lists June sales as **$134.5 billion**, so consecutive summaries differ by **$3.4 billion**, or **2.5279%** relative to the earlier value.

**INFERENCE:** Nominal semiconductor revenue accelerated strongly, but the cross-release difference means a fixed-vintage panel is unavailable from these summaries. The evidence supports a nominal-sales observation, not a claim about chip units, U.S. fabrication, broad manufacturing output or final demand.

**SPECULATION:** AI-related mix, memory pricing, exchange rates or channel inventory could contribute, but the retained evidence cannot discriminate among them.

**Verdict:** **nominal acceleration observed; physical-demand claim inconclusive**.

### H4 — Orders, inventories and breadth

**RESULT:** **blocked/untested.** Census M3 remains unresolved, and no eligible ISM or USGS physical-quantity evidence was acquired. Missing data are not negative findings. One SIA/WSTS lineage cannot establish broad industrial breadth.

## Reproducibility and evidence discipline

Decimal calculations used exact retained strings. Independent Fraction arithmetic reproduced the central comparisons: **325/734%** for manufacturing, **2000/3069%** for total industry and **8900/1379%** for July versus the later June semiconductor comparator. SIA and WSTS count as one lineage; repeated G.17 calculations add no evidence weight. Findings were frozen before any other domain report was read, so no cross-domain reconciliation altered the independent Industry conclusion.

## Limitations

- The G.17 panel has six aggregate months, below the desired 36-month and sector-level baseline.
- No year-ago, motor-vehicles-excluded, workday, strike, weather or historical-release-vintage sensitivity was feasible.
- SIA data are nominal global sales. Units, price/mix, currency, inventories, end markets and fabrication geography are absent.
- The two June SIA values demonstrate material release-vintage sensitivity; neither is silently preferred as the unique historical value.
- Census M3 was not repeated because its prior reservation remains unresolved. ISM and USGS remained unmeasured in this pass.
- Tool-extract hashes identify reviewed representations, not original publisher-body bytes or hidden upstream request totals.
- Prior Industry findings were visible, so this is exploratory continuation, not blinded independent replication.

## Sources

- [Federal Reserve G.17 Industrial Production and Capacity Utilization](https://www.federalreserve.gov/releases/g17/current/default.htm) — reviewed retained cells for March-August 2026; September 18 release vintage.
- [Semiconductor Industry Association market data](https://www.semiconductors.org/policies/tax/market-data/) — dated release summaries for May-July 2026 and 2026-Q2; SIA/WSTS is one lineage.
- [Census Manufacturers’ Shipments, Inventories, and Orders](https://www.census.gov/manufacturing/m3/index.html) — unavailable numeric evidence; not used.
- [ISM Manufacturing PMI reports](https://www.ismworld.org/supply-management-news-and-reports/reports/ism-pmi-reports/) — unavailable numeric evidence; not used.
- [USGS Cement Statistics and Information](https://www.usgs.gov/centers/national-minerals-information-center/cement-statistics-and-information) — unavailable physical-quantity evidence; not used.

## Changes from prior eligible Industry work

The G.17 output and capacity conclusions reproduce the prior retained-evidence result and add no independent evidence. This report adds current SIA/WSTS nominal sales evidence and a cross-release-vintage sensitivity. It does not supersede earlier reports.

## Next decisive evidence

A dated, compatible M3 orders/shipments/inventories panel and a longer G.17 sector history would address demand and breadth. Semiconductor interpretation needs nonoverlapping fixed-vintage periods plus unit shipments, price/mix, inventories and end-market context. Materials breadth requires physical quantities from independently sourced cement, steel, chemicals or machine tools. These gaps create no retry schedule or additional authority.
