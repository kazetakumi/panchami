---
id: 005
title: Competitor landscape — Kerala/Malayalam astrology apps & AI astrologers
label: wayfinder:research
status: closed
assignee: research-subagent (fired 2026-07-17, charting session; resolved 2026-07-17)
blocked-by: []
---

## Question

Who already serves this market and how? Survey: (a) Astrotalk and the big Indian astrology platforms — pricing anchors (per-minute rates, wallet mechanics), whether they offer Malayalam/Kerala-method consultations; (b) Kerala/Malayalam-specific astrology apps and sites (jathakam generators, panchangam apps, matrimony porutham tools) — features, pricing, quality; (c) existing AI-astrologer products in India and globally — positioning, pricing, how they handle disclosure and guardrails; (d) gaps: what nobody offers that our locked product definition does. Output: findings doc in docs/research/ with pricing table and a differentiation summary.

## Resolution (2026-07-17)

Full findings: [`docs/research/competitor-landscape.md`](../../research/competitor-landscape.md).

- **Big platforms:** all run wallet recharge + per-minute human consults (₹10–₹250+/min). Astrotalk ~₹1,214 Cr FY25 revenue, 17% NRI, 160-currency checkout — but positions AI as assistive only. Malayalam exists everywhere only as a language *filter* on human astrologers; **no platform productizes the Kerala method** (prashna, 10-porutham, Kerala chart conventions).
- **Kerala players:** ClickAstro/Astro-Vision own Malayalam jathakam artifacts (PDF reports ₹520–₹1,500; LifeSign is the astrologer-standard software) but have no conversational product and no shipped AI. Prokerala owns free Kerala-convention tools + a licensable API. Manorama/Mathrubhumi set the free-panchangam bar.
- **AI astrologers:** AstroSage is the most aggressive incumbent — AI chat + voice in 8 Indian languages, **Malayalam not among them**. Vedic AstroGPT (₹49/question), KundliGPT, Melooha (funded). Co-Star is the Western honest-LLM benchmark ($9–15/mo).
- **The gap:** honest-AI × Kerala-method × Malayalam-vocab-in-Latin-script × prashna × diaspora is **empty**; interactive prashna exists nowhere. Top threats in order: AstroSage adding Malayalam (config-level change for them), Astrotalk fast-following (constrained by human-revenue cannibalization), ClickAstro+Matrimony.com bolting an LLM onto LifeSign (best data, slowest org).
- **Pricing anchors** (for [Pricing & the free-tier boundary](002-pricing-free-tier.md)): AI question floor ₹27–49; human session ₹500–1,500; Malayalam report ₹520–1,500; NRI clears $0.65+/min.
- One unverified item flagged in the doc: "ClickVedicAstro.com" claims Astro-Vision-powered AI avatars but its relation to the official ClickAstro line is unconfirmed.
