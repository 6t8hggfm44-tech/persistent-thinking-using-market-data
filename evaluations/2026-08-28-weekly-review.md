# Weekly Learning Review — 2026-08-28

**Evidence cutoff:** 2026-08-28T18:07:44-04:00  
**Current model after review:** v0.2.13  
**Newly resolved since the prior Friday review:** 3 binary-probability components  
**Lifetime resolved binary-probability components:** 15

## 1. Auditor results this cycle

All outcomes were resolved before post-outcome evidence was used to revise the model. Original forecast content, thresholds, benchmarks and resolution rules remain unchanged.

- **P000021 — July core PCE:** p(core PCE m/m >=0.3)=0.36 resolved FALSE at **0.2%**. Brier **0.1296**; log loss **0.446287**; point error **0.0 pp**; interval hit. The point forecast exactly equaled the frozen published consensus, so the exact point result demonstrated **no information beyond consensus**.
- **P000020 — joint claims flow test:** p(initial <220k AND continuing >=1.800m)=0.57 resolved FALSE at **203k initial / 1.778m continuing**. Brier **0.3249**; log loss **0.843970**. Initial point error was 6k versus 3k no-change and 7k external-calendar; continuing point error was 34k versus 21k no-change and 33k external-calendar. Both component intervals covered. This was negative OOS evidence for the specific sticky-reemployment threshold formulation.
- **P000022 — Aug. 28 10-year Treasury:** p(10-year >=4.70)=0.47 resolved TRUE at **4.73%**. Brier **0.2809**; log loss **0.755023**. Point MAE **4 bp** versus **6 bp** no-change and **5 bp** one-day recent trend; interval hit. The binary probability lost to neutral even though the point forecast modestly beat both simple point baselines.

## 2. Lifetime proper scores and benchmark skill

Across all **15** resolved binary-probability components:

- Mean Brier: **0.229100**
- Mean log loss: **0.650410**
- Neutral-0.50 Brier comparator: **0.250000**
- Descriptive Brier skill vs neutral: **+0.0836**
- Neutral-0.50 log loss: **0.693147**
- Descriptive log-loss skill vs neutral: **+0.0617**

These targets are heterogeneous; the neutral comparison is a fixed descriptive comparator, not proof of transferable forecasting skill or an empirical base-rate benchmark.

### Recent OOS window versus prior history

The three resolutions since the Aug. 21 Friday review have:

- Mean Brier: **0.245133**
- Mean log loss: **0.681760**
- Descriptive Brier skill vs neutral: **+0.0195**
- Descriptive log-loss skill vs neutral: **+0.0164**

The prior twelve resolutions had mean Brier **0.225092** and mean log loss **0.642572**. Thus the newest three are **worse**, not better, on both proper scores. This does not establish deterioration either: n=3 is tiny and the targets changed. It does, however, directly rule out a convenient monotonic-learning story.

A simple vintage chronology is also non-monotonic:

- earliest 6 resolutions: Brier **0.227400**, log loss **0.647876**;
- next 6 resolutions: Brier **0.222783**, log loss **0.637268**;
- latest 3 resolutions: Brier **0.245133**, log loss **0.681760**.

The middle window looked better; the latest window gave back that apparent gain. Target mix, regime and small-sample luck remain plausible explanations throughout.

### S&P point forecasts

No additional S&P point forecast resolved this week, so the prior Friday comparison remains the current frozen summary across six resolved S&P point forecasts:

- mean model MAE **31.465 points**;
- mean matched no-change MAE **39.957 points**;
- descriptive MAE skill vs no-change **+0.2125**.

Across the four S&P forecasts with a frozen recent-trend benchmark:

- mean model MAE **43.730 points**;
- mean recent-trend MAE **58.823 points**;
- descriptive MAE skill **+0.2566**.

These are not new successes this week and receive no additional learning credit.

### Non-S&P benchmark results this week

- P000021: exact model point, but **tied consensus exactly**; no consensus-relative skill.
- P000020: both point estimates were within their 80% intervals, but initial claims lost to no-change and continuing claims lost to both no-change and the external point forecast.
- P000022: model point modestly beat both no-change and recent-trend rate baselines, while its binary probability lost to neutral.

The mixed benchmark record is more informative than simply counting correct event directions.

## 3. Calibration, coverage and sharpness

Across the 15 probability forecasts, mean assigned event probability is **0.4940** and observed event frequency is **6/15 = 0.4000**. The system has therefore assigned somewhat more event probability than the observed rate, but n=15 is far too small and heterogeneous for a meaningful calibration curve.

Coarse probability bins remain sparse:

| Probability bin | n | Mean forecast p | Event frequency |
|---|---:|---:|---:|
| 0.30–0.40 | 3 | 0.370 | 0/3 = 0.000 |
| 0.40–0.50 | 4 | 0.480 | 1/4 = 0.250 |
| 0.50–0.60 | 8 | 0.548 | 5/8 = 0.625 |

The low-probability bin has not yet produced an event, while the >0.50 bin has produced more events than its mean assigned probability. Counts are too small to justify probability recalibration.

**Interval coverage is now 13/13 = 100%** at the forecast-record level among resolved forecasts carrying intervals. If intervals were independently and exactly 80% calibrated, 13 consecutive hits would occur about **5.5%** of the time. Independence and homogeneous coverage do not hold here, so this is not a formal rejection test; it is a warning that intervals may be conservative. The system should not widen intervals to preserve a perfect record.

Sharpness has not obviously deteriorated this week: P000022's rate interval was 0.24 percentage point wide versus roughly 0.23 for earlier rate forecasts; P000021's core-PCE interval was 0.3 pp wide; P000020 used 31k initial-claims and 120k continuing-claims widths. The new P000023 core-CPI interval is 0.3 pp wide rather than being widened in response to the 13/13 coverage streak. Cross-unit widths are not pooled.

## 4. Error diagnosis and model-change audit

### v0.2.7 — labor-flow asymmetry / sticky-reemployment formulation
This is the clearest direct test of a recent model change. P000020 was designed specifically to test low initial claims with sticky continuing claims. The low-layoff leg held, but the >=1.800m continuing-claims leg failed at 1.778m; the forecast lost to neutral and its continuing-claims point lost both frozen point baselines. **The specific sticky-reemployment formulation worsened the next direct forecast and therefore receives negative performance evidence.**

The broader methodological split between layoffs and hiring/re-employment remains logically useful, but it is no longer allowed to infer a durable regime from one near-threshold continuing-claims observation. Future updates require persistence or corroboration from payroll breadth, vacancies, hiring, unemployment duration or similar measures.

### v0.2.8 — regional-to-national manufacturing safeguard
This change was created from P000019's regional-survey extrapolation failure. No later national-manufacturing forecast generated under the safeguard has resolved. It therefore has **zero predictive-learning credit** so far.

### v0.2.9 — Treasury timing/flow correction and P000021
The buyback correction separated announcement/expectations effects from realized purchase flow. Because enlarged purchases do not begin until Sept. 10, no pre-Sept. 10 yield outcome can validate the realized-flow mechanism. This correction improves causal hygiene but has **no predictive credit yet**.

P000021, generated under v0.2.9, had a good absolute probability score and an exact point forecast, but the point exactly matched consensus. The result is compatible with the model's restrained inflation probability; it is not evidence that v0.2.9 added information beyond the external baseline.

### v0.2.10 — repeated household/housing weakness
The Aug. 25 state increased H002 after another housing/sentiment confirmation. Subsequent claims moved in the opposite direction from the specific sticky-reemployment test and stronger private-demand evidence followed. This branch has not disappeared, but it did not improve the next direct labor forecast. No positive predictive credit is assigned.

### v0.2.11 — AI investment versus realized productivity
No productivity forecast has resolved under this refinement. The separation remains methodologically important, and Warsh's Aug. 28 speech independently framed AI productivity as an unresolved question, but **method agreement is not forecast skill**. Zero predictive credit.

### v0.2.12 — post-claims revision / P000022
P000022 was generated after the model reduced H002 and kept H003 narrowly leading. The realized 10-year rate at 4.73% was directionally compatible with the rate-pressure branch and the point estimate beat simple point benchmarks. But the forecast's 47% event probability lost to neutral. Because the target is multiply determined and because proper-score evidence was negative, v0.2.12 receives **mixed evidence, not improvement credit**.

## 5. Hypothesis-weight review

Weights at the prior Friday close and today:

| Hypothesis | Aug. 21 | Aug. 28 | Change |
|---|---:|---:|---:|
| H001 Soft landing | 0.34 | 0.34 | 0.00 |
| H002 Late-cycle recession | 0.19 | 0.18 | -0.01 |
| H003 Fiscal/inflation regime | 0.35 | 0.36 | +0.01 |
| H004 Productivity boom | 0.12 | 0.12 | 0.00 |

The small net change masks real intraweek movement: Aug. 24 was 0.34/0.20/0.34/0.12; Aug. 25 0.33/0.21/0.34/0.12; Aug. 26 0.33/0.20/0.35/0.12; Aug. 27 0.34/0.19/0.35/0.12; Aug. 28 0.34/0.18/0.36/0.12. The system is therefore not silently presenting today's weights as though the path were smooth.

H003's current lead comes primarily from the explicit price-focused reaction function and still-high underlying inflation, not from the week's oil path; oil actually moved against the immediate energy branch. H001 remains close because energy fell and medium-term inflation expectations remain anchored. H002 remains alive through household weakness and historically weak hiring, but current low layoffs and strong private demand prevent a larger weight. H004 is held fixed because investment inputs still do not establish realized productivity.

## 6. Is the system learning?

**Conclusion: no demonstrated learning; sample size n=15.** The protocol's precommitted threshold is 30 resolved forecasts before even a preliminary learning claim. We are only halfway there, and the outcomes are not independent or homogeneous.

The evidence is currently mixed to unfavorable for a learning claim:

1. Lifetime scores still beat a neutral-0.50 comparator descriptively, but the margin shrank this week: Brier skill is **+0.0836** and log-loss skill **+0.0617**.
2. The latest three OOS forecasts are **worse than the prior twelve** on both Brier and log loss, so recent performance does not show monotonic improvement.
3. One recent favorable point forecast, P000021, simply matched consensus; another, P000022, beat simple point baselines but lost the binary neutral benchmark.
4. The most direct recent causal discriminator, P000020, failed and forced a model narrowing.
5. 13/13 interval coverage is not evidence of superior uncertainty estimation and may indicate insufficient sharpness. The project is explicitly resisting the temptation to widen intervals further.
6. Several recent model changes are methodological safeguards whose predictive effects have not yet been tested. They cannot be counted as learning merely because they sound more sophisticated.

Possible explanations for the apparent lifetime advantage over neutral remain **luck, target-mix composition, regime-specific fit, conservative probabilities, broad intervals, and dependence among forecasts**. There is no evidence of hindsight rewriting in the audited records, but absence of hindsight leakage is a validity condition, not proof of learning.

The correct status is therefore: **the system is producing auditable error-linked revisions, but it has not yet shown longitudinal out-of-sample improvement.**

## 7. Highest-information discriminating forecast

**P000023** is the new highest-information forecast: **54%** probability that first-release **August core CPI is >=0.3% m/m** on Sept. 11; point **0.3%**, 80% interval **0.1%–0.4%**.

This directly tests the current H003-versus-H001 contest. Core CPI is chosen rather than headline CPI because the immediate oil/Hormuz branch weakened sharply this week; the question is whether **underlying** inflation remains sticky enough to justify the price-focused policy constraint. July core CPI was 0.2% and June 0.0%, so the probability is only modestly above even. A <=0.1% print with resilient activity would materially favor H001; >=0.4% would strengthen H003. No later consensus will be retrofitted into the forecast because none was sufficiently stable at the evidence cutoff.

The Sept. 4 Employment Situation remains an important earlier observation for H002 and the Fed reaction function, but P000023 is the cleaner discriminator between the two leading hypotheses.

## 8. Transferability review

No new Universal transfer candidate is created this Friday. The main lessons are applications of existing Universal safeguards: benchmark-relative evaluation, preserving downstream causal ambiguity, distinguishing direct policy communication from action/market response, proxy-scope discipline, and refusing to claim learning without longitudinal OOS evidence. The sticky-reemployment failure is important locally but currently instantiates existing proxy/persistence discipline rather than a genuinely new cross-domain principle.
