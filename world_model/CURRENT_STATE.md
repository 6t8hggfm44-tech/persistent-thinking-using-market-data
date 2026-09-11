# Current Market State

**Model version:** 0.2.14  
**Status:** Friday Sep. 11 post-CPI / post-close cycle completed; P000023 resolved TRUE; no structural or hypothesis-weight change; no new forecast added  
**Evidence cutoff:** 2026-09-11T17:11:19-04:00

## Auditor

Forecast resolution occurred before post-outcome evidence intake or model interpretation.

- **P000023 — August core CPI:** the first BLS release reported **+0.3% m/m**, so the frozen `p(core CPI >=0.3)=0.54` event resolved **TRUE exactly at the threshold**. Brier **0.2116**, log loss **0.616186**. The 0.3% point had **0.0 pp** absolute error, beating the frozen July no-change 0.2% point (**0.1 pp error**) and frozen June-July mean 0.1% point (**0.2 pp error**). The 0.1%-0.4% 80% interval covered. Reuters later reported an economist consensus of 0.2%, but no stable timestamped consensus had been frozen at P000023's Aug. 28 cutoff, so it is not retrofitted as a benchmark.

Lifetime probability scoring is now **n=21**, mean Brier **0.213919**, mean log loss **0.617880**. Descriptive skill versus neutral 0.50 is **+0.1443** on Brier and **+0.1086** on log loss. The precommitted 30-resolution threshold remains unmet, so **learning cannot yet be assessed**. Strict record-level 80% interval coverage is **20/22 = 90.91%**; cross-target interval widths remain incomparable in raw units.

## New observations — first available after 2026-09-10T17:41:18-04:00

- **OBSERVATION:** BLS reported August headline CPI **+0.4% m/m and +3.4% y/y**; CPI excluding food and energy rose **+0.3% m/m and +2.4% y/y**. Energy rose 2.1%, gasoline 3.9%, shelter 0.3%, and services less energy services 0.3%.
- **OBSERVATION:** Preliminary September University of Michigan consumer sentiment fell to **47.8** from 51.7; Current Conditions were 50.9 and Expectations 45.8. Reuters reported one-year inflation expectations at **4.6%** and five-year expectations at **3.4%**.
- **OBSERVATION:** Brent settled **$104.61/bbl** and WTI **$100.05/bbl**, down on Friday but still up more than 8% over the week amid Middle East supply disruption and refined-product stress.
- **OBSERVATION:** The S&P 500 closed **0.86% higher at 7,656.98**; Reuters reported market-implied probability of a Sep. 16 Fed hike at nearly **90%**, up from 72% Thursday. The 10-year Treasury yield briefly approached 5% intraday.

## Inference

P000023 supplies modest positive prospective evidence for H003 relative to H001 because the precommitted core-inflation event occurred. The strength of that evidence is limited: the realization was exactly the threshold, core y/y inflation eased to 2.4%, and the forecast itself was only 54%. The headline acceleration was substantially energy-linked.

The September energy shock and higher household inflation expectations keep H003's forward inflation/policy-constraint pathway active. The same shock can reduce real household income and margins, while consumer sentiment and expectations weakened sharply, preserving an H002 delayed-downturn tail. Market rate probabilities, yields, and equities are treated as downstream belief/endpoints rather than independent confirmations of a causal mechanism.

## Hypothesis weights

- **H001 Soft landing: 0.35** (unchanged)
- **H002 Late-cycle recession: 0.15** (unchanged)
- **H003 Fiscal/inflation regime: 0.38** (unchanged)
- **H004 Productivity boom: 0.12** (unchanged)

No reweighting is made. H003 remains the narrow leader. The core CPI discriminator resolved in its direction, but only at the boundary and without hitting the precommitted >=0.5% strong-persistence surprise. A one-percentage-point weight move would imply more precision than the event supplies given the simultaneous energy/demand channels and shared ancestry of today's market reactions. P000027 now provides the cleaner next direct test of the policy-reaction mapping.

## Skeptic

**Attack on leading H003:** Core CPI was 0.3% rather than a large upside surprise and core y/y eased to 2.4%. Headline inflation was energy-heavy. Consumer sentiment fell to 47.8 and expectations to 45.8. Oil fell on Friday despite remaining above $100. High energy and near-5% long yields can create a contractionary real-income/financial-conditions shock. Nearly 90% market-implied hike odds are an investor belief, not Fed action.

**Response:** H003 remains narrowly plausible because core CPI stopped short of the benign recent-trend baseline, the energy shock remains severe, household inflation expectations rose, labor remains resilient, and policy pricing tightened. But these observations are causally related and do not justify counting multiple downstream endpoints as independent confirmations.

**What would surprise the current model:** a Sep. 16 Fed decision that does not raise the target range would directly challenge the current policy-constraint mapping represented by P000027; conversely, a hike would support that mapping but still require separate evaluation of later growth consequences. A later combination of persistent energy stress, widening credit, and rising layoffs would materially strengthen H002.

## Friday learning review — final post-close update

Across **21** resolved probability forecasts, mean Brier is **0.213919** and mean log loss **0.617880**. A fixed neutral-0.50 comparator has Brier 0.25 and log loss ln(2), giving descriptive skill of **+14.43%** and **+10.86%**, respectively. Market Repo B must treat these as descriptive because targets are heterogeneous and partly dependent.

The **first 10** probability forecasts average Brier **0.214740** / log loss **0.621654**; the **last 10** average **0.210480 / 0.608561**. The later window is numerically better, but the difference is small relative to descriptive bootstrap uncertainty and the target/horizon mix differs. The latest six are **0.175967 / 0.536558** versus earliest-six **0.227400 / 0.647876**, but six-forecast windows have already reversed direction in prior reviews.

The three probability forecasts resolved since the Sep. 4 weekly review average Brier **0.241367** and log loss **0.675864**, only modestly better than neutral. They include a one-month S&P miss, a PPI threshold success whose point merely tied frozen consensus, and today's CPI threshold success. This mixed composition is not a stable learning signal.

Calibration remains sparse: mean assigned probability is **47.57%** versus **38.10%** realized event frequency (8/21). Mean probability is **52.75%** on realized events versus **44.38%** on non-events, descriptively consistent with some discrimination. Counts remain too small and heterogeneous for recalibration.

Strict 80% interval coverage is **20/22 = 90.91%**, above nominal. That may reflect conservative intervals; raw widths cannot be pooled across incompatible units, so no sharpness-improvement claim is made. S&P point performance remains negative versus matched no-change after P000003: seven resolved S&P points have model MAE **47.896** versus **46.266** for no-change, descriptive skill **-3.52%**.

**Learning conclusion:** **insufficient evidence to assess learning at n=21**. Auditable self-correction and error preservation are present, but sustained longitudinal out-of-sample predictive improvement is not demonstrated. The universal longitudinal-learning safeguard remains applicable: process sophistication and favorable short windows are not outcome learning.

## Model-change attribution

- **v0.2.8 regional-to-national manufacturing safeguard:** P000024 remains one positive direct post-change test; n=1 is insufficient for learning credit.
- **v0.2.13 inflation/policy discriminator:** P000023 is one modest positive prospective test for the H003-vs-H001 inflation-state question. It resolved at the exact threshold rather than a strong surprise, so it receives positive evidence but not broad causal-learning credit.
- **v0.2.14 labor measurement bridge:** no later monthly payroll forecast generated under this revision has resolved. Claims data do not validate the net-payroll bridge. Learning credit remains zero.
- **Treasury announcement/realized-flow distinction:** current yield behavior remains multiply caused; no isolated prospective causal score exists. No learning credit.

No identified model change yet shows repeated benchmark-relative improvement in the forecasts it was intended to improve.

## Material model changes

**None.** Model v0.2.14 remains current. No causal-graph edge or measurement bridge is altered and hypothesis weights are unchanged. No new Universal transfer candidate is added; today's lessons are already covered by existing Universal guidance on longitudinal OOS learning, benchmark attribution, endpoint ambiguity, and shared causal ancestry.

## Open forecasts

- **P000027:** 58% probability the FOMC raises both bounds by at least 25 bp at the Sep. 15-16 meeting; frozen at the Sep. 4 cutoff. Today's near-90% market pricing is evidence, not a forecast rewrite.
- **P000004:** three-month S&P distribution, resolving Nov. 9 close; frozen Aug. 8.
- **P000005:** one-year S&P distribution, resolving Aug. 9, 2027 close; frozen Aug. 8.

## New forecast

**None.** P000027 is already a frozen, falsifiable policy-reaction test only days away. Issuing another FOMC/rates forecast after CPI would be highly correlated with it and would inflate nominal sample size rather than add independent discrimination. No unrelated target has enough information value at this cutoff to justify manufacturing activity.

## Most important watch

**The Sep. 16 FOMC decision resolving P000027.** It is now the highest-information frozen test of whether the model's inflation/policy-constraint state maps into actual policy action rather than merely market repricing.
