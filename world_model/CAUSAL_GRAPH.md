# Causal Graph

This is a human-readable causal map. Arrows are hypotheses, not facts.

```text
growth ──> earnings ──> equity cash-flow expectations ──> equity prices
   │
   └──> labor ──> income / consumer demand ──> real activity / growth
                         │
                         ├──> earnings / cash-flow expectations ──> equity prices
                         └──> inflation pressure ──> expected policy path ──> discount rates ──> equity prices

weak labor ──> expected policy path ──> short/intermediate yields
weak consumer demand ──> expected policy path ──> yields

fiscal impulse ──> growth
fiscal impulse ──> Treasury issuance ──> duration supply / term premium ──> long yields ──> financial conditions

AI / corporate capex financing ──> corporate bond issuance ──> private duration supply ──> long yields / financial conditions

credit stress ──> financial conditions ──> growth
liquidity ──> risk appetite / valuation

geopolitical shocks ──> commodity prices ──> inflation expectations ──> long yields / policy constraint
commodity shocks ──> retail energy prices / input costs ──(lagged, state-dependent)──> measured inflation
commodity shocks ──> real household purchasing power / consumer demand
commodity shocks ──> margins

positioning ──> short-horizon price response
```

## State-dependent interaction added 2026-08-10

Weak labor does not imply falling long yields mechanically. The Aug. 10 evidence reinforced a competing path in which commodity/inflation risk and Treasury-supply/term-premium pressure can offset or dominate the easier-policy channel. This interaction should be tested prospectively rather than treated as proved from one session.

## Timing refinement added 2026-08-12

A spot commodity shock is not a contemporaneous one-for-one CPI shock. Pass-through depends on timing, retail gasoline/refining dynamics, inventories, substitution, and indirect input-cost transmission. July CPI showed falling monthly energy prices even though spot oil moved sharply higher in August. Therefore July CPI cannot be used retroactively as a clean falsification of an August oil-shock channel; the channel must be tested prospectively in later price data and market inflation expectations.

## Opposing-channel consumer-demand refinement added 2026-08-14

A negative consumer-demand shock can affect equities through **opposing causal channels**. Weaker demand can lower expected earnings/cash flows, which is equity-negative, while also lowering the expected policy path and discount rates, which can be equity-positive. The Aug. 14 combination of unexpectedly weak retail/control-group sales, lower Treasury yields, and only a modest S&P decline illustrates why index price alone cannot identify the dominant growth mechanism. Future model discrimination should prefer joint observations across growth, yields, credit, labor, and earnings breadth rather than inferring macro strength directly from a resilient index.

Retail sales are nominal, goods-heavy, revision-prone, and sensitive to timing effects; the demand node therefore should be updated from repeated evidence rather than one release.

## Private-duration supply refinement added 2026-08-17

The model now distinguishes **Treasury duration supply** from potentially material **private corporate duration supply**. On Aug. 17 the 10-year and 30-year Treasury yields rose despite recent soft demand data; Reuters reported market commentary attributing part of the long-end pressure to fiscal concerns and heavy AI-related corporate debt issuance. This motivates, but does not prove, a candidate path from large corporate capex-financing needs through bond issuance to duration supply and long yields.

This edge is **provisional and low-confidence**. A single session cannot identify the cause of a long-yield move. It should gain confidence only if periods of unusually heavy corporate duration issuance repeatedly coincide with long-end pressure after controlling qualitatively for growth, inflation, Treasury supply, and policy expectations. It should be weakened or removed if future long-end behavior does not differ when private issuance pressure changes.

Every material edge should eventually carry sign, expected lag, confidence, evidence, and known failure conditions.
