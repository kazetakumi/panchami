---
id: 013
title: UI/UX design — mobile-first visual language & key surfaces
label: wayfinder:grilling
status: closed
assignee: akhil (claimed 2026-07-17, resolved 2026-07-18)
blocked-by: []
---

## Question

Decide the mobile-first visual language and how it plays out on the app's identity-level surfaces. To decide: the design-token approach (color, type, spacing, component patterns) and how it expresses mobile-first (not "responsive desktop," designed for one-hand phone use first); the **South Indian square chart rendering** — fixed signs, clockwise, the exact visual/labeling convention Malayali users expect (research §3.7), Malayalam sign/planet abbreviations vs English; the chat UI's visual and interaction design (streaming message display, mobile chat patterns, how the AI's method-citation — naal, dasha lord — surfaces visually per the "honest AI" positioning); the jathakam/grahanila view layout (chart + panchanga block + dasha table together, per the pipeline in research §3.8). Not covered here: framework/SSR choice, offline/PWA technical implementation ([Frontend technical architecture](010-frontend-architecture.md)); consultation-session flow, which waits on the product map's consultation-UX fog.

Split off from the original combined ticket 010, 2026-07-17, so the UI/UX half stays session-sized and separable from framework decisions.

Paused 2026-07-18, blocked-by added: the founder wants to settle the primary IA pattern (chat-first vs dashboard) with a concrete prototype before locking token/component details — see [Primary IA pattern — chat-first vs dashboard](014-ia-pattern-chat-vs-dashboard.md). Placeholder-branding decision (warm/traditional palette; jathakam/panchanga density question left open) carries forward once this resumes.

Resumed 2026-07-18: ticket 014 closed by reference to the product map's [Daily practice card — design prototype](../../tickets/009-daily-practice-card-design.md) — dashboard-leaning hybrid, drawer + rooms chrome, frozen home tokens. That IA shell and palette now carry forward as fixed; this ticket's remaining scope is the chat UI visual/interaction design, the jathakam/grahanila layout, and the South Indian square chart rendering convention.

Narrowed 2026-07-18 (grilling session): the founder wants the chart rendering convention decided now and the rest — chat UI, and the full jathakam page layout (panchanga block + dasha table) — worked later. This ticket closes scoped to the chart only; the deferred scope moves to [Chat UI & jathakam page layout](015-chat-ui-jathakam-layout.md).

## Resolution (2026-07-18)

**South Indian square chart rendering convention**, resolved by grilling:

1. **Format**: the standard South Indian square (research §3.7) — 12 fixed boxes, signs fixed per box (Aries always second cell, top row), read clockwise, lagna marked with a diagonal stroke in its box.
2. **Labels**: Malayalam vocabulary in Latin script (e.g. "Chovva" for Mars, "Idavam" for Taurus) — consistent with the product map's locked language strategy (decision 5: English prose + Malayalam astrological vocabulary in Latin script), not English abbreviations and not Malayalam script (that stays a later locale).
3. **Box density**: name only — just the planet's Malayalam name sits in its occupied sign's box. No degree, retrograde marker, or nakshatra inline; keeps the chart glanceable and consistent with the minimalist direction set on the home screen.
4. **Tap-to-reveal detail**: tapping a planet opens a detail sheet with degree-in-sign, retrograde flag, nakshatra + pada, **and the English name alongside the Malayalam** (e.g. "Chovva (Mars) · Idavam (Taurus) · 14°32′ · Retrograde · Rohini pada 2"). This is the only place English appears — the chart face itself stays Malayalam-only, no dual-labeling.
5. **No standing English toggle** — considered and rejected in favor of tap-to-reveal, to avoid crowding small mobile boxes with dual labels.

No prototype asset was built for this narrow scope; the decision is recorded directly from the grilling session. Consequence: the engine/API contract ([Engine architecture & API contract](004-engine-architecture.md)) should expose Malayalam sign/planet names as first-class fields (not derived client-side from English), matching the Malayalam-vocabulary data layer noted in the map's fog.
