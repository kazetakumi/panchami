---
id: 002
title: Pricing & the free-tier boundary
label: wayfinder:grilling
status: closed
assignee: akhil
resolved: 2026-07-18
blocked-by: [005]
---

## Question

Within the locked freemium + wallet-credits model: what exactly is free, what consumes credits, and at what price points? To decide: what a free user gets (basic chart? N questions? full jathakam?), the unit a credit buys (per question, per consultation session, per report), credit pack sizes and INR/USD price points (diaspora pays in foreign currency), and whether daily panchangam is free (retention hook) or gated. Blocked by competitor landscape (005) — Astrotalk/Kerala-app price anchors inform the points. **Constraint from map decision 16 (2026-07-18): the wellness layer (daily practice card, practice library, streaks) is entirely free in the MVP — do not gate it. Record, but do not decide, the post-validation possibility of a wellness subscription tier alongside the wallet.**

## Resolution (2026-07-18)

**The unit: 1 credit = 1 concern-scoped consultation** (prashna included — a prashna session is a consultation type). A consultation opens when the user states their concern (credit consumed at open) and ends on the first of three edges: **resolution** (AI wraps up with a summary + a practice/sankalpa for the period), **48h inactivity** (transcript stays readable; reopening the concern later is a new session), or a **soft cap of ~30–40 user messages** with a graceful wrap-up, never a cut-off. Topic drift is handled socially (AI answers briefly, notes a new concern deserves its own consultation). This deliberately attacks the market's per-minute meter anxiety: "no clock — one credit, one concern, all your questions about it." **This also resolves the map's consultation-UX fog** (session-based; begins/ends/credit-consumption defined).

**Free credits: 2 per new user** (beats every incumbent's 1 free/₹1 session; keeps the paywall inside the concierge observation window so willingness-to-pay is actually measured).

**Price: ₹25/credit — validation pricing, not the business model.** Founder decision; recorded dissent: ₹25 for a full session sits below the market's single-AI-question floor (₹27–49, Vedic AstroGPT), so a post-validation price rise is baked in and must be treated as a deliberate later decision. The concierge question this price answers is "will Malayalis pay this AI *anything*?" — low friction serves that.

**Purchase mechanics: no packs, no bonus credits during validation** (bonuses muddy the willingness-to-pay reading). Credits bought singly at ₹25, or a plain ₹100 = 4 credits recharge for the Astrotalk-familiar gesture. **Diaspora: $0.99/credit** (standard purchasing-power premium; vs ~$13 for 20 human minutes at NRI rates).

**The free-tier boundary:**
- **Free forever:** birth chart + jathakam view (South Indian chart, dasha timeline, naal — matches Prokerala's free bar) · daily practice card (naal insight + sankalpa + practical panchangam-grounded caution + streaks) · **panchangam calendar** — month grid with each day's naal (Malayalam star), rahu kalam, gulika kalam, yamakanda kalam, Kollavarsham date; English prose + Malayalam terms. (Calendar added to MVP scope this session — it intercepts the existing daily Manorama/Mathrubhumi habit; quality bar is absolute: output must match the printed panchangam or credibility dies. Travancore/Malabar regional editions and full muhurtham tables deferred.)
- **Paid, 1 credit:** consultations only. The line: the free tier shows the *what* (chart, naal, kalams); "**what does this mean for me?**" starts a consultation.
- **Caution constraint** (inherited by the card prototype, ticket 009): daily cautions are practical and panchangam-factual ("rahu kalam 10:30–12:00; not the hour to sign") — never ominous dread next to a consult button; that's the monetization-of-fear dark pattern the honest-AI brand cannot touch.

**Consequences:** unblocks [Validation metrics](001-validation-metrics.md) (willingness-to-pay is now definable: recharge behavior after the 2 free credits at ₹25/$0.99). Onboarding fog graduates (consultation UX now defined) → new ticket [Onboarding flow](010-onboarding-flow.md). Post-validation: standard-price decision, packs/bonuses, wellness subscription tier possibility.
