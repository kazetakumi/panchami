---
id: 005
title: Validation & test-oracle strategy
label: wayfinder:grilling
status: open
assignee:
blocked-by: []
---

## Question

A from-scratch engine is only credible if its outputs are provably right. Decide the validation regime the spec mandates: the **golden-fixture corpus** (how many test births, chosen to cover edge cases — nakshatra boundaries, sankranti days, retrograde stations, southern-hemisphere/diaspora births, midnight/DST births); tolerance policy (arc-minute vs arc-second per quantity; what discrepancy vs JHora fails the build); panchanga cross-validation against Mathrubhumi/Manorama print for a sample year (Kollavarsham month attribution and naal-boundary edge days per research §6.4); the **conventions ledger** (every place our output could legitimately differ from another app — ayanamsha, dasha year length, node type, sunrise definition — documented with the choice and why, since users WILL compare against other apps); and regression discipline (every doctrine rule from ticket 003 lands with a test citing its source). Not blocked — the strategy can be decided before the engine exists; it shapes how the engine is built.

Carried in from the astronomy spike (closed on partial evidence, founder decision 2026-07-17): the spike's 3 test births ([`spikes/astronomy-layer/`](../../../../spikes/astronomy-layer/README.md)) still need full graha + lagna arc-minute verification in JHora itself — fold them into the golden-fixture corpus as its first entries. Also seed the conventions ledger with the spike's finding that Drik Panchang and JHora display Lahiri values ~38″ apart.
