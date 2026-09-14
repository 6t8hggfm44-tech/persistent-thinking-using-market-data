# Current Market State

**Model version:** 0.2.14  
**Status:** Monday Sep. 14 post-close cycle completed; no forecast expired; no structural or hypothesis-weight change; no new forecast added  
**Evidence cutoff:** 2026-09-14T17:37:19-04:00

## Auditor

No currently authoritative open forecast reached its resolution horizon after the prior Sep. 11 cutoff and before this cutoff.

Open forecasts remain:
- **P000027:** 58% probability the FOMC raises both target-range bounds by at least 25 bp at the Sep. 15-16 meeting; resolves from the official Sep. 16 statement.
- **P000004:** three-month S&P distribution, resolving Nov. 9 close.
- **P000005:** one-year S&P distribution, resolving Aug. 9, 2027 close.

The prior probability ledger therefore remains **n=21**, mean Brier **0.213919**, mean log loss **0.617880**. No score, outcome, forecast content, benchmark or prior cutoff was altered. Because no forecast resolved and no learning/calibration state changed, no new Market Repo B validation record is required this cycle; the current validation protocol/code was nevertheless read at initialization as required.

## Canonical research-report intake

The canonical Energy/Weather research index and legacy GEV index remain empty at this cutoff. No completed weekly Energy, Weather or GEV packet has been received into the Market evidence archive, so no cross-domain report is used in this cycle. Setup notices are not evidence reports.

## New observations — first available after 2026-09-11T17:11:19-04:00

- **OBSERVATION:** Brent settled **$105.68/bbl** and WTI **$101.39/bbl** on Sep. 14. Reuters reported a Sep. 11 strike had knocked Saudi Arabia's East-West pipeline out of service and preliminary commodity-vessel transits through the Strait of Hormuz fell to single digits per day over the weekend versus a 10-day average of 14. Crude had jumped nearly 5% intraday before giving back most of the gain after a diplomatic remark.
- **OBSERVATION:** A Sep. 14 Reuters poll found **86 of 101 economists (85%)** expecting a 25 bp Fed hike on Sep. 16, reversing the prior week's majority hold call. Reuters also reported futures pricing near **90%** for a hike.
- **OBSERVATION:** The 10-year Treasury yield crossed **5%** on Sep. 14 for the first time since October 2023, around **5.01%** at Reuters' cited update.
- **OBSERVATION:** Reuters reported leaders of Anthropic, OpenAI and xAI calling for slower AI development because of safety risks. The PHLX semiconductor index fell **5.9%**; the S&P 500 closed **0.48% lower at 7,619.94**.

Full provenance and source links are preserved in `evidence/2026-09-14-cycle.md`.

## Inference

The new physical energy-disruption evidence modestly strengthens the near-term inflation/policy-constraint channel under H003, but the same shock can weaken real household demand and margins under H002. The large intraday oil reversal after a diplomatic signal demonstrates that the supply-risk path remains contingent rather than monotonic.

The sharp shift in economist and futures expectations is important external evidence about the Sep. 16 decision, but it is post-registration information for P000027. It cannot revise the frozen 58% probability or its benchmarks. Those expectations also share causal ancestry with CPI, PPI, energy prices and Fed communication, so they are not independent confirmations of H003.

The 10-year crossing 5% tightens financial conditions but is a multiply caused endpoint: expected Fed policy, oil/inflation risk, government and corporate issuance, fiscal risk and resilient growth can all contribute. It therefore supports neither H003 nor H002 uniquely.

The AI-development slowdown call is modest negative evidence for an unconstrained near-term H004 productivity/capex path, but one day's semiconductor/equity response is not direct evidence that realized economy-wide productivity investment will fall.

## Hypothesis weights

- **H001 Soft landing: 0.35** (unchanged)
- **H002 Late-cycle recession: 0.15** (unchanged)
- **H003 Fiscal/inflation regime: 0.38** (unchanged)
- **H004 Productivity boom: 0.12** (unchanged)

No reweighting is made. H003 remains the narrow leader. The additional energy disruption is directionally supportive, but the strongest new policy indicators are forecast/belief endpoints that share ancestry with already-known inflation and oil information. Moving weights immediately before the precommitted Sep. 16 discriminator would risk double-counting downstream repricing.

## Skeptic

**Attack on leading H003:** Oil's Sep. 14 intraday spike largely reversed on a single diplomatic comment, so the current supply shock may be less persistent than headline disruptions imply. A 10-year yield above 5% is itself contractionary and could transmit into housing, corporate finance and consumer credit, strengthening an H002 path. The 85% economist hike consensus and ~90% futures probability are not new physical measurements; they are reactions to much of the same inflation/oil/Fed information. The new AI-slowdown call adds a distinct risk to the H004-supported investment/wealth channel and could amplify tightening rather than validate H003.

**Response:** H003 remains narrowly plausible because the physical energy bottleneck worsened after the last cutoff and inflation had already been firm, but the evidence is mixed in sign for later real activity. The correct test is now the frozen policy-action forecast rather than further narrative updating from consensus or market repricing.

**What would surprise the current model:** an official Sep. 16 FOMC decision that does **not** raise both target-range bounds by at least 25 bp would directly challenge the policy-reaction mapping encoded prospectively in P000027. A hike would support that mapping but would not by itself prove H003's broader inflation/fiscal mechanism or resolve whether the energy shock later becomes contractionary.

## Learning state

Unchanged from the Sep. 11 weekly review: **insufficient evidence to assess learning at n=21** resolved probability forecasts. Later-vintage proper scores remain too sparse and heterogeneous to establish sustained improvement, interval coverage remains above nominal with cross-target sharpness not directly comparable, and no model revision has yet shown repeated benchmark-relative improvement on the forecasts it was designed to improve.

## Model-change attribution

- **v0.2.8 regional-to-national manufacturing safeguard:** one positive direct post-change test; insufficient for learning credit.
- **v0.2.13 inflation/policy discriminator:** P000023 supplied one modest positive prospective test; P000027 is the next cleaner policy-mapping test and remains unresolved.
- **v0.2.14 labor measurement bridge:** no later monthly payroll forecast generated under the revision has resolved; learning credit remains zero.
- **Treasury announcement/realized-flow distinction:** the 5% 10-year endpoint remains multiply caused; no isolated causal score exists.

## Material model changes

**None.** Model v0.2.14, `world_model/CAUSAL_GRAPH.md`, measurement bridges and hypothesis weights remain unchanged. No new Universal transfer candidate is added; today's source-ancestry, ambiguous-endpoint and anti-hindsight issues are already covered by existing Universal lessons/failure modes.

## New forecast

**None.** P000027 resolves in two days and is already the highest-information prospective discriminator. Creating another FOMC/rates forecast after observing the post-CPI consensus swing would be strongly correlated with it and would inflate nominal sample size. No unrelated target at this cutoff offers enough incremental information value to justify manufacturing activity.

## Most important watch

**The Sep. 16 FOMC decision resolving P000027.** The model should be judged against the frozen 58% forecast and frozen Sep. 4 market comparators, not against today's much higher post-CPI consensus.
