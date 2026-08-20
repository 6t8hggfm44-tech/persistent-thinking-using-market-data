# Causal Graph

This is a human-readable causal map. Arrows are hypotheses, not facts.

```text
growth ──> earnings ──> equity cash-flow expectations ──> equity prices
   │
   └──> labor demand ──> hiring flow ──> income / consumer demand ──> real activity / growth
             │              │
             │              └──> re-employment speed / continued-claims duration
             └──> separation / layoff flow ──> initial jobless claims

income / consumer demand ──> earnings / cash-flow expectations ──> equity prices
income / consumer demand ──> inflation pressure ──> expected policy path ──> discount rates ──> equity prices

weak labor demand ──> expected policy path ──> short/intermediate yields
weak consumer demand ──> expected policy path ──> yields

fiscal impulse ──> growth
fiscal impulse ──> Treasury issuance ──> duration supply / term premium ──> long yields ──> financial conditions
Treasury debt-management / liquidity-support buybacks ──> long-end liquidity & net duration absorption ──> term premium / long yields ──> financial conditions

AI / corporate capex financing ──> corporate bond issuance ──> private duration supply ──> long yields / financial conditions
AI / capex / defense demand ──> business-equipment & high-tech output ──> aggregate industrial production
household-demand weakness ──> consumer-goods / auto output
housing financial conditions ──> residential construction activity

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

## Composition-sensitive activity refinement added 2026-08-18

Aggregate industrial production is now treated explicitly as a **mixture of potentially opposing sector channels**, not a sufficient statistic for broad demand. July 2026 total IP rose 0.2% while consumer-goods output fell 0.4%, business-equipment output rose 0.8%, and high-tech/defense categories were strong; housing simultaneously weakened sharply.

This means an AI/capex/defense boom can keep aggregate industrial output positive while household-sensitive activity deteriorates. Conversely, weak consumer categories do not establish broad contraction if investment-linked production is expanding. H001/H002/H004 discrimination should therefore use the aggregate jointly with sector composition, housing, labor, credit, and earnings breadth. This is a direct market application of the existing Universal ambiguous-endpoint safeguard rather than a new causal law.

## Treasury debt-management / liquidity-support refinement added 2026-08-19

Treasury's Aug. 19 announcement that long-duration nominal-coupon liquidity-support buybacks will rise from $2 billion to at least $4 billion per operation adds an explicit **policy/liquidity pathway into the long end of the curve**. Treasury's official CMT curve then fell from 4.71% to 4.65% at 10 years and from 5.28% to 5.19% at 30 years between Aug. 18 and Aug. 19.

The timing is consistent with the announcement affecting long-end liquidity and net duration absorption, but it does not identify the buyback as the sole cause of the yield move. This refinement therefore weakens any inference that a long-yield change uniquely reveals growth, inflation, fiscal supply, or private-duration pressure. Future rate interpretation should jointly inspect policy expectations, inflation compensation/commodity pressure, issuance, debt-management actions, and growth/credit evidence where available.

This is an application of Universal UL-0004 / FM-006, not a claim that Treasury can permanently set long yields or that the Aug. 19 intervention proves market stress.

## Labor-flow asymmetry refinement added 2026-08-20

Initial jobless claims are now treated specifically as a **separation/layoff-flow indicator**, not as a sufficient statistic for total labor demand. P000017 prospectively tested whether prior household/housing weakness had already transmitted into layoffs; the event failed at 206,000 claims. At the same time, continued claims rose to 1.799 million and contemporary labor commentary characterized the environment as low-hire/low-fire.

The model therefore separates at least two labor-demand pathways: weaker demand can first reduce hiring and slow re-employment while layoffs remain low, or it can progress into rising separations/initial claims. Low initial claims should reduce H002's **immediate layoff-transmission** probability but should not erase a slowdown hypothesis if hiring, continued claims, payroll breadth, vacancies, or household demand weaken. Conversely, a later synchronized rise in initial claims plus credit stress would be much stronger H002 evidence than low hiring alone.

This is an application of Universal UL-0004 / FM-006: one labor endpoint can be generated by only part of the causal mechanism. It is not submitted as a new Universal transfer candidate.

Every material edge should eventually carry sign, expected lag, confidence, evidence, and known failure conditions.
