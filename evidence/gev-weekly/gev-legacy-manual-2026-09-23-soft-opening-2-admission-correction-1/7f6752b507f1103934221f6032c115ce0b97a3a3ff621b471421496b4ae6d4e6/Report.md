# GEV: reproducible coordinate discontinuities, unresolved physical cause

## Summary

**OBSERVATION:** A verified cached review contains 75 retained coordinate-jump cases inside this report's rolling window, with 92 constituent coordinate pairs. Exact replay and separate haversine arithmetic reproduce them. They demonstrate discontinuities in reported positions, not aircraft speeds, interference, attribution, military intent or economic loss. Forty-two pairs include a change in position-source label, leaving processing or association artifacts as a material alternative.

## Coverage

The requested interval is September16 00:58:46 UTC through September23 00:58:46 UTC. The newest completed readable cached weekly export covers September14–20, with September15 missing. Ninety retained cases across six available calendar days reproduce from original trace bytes; 75 fall within the requested interval, fifteen each on September16–20. September21 is present in the latest private daily-review index but its actual trace bytes are not included in this completed weekly access mirror. September22 and the current partial day are also absent here. Missing days are gaps, not evidence of normal traffic.

A separate completed live/satellite screening export ends September21 19:37:40 UTC and reproduces 288 detector events. Its exact input sets contain 19,510 aircraft observations, a capped 250,000-record aircraft baseline, 1,012 satellite records and 218 satellite-baseline records. The screen is partial. It is a saved artifact, not a live GEV query, full global surveillance or a fresh September23 collector pass. Both exports were materialized through the authorized private connector, their exact outer/inner hashes verified, and their deterministic code pins checked. The model invoked no collector, export workflow, provider request or schedule.

## Hypotheses and tests

The ranked leads were retained aircraft coordinate jumps, changes accompanying position-source switches, and satellite model-epoch comparability. Aircraft geometry was selected because original retained trace bytes support exact bounded tests. Cached per-day selections are bounded leads, not a whole-week ranking. Selection and threshold sensitivity were predeclared; past findings and preparatory metadata exposure make this replication exploratory.

The unchanged pinned aircraft engine at `satellite-research@e9105bf38cdca6e78955f03844a2c894c9abd793` reproduced all 90 retained cached cases. A separate calculation bound original observation IDs to each constituent pair, used a 6,371,000 m spherical Earth radius and exact epoch differences, and matched the saved maxima for all 75 in-window cases. The 92 pairs exceed 600 m/s and 5 km under the configured rule; 71 exceed 750 m/s and 53 exceed 1,000 m/s. These are sensitivity counts within selected anomalous pairs, not false-positive rates or population prevalence.

One extreme pair spans about 448.740 km in 1.33000016 seconds, or 337,398.684 m/s implied by coordinates. Its position-source label switches MLAT to ADS-B and the position ages remain unknown. This cannot be read as physically verified flight. **H1, a discontinuity in the retained reported coordinates:** supported. **H2, processing/source association or equipment artifacts:** plausible and consistent with observed switches, not causally proven. **H3, actual navigation interference:** unresolved; a source switch can also accompany genuine degradation, and receiver-independent corroboration is missing. **H4, a military or trade consequence:** untested; traffic geometry supplies no cargo/facility outcome or attribution.

The satellite comparison audits the last retained snapshot pair for 128 entities. Five pairs have unchanged model epoch and six have nonpositive epoch differences. Therefore a generic rate obtained by dividing every element change by snapshot elapsed time would mix incompatible model vintages. Model-element changes do not establish maneuvers, close approaches or intent. No physical orbit-cause verdict was inferred.

An initial independent diagnostic incorrectly compared whole-event endpoint chords with maximum constituent-pair speeds for grouped events. That draft diagnostic was rejected and is explicitly superseded by the original-observation-ID pair audit; it was not used as a final finding. The deployed replay itself passed. All 53 inventoried live-export files were verified. The cached verifier proves retained case reproduction, not omitted cases, full-day ranking or global coverage.

## Limitations

Aircraft field ages and receiver independence are unknown; source labels do not identify independent sensors. The three sampled pilot regions and retained daily selections are not the world. Unknown field ages, missing controls, partial-day boundaries and capped baseline remain unresolved. A zero matched control count would not establish an unaffected comparison group. The latest collector uncertainty/cooldown ledger was preserved separately from older export evidence; no uncertainty was cleared. Source ancestry receives one evidence contribution and related weather/energy narratives do not independently confirm this geometry.

## Sources

Retrospective [adsb.lol](https://www.adsb.lol/) trace archive records and [CelesTrak](https://celestrak.org/) model elements, with exact original member hashes, acquisition times, daily review/export manifests and pinned method identities in the private package. Cached packet SHA256 is `92b3641a100873d4c0aedcac87ea2b825a61bdb67bfad5cc955fb2b5d479e457`; that identifies the actual verified saved packet, not current source coverage.

## Next decisive evidence

A permitted completed mirror containing September21–22 original traces, receiver-independent observations with known field freshness, and matched healthy passes would improve coverage and discrimination. Physical/economic linkage additionally requires independent operational/cargo outcomes. The report creates no backfill, source replay, collection takeover or new schedule.
