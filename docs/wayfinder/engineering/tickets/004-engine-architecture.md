---
id: 004
title: Engine architecture & API contract
label: wayfinder:grilling
status: open
assignee:
blocked-by: [001]
---

## Question

Decide the Python engine's module decomposition and the JSON contract everything else consumes. Module candidates (research §3.8 pipeline): ephemeris adapter (wraps the astronomy source chosen in ticket 001 — the ONE seam where external data enters), ayanamsha, chart builder (rashi/lagna/whole-sign bhavas), nakshatra/naal, vargas (D9 first), panchanga (tithi/vara/nakshatra/yoga/karana + rahukalam/gulikakalam), Vimshottari dasha tree, gochara/transits, prashna primitives. To decide: module boundaries and dependency direction; the canonical chart JSON schema (the AI harness and frontend both consume it — canonical codes + locale-aware labels per product decision 5); sync API vs precompute-and-store (dasha trees are precomputed at chart-build time); how conventions (ayanamsha, dasha year length 365.25d, true/mean Rahu) are pinned in one config with documentation. Blocked by the astronomy spike because the adapter seam shapes everything downstream.

**Paused 2026-07-18:** opened on module boundaries (first candidate: a single "Positions" core off the astronomy adapter, with chart-builder/nakshatra/vargas/panchanga/dasha as independent consumers rather than a linear pipeline) — the founder wants to sit with the full open-ticket picture before going deeper into an architecture call. No decision made; resume fresh.
