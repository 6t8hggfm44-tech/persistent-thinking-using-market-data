# Energy and weather research intake and reconciliation

Pete authorized complementary energy and weather research workflows on 2026-09-14, using the same save, verify, distribute and canonical-input pattern as GEV. This policy extends intake without rewriting the existing [GEV intake](GEV_REPORT_INTAKE.md), forecast records or model weights.

## Canonical source records

The source repositories are [energy](https://github.com/6t8hggfm44-tech/energy), [weather](https://github.com/6t8hggfm44-tech/weather), and [satellite-research](https://github.com/6t8hggfm44-tech/satellite-research). Domain reports are independent, dated research records. A completed received report becomes canonical with its original confidence, evidence status, missingness and later corrections intact. It does not establish every causal claim as fact.

Receive full final hypothesis reports and metadata, not screening output, synthetic examples or local Mac links alone. A finished negative, inconclusive or evidence-gap report is valid. Verify a complete packet before marking intake complete. Preserve source hashes, report versions, workflow commit, actual coverage, event window, generation/local-availability times and actual market receipt time separately. Hashes identify exact bytes; copied text needs its own computed hash and honest source-byte verification status.

Use the domain-qualified key `domain:run_id:report_sha256`. Save energy and weather final text and intake records under `evidence/research/<domain>/<run-id>/<report-hash>/`, and append to [the research index](../evidence/research/INDEX.md). GEV keeps its established archive/index and legacy key; do not create a second record merely to add the domain prefix. Preserve only authorized final report content and safe metadata, never raw archives or credentials.

Acknowledge the key, version, supplied hash, actual receipt timestamp, integrity state and verified archive path/commit or exact failure. Distinguish received, acknowledged and persisted states. Deduplicate retries. Do not claim receipt from an originating local file alone, or durable persistence from a successful message send alone. Incomplete chunks are pending.

## Use during normal reporting

At Phase 2, consult complete reports available by this cycle's evidence cutoff, including revisions to earlier reports. Cite exact domain/run/version and date; state whether each relevant report changes the assessment, supports a view, is inconclusive or has no demonstrated relevance. Distinguish OBSERVATION, INFERENCE, ASSUMPTION and SPECULATION. Do not force market significance.

Keep frozen forecasts, source cutoffs and outcomes immutable. Later source backfill or reanalysis cannot become earlier knowledge. A research report is not itself a scored Market prediction. Preserve prospective registration, benchmarks, resolution rules, the Economy handoff boundary and Market Repo B validation. Only justified material model changes enter the existing model changelog; intake alone changes no weights.

## Reconcile the three domains

Follow the source [reconciliation protocol](https://github.com/6t8hggfm44-tech/energy/blob/main/docs/RECONCILIATION.md). First preserve the separate domain reports; then perform a separately identified synthesis using their exact versions. Weather must not be fitted to the current energy/GEV story after seeing downstream outcomes. Previously declared weather controls may be used with recorded vintages and provenance.

Align actual event windows, geography, exposure, reporting periods, units and physically plausible lags. A model weather point, weekly national fuel estimate and aircraft track do not measure the same population. Check common causes, shared feeds and upstream source IDs: three reports based on one measurement are not three independent confirmations. An absence of declared common IDs does not prove independence.

Test supported linkages against ordinary alternatives and matched controls. Require operational evidence for disruption and separate economic evidence for costs, output, prices or inflation. Preserve contradictions and missing controls. The optional source-repository audit script verifies report hashes, availability and shared-source metadata; it does not establish a causal or economic link.

Weather is due Monday 08:20 and energy 08:40 America/Los_Angeles; GEV is due 08:00. These are start times, not delivery guarantees. A late, missing or stale counterpart stays explicit. Use available evidence and reconcile at the next existing reporting cycle when the missing report arrives. Do not create another schedule or an extra forecast cycle for intake.

Corrections append new versions with supersedes links and changed claims. Retain original report versions and historical use, then review affected downstream interpretations prospectively. No setup notice is a weekly report. No trading, purchases, broader sharing, or Executive Agent activation is authorized by this policy.
