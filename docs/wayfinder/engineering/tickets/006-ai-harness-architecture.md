---
id: 006
title: AI harness architecture — grounding, provider abstraction, guardrail layer
label: wayfinder:grilling
status: open
assignee:
blocked-by: [004]
---

## Question

Design the AI astrologer harness. To decide: the **provider abstraction** (locked: ≥2 providers from day one — which two first, what the abstraction covers: chat, streaming, tool use); the **grounding design** — how the engine's chart JSON, precomputed dasha tree, today's panchanga, and doctrine rules (ticket 003) enter context (structured system prompt vs tool-calls back into the engine vs retrieval over the rule base — and when each); how readings **cite the method** (naal, dasha lord, Prashna Marga grounding — the honest-AI positioning made visible); conversation memory across a consultation; and the **guardrail enforcement layer** — where hard floors (no death-timing, no medical-cure claims) are enforced (system prompt alone is not enforcement: decide on input classification, output filtering, or both), leaving slots for the product map's per-topic table when it lands. Blocked by engine architecture — the harness consumes its contract.
