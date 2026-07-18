---
id: 009
title: Daily practice card — design prototype
label: wayfinder:prototype
status: closed
assignee: akhil
resolved: 2026-07-18
blocked-by: []
---

## Question

What does the daily practice card look and feel like? Per map decision 14 it is the retention loop: today's naal + a short practice + the user's sankalpa, generated from chart + current dasha + today's panchangam, feeding the consultation chat ("your practice mentioned Sani pressure — ask about it"). Prototype the card to react to: layout and content hierarchy (what's first — naal, practice, or sankalpa?), tone of the copy (psychological framing per decision 12, sankalpa vocabulary per decision 13), how the card links into a consultation, how streaks surface on it (lightweight per decision 15 — resolve the streak-mechanics fog here), and what changes day to day vs dasha period to dasha period. **Added by the pricing resolution (2026-07-18): the card carries a practical daily caution (rahu kalam / gulika kalam timing, panchangam-grounded) — constraint: cautions are practical and factual, never ominous; vague dread next to a consult prompt is the monetization-of-fear pattern the honest-AI brand cannot touch.**

## Resolution (2026-07-18)

Resolved by an iterative HITL prototype session (step-by-step: ground → ink → content blocks → chrome). **Asset:** the locked prototype at https://claude.ai/code/artifact/82df65e6-1714-4c38-99f9-18ca0c7ba53c (final + all exploration steps preserved in `spikes/practice-card-prototype/`).

### The locked home screen ("Today")

1. **Top line:** *Panchami* wordmark (serif) + **profile chip** top-right → **right side-drawer** over a scrim: identity header rendered the jyothisham way (*name · naal · rasi* — your birth star is your profile), then Jathakam · Pariharam · Panchangam · Wallet/credits · Birth details · Settings. No tab bar in the MVP.
2. **Tear-off calendar sheet** (the Malayalam wall-calendar daily page as design grammar): heavy top rule; big serif date numeral; **Velli/Friday pairing** (Malayalam leads, English confirms); Kollavarsham right-aligned; naal row in serif with rasi; **kalam strip as three equal columns, label over time** (Rahu · Gulika · Yamakanda), rust color, tabular numerals, no AM/PM.
3. **Her note — a warm-rose card** (#F7E3DC, rounded, soft shadow): the *tailored* daily reading (chart + dasha + panchangam; the moat vs. free generic content), 2–3 sentences, serif italic, signed *— Panchami*. **No veil/tap** — a fresh note each morning is the reveal. **No method line on the card** — chart grounding lives in her chat. Two value zones deliberately: sheet = shared fact, rose card = yours.
4. **Single CTA:** *"Something on your mind about today?"* → violet button **Speak to Panchami** → *1 credit · no clock, one concern, all your questions.* The page's one loud element; the payment funnel shares attention with nothing.
5. **Screen scrolls**; content may push the CTA partially below the fold on small phones — accepted (first glance = daily value; verify at 320px in build).

### Design tokens (frozen — nothing new gets a color without retiring one)

Light-first (brand decision; dark mode a later courtesy). Ground **Kanikkonna #FBF6E2** (Vishu-flower pale gold) · ink **Kadukka #2F2812** (warm umber-black) · accent gold **#A8842C** · kalam/warn rust **#A4552E** · her card **warm rose #F7E3DC** · Panchami violet **#4A3F63** (CTA, her avatar). Serif (Georgia-class) for ritual/domain content, system sans for utility; license a proper serif (and script, if ever used) in the real build.

### Explored and rejected (with reasons — primary sources in the spike files)

Chat-bubble card frames (two materials fighting the paper world) · **manifestation deck card** incl. spiritvibez-style blush/line-art/script (foreign metaphor; the generic-wellness territory the brand ticket forbids) · lamp-ignition reveal animation (too theatrical for the founder's minimalism) · tap-to-reveal veils, incl. "kani reveal" (daily friction on a glance object; the fresh page IS the reveal) · method line on the card (redundant; lives in chat) · practice as separate row and as in-card prescription (removed from home entirely) · tab bars (5-tab/4-tab/FAB/swipe/header-doors/drawer/hub all rendered and compared; leaner chrome chosen **for now** — see watch-item) · two equal CTAs and the pariharam secondary link (funnel-splitting; removed "for now").

### Watch-items recorded for the concierge run

1. **All retention weight now rides on daily writing quality** — no gamification remains on the home screen; the practice-library/voice ticket and AI-harness evals inherit that weight.
2. **Pariharam/practices and streaks are off the home screen** (drawer only). Watch drawer-room visit rates; if the wellness layer goes unvisited, the navigation conversation (tab bar / secondary link) returns post-validation. Streak mechanics now belong to the **pariharam screen design** (graduated to [ticket 013](013-pariharam-screen.md)).
3. **Interaction language:** kavadi-cast gesture reserved for prashna mode (recorded in the fog for consultation/prashna design); kani framing retired.

**Consequences:** engineering map's frontend/UI work (tickets 013/014 there) inherits a fully specified home screen + frozen tokens; streak-mechanics fog graduates → [Pariharam screen — design prototype](013-pariharam-screen.md). Asset: a throwaway UI prototype via /prototype, linked from this ticket on resolution.
