---
id: 015
title: Chat UI & jathakam page layout — visual and interaction design
label: wayfinder:grilling
status: open
assignee:
blocked-by: []
---

## Question

Split off from [UI/UX design — mobile-first visual language & key surfaces](013-ui-ux-mobile-first.md), 2026-07-18, when the founder chose to lock the chart rendering convention now and defer the rest. Two surfaces remain:

1. **Chat UI visual and interaction design** — resolved so far: conventional two-sided chat bubbles (not a continuation of the home screen's paper-sheet metaphor), frozen palette (Kanikkonna/Kadukka/gold/rust/rose/violet) applied to the bubble layout. Still open: how the AI's method-citation (naal, dasha lord, and other chart facts a reply is grounded in) surfaces visually inside a message per the "honest AI" positioning — candidates discussed but not decided were inline highlighted terms with tap-for-grounding, footnote markers, or a per-reply "based on" panel; streaming-message display; the persistent "AI" marker placement (policy locked in [guardrail ticket 004](../../tickets/004-guardrail-policy.md), this ticket gives it a concrete visual home); input area and send affordance.
2. **Jathakam page layout** — the full page beyond the chart alone: how the panchanga block (birth-moment tithi/nakshatra/yoga/karana) and the dasha table (resolved shape from ticket 013's chart-only session doesn't cover this: mahadasha list only, no antardasha drill-down) sit together with the chart on one mobile screen. The chart-rendering ticket assumed single-vertical-scroll (chart → panchanga → dasha) as the leading option but did not confirm it in scope.

Also carries forward the general design-token/component-pattern question for surfaces beyond the home screen and the chart (typography scale, spacing, button/input component patterns) — home-screen tokens are frozen (ticket 009) but haven't been proven out on a data-dense or conversational surface yet.
