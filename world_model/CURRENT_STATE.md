# Current Market State

**Model version:** 0.2.14  
**Status:** Friday Sep. 11 weekly review run before the 08:30 ET CPI release; P000028 resolved; no hypothesis-weight or causal-graph change; no new forecast added  
**Evidence cutoff:** 2026-09-10T17:41:18-04:00

## Auditor

Forecast resolution occurred before post-outcome model interpretation.

- **P000028 — August final-demand PPI:** the first BLS release reported **+0.4% m/m**, so the frozen `p(PPI>=0.4)=0.53` event resolved **TRUE**. Brier **0.2209**, log loss **0.634878**. The 0.4% point had **0.0 pp** absolute error, exactly tying the frozen 0.4% external consensus and beating the frozen 0.0% no-change point. The -0.2%-0.9% 80% interval covered. Because the point merely matched consensus, the result does not establish point information beyond consensus.

Lifetime probability scoring is now **n=20**, mean Brier **0.214035**, mean log loss **0.617965**. Descriptive skill versus neutral 0.50 is **+0.1439** on Brier and **+0.1085** on log loss. The precommitted 30-resolution threshold remains unmet, so **learning cannot yet be assessed**. Strict record-level 80% interval coverage is **19/21 = 90.48%**; cross-target widths remain incomparable in raw units.

## New observations — first available after 2026-09-09T17:17:44-04:00

- **OBSERVATION:** BLS reported August final-demand PPI **+0.4% m/m and +5.4% y/y**. Final-demand goods rose 1.1%, services 0.1%, and final demand less foods, energy, and trade services 0.3%. More than three-fourths of the goods increase was attributable to a 4.2% rise in energy.
- **OBSERVATION:** Initial unemployment claims for the week ended Sep. 5 were **206,000**; continuing claims for the week ended Aug. 29 were **1.774 million**.
- **OBSERVATION:** August existing-home sales fell **2.0%** to a **3.98 million** annualized rate, a 14-month low, while inventory rose to 4.9 months of supply.
- **OBSERVATION:** Treasury's enlarged long-end liquidity-support buyback program entered its realized-operation phase. Long yields nevertheless rose on Sep. 10; Reuters reported the 10-year at its highest in nearly three years and the 30-year at its highest in more than 19 years.
- **OBSERVATION:** Brent settled **$107.63/bbl** and WTI **$102.48/bbl**, each up about 6%, as tanker attacks and Middle East supply disruption intensified.
- **OBSERVATION:** The S&P 500 closed **0.58% lower at 7,591.75**; Reuters reported market-implied probability of a September Fed hike near **70%**, up from about 64% before the PPI release.

## Inference

The post-cutoff state remains split rather than uniformly inflationary or recessionary. Low claims reinforce the low-separation branch and argue against immediate generalized contraction; weak existing-home sales preserve the delayed household/housing downside. August PPI is firm but exactly consensus and materially energy-driven, so it does not identify broad core-price persistence by itself.

The September oil escalation and higher long yields strengthen H003's **forward** input-cost/policy-constraint pathway. The same energy shock can also weaken real household demand and margins, preserving an H002 tail. September energy information is not leaked backward into P000023's August core-CPI forecast.

The realized buyback operation does not receive causal credit or blame from one day's yield movement because simultaneous PPI, oil, policy expectations, deficits, auctions, and duration supply remain credible causes. The existing announcement-versus-flow distinction remains adequate.

## Hypothesis weights

- **H001 Soft landing: 0.35** (unchanged)
- **H002 Late-cycle recession: 0.15** (unchanged)
- **H003 Fiscal/inflation regime: 0.38** (unchanged)
- **H004 Productivity boom: 0.12** (unchanged)

No reweighting is made. H003 remains the narrow leader, but its strongest new support comes from a joint energy/rates/policy-constraint state rather than P000028 alone. The precommitted core-CPI discriminator resolves within hours; moving weights aggressively before that result would overreact to vivid but composition-sensitive and downstream evidence.

## Skeptic

**Attack on leading H003:** P000028 merely matched consensus, its headline was energy-heavy, and services PPI rose only 0.1%. Existing-home sales remain weak. Oil above $100 can impose a negative real-income shock rather than create persistent core inflation. Low claims support labor resilience but do not prove strong hiring, consumption, or payroll growth. Rising Treasury yields and falling equities are downstream endpoints with multiple plausible causes.

**Response:** H003 remains narrowly plausible because resilient labor, a firm producer-price pipeline, severe energy disruption, elevated long yields, and higher hike pricing coexist. But the model does not promote this into stronger confidence without the frozen core-CPI test.

**What would surprise the current model:** first-release August core CPI <=0.1% m/m would materially strengthen H001's benign-disinflation path; >=0.5% would materially strengthen H003's underlying-inflation branch. A later combination of persistent energy stress, widening credit, and rising layoffs would strengthen H002.

## Friday learning review

The first 10 resolved probability forecasts average Brier **0.214740** / log loss **0.621654**; the last 10 average **0.213330 / 0.614277**. That is essentially flat. Descriptive iid-bootstrap uncertainty around last-minus-first easily includes both meaningful improvement and deterioration. Target/horizon composition also differs, so the comparison is not a clean causal estimate of learning.

The latest six remain numerically better than the earliest six (**0.187517 vs 0.227400 Brier**), but six-forecast windows have already changed direction across prior reviews. This remains unstable descriptive evidence.

S&P point performance versus matched no-change has deteriorated after P000003: seven resolved S&P points now have model MAE **47.896** versus **46.266** for no-change, descriptive skill **-0.0352**. The one-month Aug. 8 batch also produced multiple point/ranking benchmark losses. These failures are preserved rather than hidden by aggregate probability scores.

Calibration remains too sparse: mean assigned probability is **47.25%** versus **35.0%** realized event frequency, although mean p is higher for realized events (**52.57%**) than non-events (**44.38%**). Interval coverage is above nominal, but cross-target sharpness is not yet comparable and possible conservatism remains a live alternative explanation.

**Learning conclusion:** **insufficient evidence to assess learning at n=20**. The system is audibly self-correcting and preserving error, but sustained longitudinal out-of-sample improvement has not been demonstrated.

## Material model changes

**None.** Model v0.2.14 remains current. No causal-graph edge or measurement bridge is altered. No model-learning credit is assigned to the Sep. 10 claims data for the v0.2.14 payroll bridge because claims test separations, not monthly CES net payroll magnitude. No new Universal transfer candidate is added; the methodological issues are already represented in existing transfer candidates and Universal lessons.

## Open forecasts

- **P000023:** 54% probability first-release August core CPI is >=0.3% m/m on Sep. 11; point 0.3%, 80% interval 0.1%-0.4%; frozen at the Aug. 28 cutoff.
- **P000027:** 58% probability the FOMC raises both bounds by at least 25 bp at the Sep. 15-16 meeting; frozen at the Sep. 4 cutoff. Current market repricing is evidence, not a forecast rewrite.
- **P000004:** three-month S&P distribution, resolving Nov. 9 close; frozen Aug. 8.
- **P000005:** one-year S&P distribution, resolving Aug. 9, 2027 close; frozen Aug. 8.

## New forecast

**None.** P000023 resolves within hours and P000027 already tests the policy mapping after the inflation data. Adding another highly correlated inflation/rate forecast would inflate activity and nominal sample size without enough independent discriminating information.

## Most important watch

**First-release August core CPI at 08:30 ET on Sep. 11.** It remains the cleanest immediate discriminator between H001 benign disinflation and H003 persistent underlying inflation/policy constraint.
