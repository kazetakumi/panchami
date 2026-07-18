---
label: wayfinder:map
title: AI Kerala Astrologer — Engineering Spec
created: 2026-07-17
tracker: local-markdown (tickets in ./tickets/, blocking via frontmatter `blocked-by`, claim via `assignee`)
---

# AI Kerala Astrologer — Engineering Spec

## Destination

A **buildable engineering spec** for the concierge MVP: every engineering decision made and written down — architecture, data model, engine module specs with textual citations, AI harness design, validation strategy, and a build sequence sliced into agent-session-sized pieces — ready for implementation sessions to execute. This map decides **how it's built**; it writes no production code. Product decisions belong to the [product-definition map](../map.md).

## Notes

- Domain research: [`docs/research/kerala-astrology-domain-research.md`](../../research/kerala-astrology-domain-research.md) (computation pipeline §3, conventions §6.2–6.4, copyright §5.1). Competitor research: [`docs/research/competitor-landscape.md`](../../research/competitor-landscape.md).
- Skills per ticket type: `/grilling` + `/domain-modeling` for grilling tickets, `/research` subagent for research tickets, `/prototype` for prototype tickets.
- **Locked engineering constraints (charting session, 2026-07-17):**
  1. **From-scratch astrology engine.** No astrology APIs, no third-party astrology libraries. Every astrological formula is derived from the classical texts and research, implemented by us, and carries a citation to its source. The engine is the product — this is a real startup product built on real domain understanding, not a wrapper.
  2. **The scratch line sits at astronomy.** Raw planetary positions come from real astronomical data (JPL/NASA ephemerides via an astronomy library such as Skyfield, MIT-licensed). Everything astrological above that — ayanamsha correction, nakshatra/naal, lagna & houses, vargas, panchanga, Vimshottari dasha, prashna — is built from scratch by us.
  3. **Stack:** Python backend (engine + API), TypeScript mobile-first web frontend.
  4. **AI harness is provider-agnostic from day one:** abstraction over ≥2 LLM providers; the model is chosen by evals on chart-grounded readings, not by default.
  5. **Working arrangement:** solo founder + AI agents — the founder does the domain learning and judgment calls (reviews every astrology rule), agents do implementation legwork.
  6. **Validation oracles:** Jagannatha Hora for chart/dasha ground truth; Mathrubhumi/Manorama printed panchangam for panchanga output.
  7. Swiss Ephemeris licensing is **moot** — constraint 2 avoids it entirely.
- Open product-map tickets gate parts of this map: pricing (wallet engineering), guardrail policy (enforcement table), consultation UX (session engineering). Cross-map blockers are noted in ticket bodies, not `blocked-by` (ids don't cross maps).

## Decisions so far

<!-- one line per closed ticket: gist + link -->

- [Astronomy layer spike](tickets/001-astronomy-layer-spike.md) — Skyfield (MIT) + JPL DE421 is the astronomy source; our from-scratch Lahiri ayanamsha matches the JHora-published table to ≤0.6″ (2000–2026); lagna from first principles works; default true node (both implemented). Asset: [`spikes/astronomy-layer/`](../../spikes/astronomy-layer/README.md). Unblocks [Engine architecture & API contract](tickets/004-engine-architecture.md).
- [DPDP obligations for birth-data — research](tickets/011-dpdp-research.md) — birth data is NOT sensitive under DPDP (no such category exists); substantive DPDP obligations bind only from ~May 2027; hosting outside India is lawful; the real special-category exposure is UK/EU GDPR Art. 9 for diaspora users. Full findings in [`docs/research/dpdp-birth-data-compliance.md`](../../research/dpdp-birth-data-compliance.md). Unblocks [Data model & DPDP posture](tickets/008-data-model-dpdp.md).
- [Primary IA pattern — chat-first vs dashboard](tickets/014-ia-pattern-chat-vs-dashboard.md) — closed by reference to the product map's [Daily practice card resolution](../tickets/009-daily-practice-card-design.md): dashboard-leaning hybrid, "Today" daily card as home, chat reached via a single CTA, jathakam/pariharam/panchangam as drawer rooms, no tab bar. No separate comparison prototype built. Unblocks [UI/UX design — mobile-first visual language & key surfaces](tickets/013-ui-ux-mobile-first.md).
- [UI/UX design — mobile-first visual language & key surfaces](tickets/013-ui-ux-mobile-first.md) — narrowed and closed on the **South Indian square chart rendering convention** only: fixed clockwise boxes with diagonal lagna mark; Malayalam vocabulary in Latin script for signs/planets ("Chovva", "Idavam"); name-only box density (no inline degree/retrograde/nakshatra); tap-to-reveal detail sheet carries degree, retrograde, nakshatra+pada, and the English name — the only place English appears. Chat UI and the full jathakam page layout (panchanga block + dasha table) deferred to [Chat UI & jathakam page layout](tickets/015-chat-ui-jathakam-layout.md).

## Not yet specified

- **Wallet & payments engineering** — payment gateway, credit ledger, INR/foreign currency. Product pricing resolved 2026-07-18 ([resolution](../tickets/002-pricing-free-tier.md)): ₹25/credit, $0.99 diaspora, 2 free credits, singles + plain ₹100 = 4 recharge, no packs/bonuses during validation — now specifiable as a ticket.
- **Guardrail implementation detail** — the per-topic enforcement table and its harness wiring. Product policy resolved 2026-07-18 ([full ruling table](../tickets/004-guardrail-policy.md)): engage/hedge/refuse rulings per topic, hard refusals (death-timing, fetal sex under PCPNDT, diagnosis/treatment), distress protocol with helpline routing (Kerala/national/diaspora) + disclosed founder-alert flagging, third-party charts refused (user's own birth data only — simplifies the data model), persistent AI marker + disclaimer surfaces — now specifiable as a ticket.
- **Consultation-session engineering** — session state, credit-consumption events, transcript storage. Consultation UX resolved 2026-07-18 inside the [pricing resolution](../tickets/002-pricing-free-tier.md): concern-scoped session, credit consumed at open, edges = resolution wrap-up / 48h inactivity / ~30–40-message soft cap, transcripts readable forever — now specifiable as a ticket.
- **Prashna-mode engineering depth** — which Prashna Marga methods are computable vs AI-interpreted, arudha/ashtamangala input UX. Sharpens after doctrine extraction from Prashna Marga (texts must be acquired and read first).
- **Malayalam vocabulary data layer** — canonical codes + locale-aware label tables (naal names, graha names, Latin-script Malayalam). Sharpens with the engine architecture and API contract.
- **Concierge admin & observability** — founder-facing view of live consultations, transcript review, flagging. Sharpens after consultation-session engineering. Validation metrics resolved 2026-07-18 ([resolution](../tickets/001-validation-metrics.md)) add a hard instrumentation requirement from day one: per-user card opens, consultation counts and session edges, and payment records — the go/no-go reads off these.
- **Wellness-layer engineering** — daily-practice-card generation (chart + dasha + panchangam → card), practice-content storage, TTS pipeline (if TTS chosen), streak tracking, and distress-signposting enforcement in the harness. Product map added the wellness layer 2026-07-18 (map decisions 10–16); sharpens when the product map's [Practice library — content definition](../tickets/008-practice-library-content.md) and [Daily practice card — design prototype](../tickets/009-daily-practice-card-design.md) resolve.
- **Build sequence & spec assembly detail** — the final ordering of implementation slices; the closing ticket [Assemble the engineering spec](tickets/012-assemble-spec.md) exists, but its internal structure sharpens as decisions land.

## Out of scope

- **Porutham engine** — product map deferred porutham out of MVP; the koota tables return post-validation.
- **Malayalam-script locale** — later locale per product decision 5.
- **Native mobile apps** — phase 1 is mobile-first web.
- **Post-validation scaling & productionization** — the spec targets the 20–50-user concierge MVP; scale engineering is a later effort.
- **Swiss Ephemeris professional licensing** — mooted by locked constraint 2 (astronomy via MIT-licensed sources, astrology from scratch).
