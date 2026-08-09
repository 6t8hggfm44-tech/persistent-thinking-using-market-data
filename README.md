# Market World Model — Proof of Concept

A persistent, auditable AI research system for testing whether an agent can improve its predictive model of the U.S. equity market over time.

## Mission

Maintain and continuously improve a falsifiable causal model of the U.S. equity market. Generate probabilistic predictions **before** outcomes are known, preserve them immutably, evaluate them after their horizons expire, and revise the model according to prediction error.

The objective is **out-of-sample calibration and predictive improvement**, not trading profit.

## Persistent default

Substantive market, macroeconomic, cross-asset, or forecasting questions should automatically consult this repository when its accumulated model, forecasts, assumptions, or prior error history could materially improve the answer. The user should not need to explicitly request GitHub access.

Not every finance question belongs here. Simple factual lookups, personal budgeting arithmetic, or questions unrelated to the modeled system can be answered directly. New material should be preserved only when it changes the causal world model, creates or resolves a forecast, records a meaningful prediction error, modifies an assumption, or adds durable evidence relevant to future forecasting.

Repository conclusions remain provisional. Fresh data and better evidence may revise them; prior forecasts and material belief changes should remain auditable rather than being rewritten after outcomes are known.

## Economy handoff boundary

The structural Economy repository, `6t8hggfm44-tech/economy-`, develops broad mechanisms and long-horizon hypotheses. It may submit a candidate implication to Market only through a complete, timestamped handoff packet.

Market independently decides whether to accept, modify, or reject the candidate. An accepted candidate becomes a Market prediction only after Market fixes the variable, universe, direction or probability distribution, evidence cutoff, horizon, benchmark, resolution source, resolution rule, and failure condition **before** the outcome, and assigns its own prediction ID.

Broad Economy narratives are not Market predictions. A Market result may feed back to Economy only when the forecast genuinely discriminated among structural explanations; one result does not automatically validate or erase a broad structural thesis.

## Initial scope

The agent models a compact cross-asset state vector:

- S&P 500 total-return direction and range
- VIX level/range
- U.S. 10-year Treasury yield
- High-yield credit spreads
- U.S. dollar index / broad dollar direction
- WTI crude oil
- Market breadth
- Relative performance of major U.S. equity sectors

Forecast horizons:

- 1 trading day
- 1 week
- 1 month
- 3 months
- 1 year

## Core loop

1. Read the repository state.
2. Ingest timestamped evidence available as of the run.
3. Separate observations from interpretations.
4. Update competing hypotheses.
5. Generate falsifiable probabilistic forecasts.
6. Commit forecasts before outcomes are known.
7. Resolve expired forecasts using objective data.
8. Score them.
9. Diagnose errors.
10. Revise the model only after the scoring step.
11. Record every material belief change.

## Roles

The same AI can execute the roles sequentially, or different models can be assigned:

- **Modeler** — maintains the causal world model.
- **Forecaster** — derives predictions without rewriting the model to fit desired answers.
- **Skeptic** — attacks the favored explanation and seeks disconfirming evidence.
- **Auditor** — resolves and scores forecasts, checks hindsight leakage and rule violations.

## Success criterion

The experiment succeeds if later forecasts are measurably better calibrated and more accurate out of sample than earlier forecasts and simple benchmarks.

It does **not** succeed merely because the repository contains persuasive explanations.
