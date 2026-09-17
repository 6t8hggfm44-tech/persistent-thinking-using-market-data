# Agriculture and food — weekly evidence-gap report (version 2)

## Summary

**Administrative correction:** this version uses the live receiver registry’s agriculture-specific run ID. Evidence, tests, cutoff, and verdict are unchanged from the preserved private predecessor.

**Verdict: inconclusive evidence gap, not a finding of no agricultural stress.** The September 17 occurrence passed the prospective cloud-start gate and was durably claimed. The available cloud checkpoint contained two prior capture identities, but not their source bytes. The one permitted collector pass attempted the two due sources—U.S. Drought Monitor and USDA APHIS HPAI—and both failed at DNS resolution. A policy-governed search-tool recovery returned no relevant official result.

**OBSERVATION:** zero usable numerical observations were available by the evidence cutoff. **INFERENCE:** none of the four registered domain hypotheses could be discriminated. **ASSUMPTION:** the access failures concern this runtime path and do not imply publisher unavailability. No market-direction signal is warranted.

## Coverage

Requested occurrence: September 17, 2026. Evidence window: September 10–17, 2026. Geography: United States, subject to source-specific coverage.

The audit covered crop progress/condition/yield, drought exposure, commodity balances, fertilizer constraints, livestock inventories/output, food inventories, exports, and HPAI. Four enabled source routes were reviewed. Two prior landing-page captures had preserved identities but missing bodies; two due routes were attempted and produced no body. The FAS export-sales route remained disabled. Fertilizer quantities and realized shipment histories were not enabled measurements.

## Hypotheses and tests

1. **Crop-weather:** adverse stage-specific weather could reduce condition or yield; seasonality, geography, and survey revisions are alternatives. Test blocked because drought exposure, fixed crop weights/stages, and a compatible outcome were unavailable.
2. **Commodity balance:** production loss could tighten ending stocks; demand and bookkeeping revisions are alternatives. Test blocked because comparable dated WASDE component tables were unavailable.
3. **Livestock disease:** confirmed disease plus removals could reduce output; surveillance intensity, seasonality, feed costs, and herd cycles are alternatives. Test blocked because detections/removals and compatible output data were unavailable.
4. **Fertilizer/trade:** an input or shipment constraint could reduce production or delivery; general costs, currency, profitability, and timing are alternatives. Test blocked because aligned price/quantity and shipment data were unavailable.

No blocked test was relabeled as completed. No values were inferred from navigation pages, hashes, search noise, or failed requests.

## Limitations

- Hashes prove identity, not byte availability or source meaning.
- The bounded collector recorded two temporary DNS name-resolution failures and no response bodies.
- The authorized search recovery produced no relevant official evidence; the incident recovery allowance was then exhausted.
- No acreage-weighted drought exposure, crop-stage match, balance decomposition, livestock exposure/output comparison, fertilizer quantity test, or export shipment test could be calculated.
- WASDE, NASS, APHIS, and drought data share or synthesize upstream observations; later analysis must avoid treating them as independent confirmations.
- This report cannot distinguish stability from unobserved change.

## Sources

- USDA WASDE landing-page capture identity, retrieved September 15, 2026; raw bytes unavailable in this runtime.
- USDA NASS publications-index capture identity, retrieved September 15, 2026; raw bytes unavailable in this runtime.
- U.S. Drought Monitor current page, attempted September 17, 2026; DNS failure, no body.
- USDA APHIS HPAI hub, attempted September 17, 2026; DNS failure, no body.

Exact source identities, attempt timestamps, ancestry, hashes where available, and integrity limits are recorded in `source-register.json`.

## Next decisive evidence

At the next normally eligible occurrence—and only after the preserved September 24 source cooldowns—restore verified bytes or obtain dated official tables sufficient for one registered test. The highest-value minimum package is either (a) a dated crop-stage exposure plus compatible NASS outcome and fixed acreage weights, or (b) two compatible WASDE balance vintages with production, use, and ending stocks. For livestock disease, require deduplicated removals and an output series; for fertilizer/trade, require quantities and realized shipments. Do not replay this run’s collector pass.

