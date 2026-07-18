---
id: 015
title: Chat UI & jathakam page layout — visual and interaction design
label: wayfinder:grilling
status: closed
assignee: akhil (claimed 2026-07-18, resolved 2026-07-18)
blocked-by: []
---

## Question

Split off from [UI/UX design — mobile-first visual language & key surfaces](013-ui-ux-mobile-first.md), 2026-07-18, when the founder chose to lock the chart rendering convention now and defer the rest. Two surfaces remain:

1. **Chat UI visual and interaction design** — resolved so far: conventional two-sided chat bubbles (not a continuation of the home screen's paper-sheet metaphor), frozen palette (Kanikkonna/Kadukka/gold/rust/rose/violet) applied to the bubble layout. Still open: how the AI's method-citation (naal, dasha lord, and other chart facts a reply is grounded in) surfaces visually inside a message per the "honest AI" positioning — candidates discussed but not decided were inline highlighted terms with tap-for-grounding, footnote markers, or a per-reply "based on" panel; streaming-message display; the persistent "AI" marker placement (policy locked in [guardrail ticket 004](../../tickets/004-guardrail-policy.md), this ticket gives it a concrete visual home); input area and send affordance.
2. **Jathakam page layout** — the full page beyond the chart alone: how the panchanga block (birth-moment tithi/nakshatra/yoga/karana) and the dasha table (resolved shape from ticket 013's chart-only session doesn't cover this: mahadasha list only, no antardasha drill-down) sit together with the chart on one mobile screen. The chart-rendering ticket assumed single-vertical-scroll (chart → panchanga → dasha) as the leading option but did not confirm it in scope.

Also carries forward the general design-token/component-pattern question for surfaces beyond the home screen and the chart (typography scale, spacing, button/input component patterns) — home-screen tokens are frozen (ticket 009) but haven't been proven out on a data-dense or conversational surface yet.

## Resolution (2026-07-18)

Resolved by grilling, then proven out with an HTML prototype reacted to and corrected in-session. **Asset:** [`spikes/chat-jathakam-prototype/`](../../../../spikes/chat-jathakam-prototype/README.md) — first pass invented a fresh visual system and was rejected ("messed up the styling"); rebuilt to reuse the locked home-screen's actual chrome and components verbatim (`spikes/practice-card-prototype/card-build.html`), then corrected again in review (the citation grounding note was a floating popover that overflowed the phone's narrow width — replaced with an in-flow expanding note, same tap-to-reveal language as the chart).

### 1. Jathakam page layout

1. **Single continuous vertical scroll**: chart → panchanga block → dasha table. No tabs/segments — matches the paper-sheet grammar already locked for the home screen; jathakam is a document read top-to-bottom, not a multi-mode workspace.
2. **Chart is the hero**: largest element, top of scroll; panchanga and dasha are visually secondary/lighter, mirroring how a traditional printed jathakam leads with the chart.
3. **Dasha table**: mahadasha list only by default (lord + date range), **tap-to-expand into antardasha for the current mahadasha only** — not a pre-expanded full tree, not pratyantardasha. Mirrors the chart's tap-to-reveal pattern; the current sub-period is what "which dasha am I running?" actually needs, deeper drill-down belongs in conversation, not the table.
4. **Panchanga block** reuses the tear-off-sheet visual grammar (serif, Malayalam-leads/English-confirms) but drops the "today" framing entirely — a static fact row (tithi · nakshatra · yoga · karana), not a date-hero sheet. Labeled **"Panchangam · at birth"** to stay distinct from the drawer's separate live "Panchangam" room (today's panchangam) — a one-line fix for a real naming collision the ticket surfaced.
5. **Standing disclaimer** (locked by [guardrail ticket 004](../../tickets/004-guardrail-policy.md)) sits as a **sticky footer**, pinned to the viewport regardless of scroll — same treatment on the chat surface, one shared component.

### 2. Chat UI visual and interaction design

6. **Method-citation**: **inline highlighted terms with tap-for-grounding** (not footnote markers, not a per-reply "based on" panel) — keeps the citation attached to the exact claim, scales to long consultations without adding chrome per message, teaches one interaction language app-wide (tap a marked term for detail, same as the chart). The grounding detail itself renders as an **in-flow expanding note below the message** — not a floating popover; the first prototype pass used a popover and it overflowed the phone width, corrected in review.
7. **Streaming**: token-by-token reveal, reducing perceived latency on chart-grounded generation; the citation term resolves into its tappable state only once it has finished streaming in.
8. **Persistent "AI" marker**: lives in the **chat header subtitle** ("Panchami · AI astrologer"), not repeated per-bubble — satisfies "never buried" without turning every message into a disclaimer. The standing disclaimer (sticky footer, same as jathakam) carries the recurring legal-duty visibility.
9. **Input area**: conventional bottom text field, **violet send button** (Panchami-violet, matching the home screen's CTA color), rounded to match the app's soft aesthetic — zero novelty on the one control that must be instantly legible.

### 3. General design-token/component-pattern rule

10. **Typography split, locked app-wide**: **serif = occasional/ritual content** (her home-screen note, jathakam section headers, panchanga labels); **sans = frequent/utility content** (chat bubbles on both sides, dasha table rows, tap-to-reveal detail sheets, chart box labels). Serif at chat-message volume would read as slow and hurt mobile legibility; this is the rule ticket 013 deferred pending proof on a data-dense and a conversational surface — both are now built.

**Consequences:** the map's fog entry "Malayalam vocabulary data layer" and the engine/API contract should expect the chart, panchanga, and dasha table to consume Malayalam-first fields per ticket 013's convention, now exercised on a full page. [Assemble the engineering spec](012-assemble-spec.md) can treat visual/interaction design as fully specified — no further UI/UX fog remains open on the engineering map.
