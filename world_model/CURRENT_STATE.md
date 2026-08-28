# Current Market State

**Model version:** 0.2.13  
**Status:** Friday post-close state; P000022 resolved; fifteen resolved binary-probability components; no demonstrated learning  
**Evidence cutoff:** 2026-08-28T18:07:44-04:00

## Auditor result
P000022 was resolved before post-Aug. 27 evidence was used for model revision. Treasury's official Aug. 28 daily par yield curve reported the 10-year rate at **4.73%**, so the precommitted `>=4.70%` event resolved TRUE. The 0.47 probability scored Brier **0.2809** and log loss **0.755023**, worse than the neutral 0.50 comparator. The 4.69 point estimate had **4 bp** absolute error versus **6 bp** for frozen no-change and **5 bp** for the frozen one-day recent-trend benchmark. The 4.57%-4.81% 80% interval covered.

Lifetime scoring is now **n=15**, mean Brier **0.229100**, mean log loss **0.650410**. Descriptive skill versus a neutral 0.50 probability comparator is **+0.0836 Brier skill** and **+0.0617 log-loss skill**, but targets are heterogeneous and the sample is only half of the precommitted 30-resolution minimum. **No learning claim is permitted.**

## OBSERVATIONS
- Fed Chair Kevin Warsh said current labor conditions are consistent with full employment, described prices as the Fed's predominant current focus, said recent better inflation readings had not established a changed underlying trend, and said the Fed must see inflation moving clearly and sufficiently quickly to 2% or it has “work to do.” He also said medium-term inflation expectations remain broadly anchored and committed to a discipline rather than a specific decision.
- BLS's preliminary March 2026 CES benchmark revision estimated total nonfarm employment 79,000 lower (-0.1%) and private employment 178,000 lower (-0.1%) over the relevant 12-month benchmark period; the final revision is due in February 2027.
- Treasury's official 10-year par yield rose **4.67% -> 4.73%** and the 30-year **5.19% -> 5.22%** from Aug. 27 to Aug. 28.
- Brent settled **$89.31** and WTI **$83.40**, down more than 5% and 4% for the week amid tentative/choppy recovery in Hormuz flows and reopening rumors.
- Final August University of Michigan sentiment was **51.7**. The S&P 500 closed **7,711.76**, down 0.25% Friday but up 0.49% for the week; breadth was negative Friday without a disorderly broad selloff.

## INFERENCE
The strongest new information is a cleaner read on the **policy reaction function**, not a new macro causal edge. Warsh's direct statement that labor is consistent with full employment while inflation progress remains inadequate strengthens H003's policy-constraint branch. This is higher-quality evidence about policy intent than inferring intent from a yield or equity move.

At the same time, the immediate **energy-escalation branch weakened materially** as oil fell sharply over the week, and Warsh said medium-term inflation expectations remain anchored. Those observations preserve H001 as a close rival and prevent a larger H003 upgrade.

The BLS benchmark revision supports the idea that hiring growth has been weaker than headline unemployment/claims alone suggest, especially in the private sector. It does **not** reverse P000020's error-linked revision: current claims still do not support promoting one continuing-claims threshold into a durable sticky-reemployment regime. The labor-flow split remains useful, but it needs corroboration from payroll breadth, vacancies, hiring, unemployment duration and future claims.

P000022 is deliberately read in two layers: the point forecast modestly beat simple yield benchmarks, but the binary probability lost to neutral. The realized 6 bp rise is compatible with H003 yet does not identify the speech, inflation persistence, term premium, or positioning as the sole cause.

## Current regime
**Resilient but bifurcated expansion with weak household sentiment/housing, low current layoffs, still-high underlying inflation, and a Fed reaction function focused primarily on price stability. H003 remains the narrow leader because the policy constraint is explicit even as the immediate oil shock eases; H001 remains close because energy is falling and inflation expectations are still broadly anchored.**

## Hypothesis weights
| Hypothesis | Weight |
|---|---:|
| H001 Soft landing | 0.34 |
| H002 Late-cycle recession | 0.18 |
| H003 Fiscal/inflation regime | 0.36 |
| H004 Productivity boom | 0.12 |

**Change from Aug. 27:** H001 unchanged, H002 -0.01, H003 +0.01, H004 unchanged. The small transfer from H002 to H003 reflects direct Warsh reaction-function evidence and his full-employment assessment, while the modest/old benchmark revision and weak sentiment preserve H002 as a delayed rival. Lower oil and anchored expectations prevent moving weight from H001.

## Skeptic result
The Skeptic attacked H003. The strongest H001 countercase is that oil has fallen sharply, medium-term inflation expectations remain anchored, and Warsh explicitly avoided a fixed policy decision. If growth remains resilient while August inflation cools and long yields subsequently retreat, Friday's rate move will look like a transitory communication/positioning response rather than confirmation of a persistent inflation regime. H003 would become unfalsifiable if every strong activity print, every high yield, and every policy comment were automatically classified as inflationary while contrary oil and household evidence were discounted.

The key identification warning is that the 10-year yield is a downstream endpoint with multiple causes. The model therefore does not attribute the 4.67% -> 4.73% move to Warsh alone.

## Material model changes
1. **Reaction-function evidence strengthened, not structurally changed.** Direct Chair communication now provides stronger evidence that current policy is price-focused while labor is judged near full employment; no new causal edge is needed.
2. **Immediate energy branch weakened.** A >5% weekly Brent decline means H003 is currently more a core-inflation/policy/duration thesis than an oil-escalation thesis.
3. **H002 -0.01 to H003.** The direct current-policy/labor assessment outweighs the modest backward-looking benchmark revision, while H002 remains live through household/hiring weakness.
4. **No H004 promotion.** Warsh explicitly treated AI productivity as an open question; AI investment remains input evidence, not realized aggregate productivity.
5. **No learning credit.** P000022's binary score worsened lifetime proper scores even though its point estimate beat simple rate benchmarks.

## Forecast status
- **P000022 resolved TRUE:** Brier 0.2809, log loss 0.755023; point MAE 4 bp versus no-change 6 bp and recent trend 5 bp; interval hit.
- Longer-horizon legacy forecasts remain governed by their original horizons and resolution rules.

## What would surprise the model?
- August employment data showing a clear synchronized deterioration in payrolls, unemployment, participation-adjusted labor conditions and subsequent claims/credit would revive H002 materially.
- August core inflation near 0.1% m/m or lower, accompanied by resilient activity and a sustained decline in long yields, would materially favor H001 over H003.
- Continued oil relief plus anchored inflation expectations **without** any easing in the policy/long-rate constraint would imply that non-energy core inflation, duration supply or term premium is doing more work than the current model can cleanly identify.
- Broad evidence of economy-wide output-per-input gains attributable to AI investment would be required before H004 can rise materially.
