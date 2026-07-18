---
label: wayfinder:map
title: AI Kerala Astrologer — Product Definition
created: 2026-07-17
tracker: local-markdown (tickets in ./tickets/, blocking via frontmatter `blocked-by`, claim via `assignee`)
---

# AI Kerala Astrologer — Product Definition

## Destination

A **validated product definition** for an Astrotalk-like app whose astrologer is an AI grounded in Kerala jyothisham, wrapped in a **wellness layer** (psychological framing + daily practices rooted in pariharam/sankalpa) that turns episodic consultation into a daily habit: every product decision made and a validation plan on paper, ready to hand to a second wayfinder map (engineering) that charts the concierge-MVP build. This map decides **what** the product is and **how we'll know it works** — it builds nothing and makes no engineering decisions.

## Notes

- Domain research lives at [`docs/research/kerala-astrology-domain-research.md`](../research/kerala-astrology-domain-research.md) — consult before any ticket touching tradition, legality, or computation feasibility.
- Skills to use per ticket type: `/grilling` + `/domain-modeling` for grilling tickets, `/research` subagent for research tickets, `/prototype` for prototype tickets.
- **Locked product decisions (charting session, 2026-07-17):**
  1. **Target user:** Malayalis — Kerala + Gulf/US/UK diaspora.
  2. **Hero use case:** AI consultation chat grounded in birth chart + dasha + transits.
  3. **Monetization:** Freemium + wallet credits (Astrotalk-familiar recharge behavior).
  4. **AI positioning:** Honest headline — "AI trained in Kerala jyothisham"; sells 24/7 access, no per-minute clock, privacy. Credibility via visibly demonstrating the method (naal, Prashna Marga grounding).
  5. **Language:** English prose + Malayalam astrological vocabulary in Latin script (naal, dasha, Thiruvonam…); canonical codes + locale-aware labels under the hood; full Malayalam script is a later locale.
  6. **Validation method:** Concierge MVP, 20–50 invited Malayali users; measure return visits and willingness to pay.
  7. **MVP scope:** Core loop (birth details → chart → AI chat) + jathakam view + prashna mode + daily panchangam/transits **+ wellness layer (see decision 15) + panchangam calendar view (month grid: naal, rahu/gulika/yamakanda kalam, Kollavarsham — added by the [pricing resolution](tickets/002-pricing-free-tier.md), free tier)**. Porutham deferred.
  8. **Guardrails stance:** Moderate — engage difficult topics with hedging, don't refuse; **hard floors regardless: no death-timing predictions, no medical-cure claims.** Per-topic detail in [Per-topic guardrail policy](tickets/004-guardrail-policy.md).
  9. **Map scope:** Product definition only; engineering is a second map.
- **Locked wellness-layer decisions (evolution grilling, 2026-07-18)** — astrology + psychology + manifestation, resolved as an *additive retention layer*, not a pivot:
  10. **Driver:** retention. Consultation apps are episodic (users come when anxious); the wellness layer makes the product a daily habit between consultations.
  11. **Kerala core survives intact:** Malayali target, Kerala method, honest-AI positioning, empty competitive quadrant — all unchanged. **Pariharam** is the cultural anchor for practices (the tradition already prescribes mantras/disciplines as remedy); **sankalpa** for intentions.
  12. **Psychology = framing + wellness-grade practices:** chart/dasha insights explained in the language of mind and emotion, plus meditation/mantra/journaling practices. **New hard floor:** wellness language only — never diagnosis, never treatment claims ("reduces anxiety" is out), signpost professional help when a user shows real distress.
  13. **No manifestation language in-product:** *sankalpa* (chart-aware intention-setting) is the product vocabulary; honest psychology ("self-talk shapes attention and behavior") is the explanation underneath. Never "the universe will deliver." "Manifestation" may appear in marketing copy only, if at all.
  14. **Hero unchanged, loop added:** consultation chat remains the hero and the monetization moment. The **daily practice card** — today's naal + a short practice + the user's sankalpa, generated from chart + current dasha + today's panchangam — is the retention loop, and it feeds the chat ("your practice mentioned Sani pressure — ask about it").
  15. **Wellness MVP depth:** full suite *shape* at minimum viable *depth* — daily practice card + a small curated library of 8–12 culturally vetted practices (text or TTS, no studio audio) + lightweight streaks. Guided-audio production, big libraries, reminders: post-validation.
  16. **Wellness is free in the MVP:** one conversion story — daily card → habit → question arises → paid consultation. A subscription tier for wellness content is a *post-validation possibility* noted in the pricing ticket, not a decision.

## Decisions so far

<!-- one line per closed ticket: gist + link -->

- [Competitor landscape — Kerala/Malayalam astrology apps & AI astrologers](tickets/005-competitor-landscape.md) — the honest-AI × Kerala-method × Malayalam × prashna × diaspora quadrant is empty; no incumbent ships Malayalam AI astrology; pricing anchors captured (AI question floor ₹27–49, human session ₹500–1,500). Full findings in [`docs/research/competitor-landscape.md`](../research/competitor-landscape.md). Unblocks [Pricing & the free-tier boundary](tickets/002-pricing-free-tier.md) and [Brand & name](tickets/007-brand-and-name.md).
- [Cultural authenticity review — practitioner involvement](tickets/006-cultural-authenticity-review.md) — no practitioner review for the MVP; the check is internal and citation-grounded (founder learns from the texts, AI interprets only from the cited knowledge base, never invents pariharam) plus a safe-mantra scope (well-documented mantras only, practice-framed never remedy-framed, no temple-ritual territory); no concierge authenticity feedback loop — founder reviews and tests against sources; credibility copy cannot claim practitioner review; practitioner advisor is a post-validation upgrade. Unblocks [Practice library — content definition](tickets/008-practice-library-content.md).
- [Pricing & the free-tier boundary](tickets/002-pricing-free-tier.md) — 1 credit = 1 concern-scoped consultation (prashna included; ends on resolution / 48h inactivity / soft cap with graceful wrap-up — resolves the consultation-UX fog); 2 free credits per new user; ₹25/credit ($0.99 diaspora) as *validation pricing, not the business model*; no packs or bonus credits during validation (₹100 = 4 plain recharge allowed); free tier = chart + jathakam view + daily practice card + panchangam calendar (new MVP scope: naal, rahu/gulika/yamakanda kalam, Kollavarsham), and "what does this mean for me?" is where paid begins. Unblocks [Validation metrics](tickets/001-validation-metrics.md); graduates onboarding fog → [Onboarding flow](tickets/010-onboarding-flow.md).
- [Brand & name](tickets/007-brand-and-name.md) — the product is a character: **Panchami**, an ageless, openly virtual AI astrologer named in homage to the mother of the Parayi Petta Panthirukulam ("astrology for every Malayali home"); voice = the psychologically fluent astrologer (astrologer's authority, psychologist's ear, no costume, no chirp — her character sheet feeds prompt design); disclosure doubles as her introduction; domains panchami.app/.ai + askpanchami pending registrar verification via [task 012](tickets/012-brand-verification.md); "astrochat" stays a codename.
- [Per-topic guardrail policy](tickets/004-guardrail-policy.md) — full ruling table locked (engage-with-hedging core topics; hard refusals: death-timing, fetal sex prediction under PCPNDT, diagnosis/treatment claims; pariharam stays in safe-mantra scope, AI never prescribes poojas; third-party charts refused in MVP with a prashna redirect); distress protocol with Kerala/national/diaspora helplines and **disclosed** founder alerts during concierge; AI disclosure on the welcome screen + persistent "AI" marker; one-line standing disclaimer. Graduates consent-copy fog → [Onboarding & consent copy](tickets/011-consent-disclosure-copy.md); the engineering map's enforcement table is now specifiable.
- [Daily practice card — design prototype](tickets/009-daily-practice-card-design.md) — the "Today" home screen locked via iterative prototype ([asset](https://claude.ai/code/artifact/82df65e6-1714-4c38-99f9-18ca0c7ba53c)): tear-off calendar-sheet grammar (serif date, Velli/Friday, naal row, 3-column kalam strip) → tailored note on a warm-rose card, signed — Panchami, no veil (fresh page IS the reveal) → single violet CTA "Speak to Panchami"; chrome = wordmark + profile chip → right side-drawer (identity as naal); tokens frozen (Kanikkonna/Kadukka/gold/rust/rose/violet, light-first); deck cards, reveals, tab bars, dual CTAs all explored-and-rejected in the ticket; watch-items: retention rides on writing quality, pariharam hidden in drawer. Graduates streak fog → [Pariharam screen — design prototype](tickets/013-pariharam-screen.md).
- [Validation metrics — what numbers make "validated" true](tickets/001-validation-metrics.md) — real money, no mock checkout (₹25 UPI / $0.99 link); 4-week window with retention read in weeks 3–4; gates: ≥30% of free-credit exhausters pay (guard-rail ≥50% exhaust, floor ≥8 payers, ≥3 repeat) and ≥40% of activated users open the daily card ≥3 days/week in weeks 3–4, with ≥60% holding a second consultation; a pre-committed 2×2 (payment × card-return) decides build/pivot/stop; week-4 founder verdict resolves the validation-playback fog; two-question end survey (Sean Ellis + recommend-to-family) is diagnostic, never gating.

## Not yet specified

<!-- Consultation UX shape: resolved inside the pricing ticket (002), 2026-07-18. Onboarding: graduated to ticket 010. -->
<!-- Validation playback: resolved inside the validation-metrics ticket (001), 2026-07-18 — week-4 founder verdict against pre-registered thresholds. -->
<!-- Streak & habit mechanics: graduated to ticket 013 (pariharam screen) by the home-screen resolution (009), 2026-07-18. -->
<!-- DPDP consent copy: graduated to ticket 011 by the guardrail resolution (004), 2026-07-18. -->

## Out of scope

- **All engineering decisions** (stack, ephemeris/licensing route, AI harness architecture, hosting) — the second map's territory; this map hands it the product definition. That map now exists: [AI Kerala Astrologer — Engineering Spec](engineering/map.md) (charted 2026-07-17).
- **Porutham (marriage matching)** — deferred out of MVP scope by charting decision 7; returns as a post-validation feature effort.
- **Malayalam-script locale** — later locale per charting decision 5.
- **Native mobile apps** — phase 1 is mobile-first web.
- **Human-astrologer marketplace** — the product's premise is no human astrologers.
- **Post-validation wellness expansion** — studio-recorded audio, large practice libraries, reminders/notifications, and a wellness subscription tier (noted as a possibility in [Pricing & the free-tier boundary](tickets/002-pricing-free-tier.md)); returns as a post-validation effort per decision 15/16.
- **Mental-health companion features** — mood tracking, clinical outcomes language, therapeutic interventions; ruled out by decision 12's hard floor (wellness language only, never treatment).
- **Practitioner advisor engagement** — ruled out for the MVP by the [authenticity-review resolution](tickets/006-cultural-authenticity-review.md); returns as a post-validation upgrade, especially if the concierge run surfaces authenticity problems.
