# Market World Model — Proof of Concept

A persistent, auditable AI research system for testing whether an agent can improve its predictive model of the U.S. equity market over time.

## Mission

Maintain and continuously improve a falsifiable causal model of the U.S. equity market. Generate probabilistic predictions **before** outcomes are known, preserve them immutably, evaluate them after their horizons expire, and revise the model according to prediction error.

The objective is **out-of-sample calibration and predictive improvement**, not trading profit.

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
