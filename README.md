# Panchami (codename: astrochat)

An AI astrologer grounded in Kerala jyothisham, wrapped in a wellness layer
(psychological framing + daily practices rooted in pariharam/sankalpa) that
turns episodic consultation into a daily habit.

Target user: Malayalis — Kerala + Gulf/US/UK diaspora. Hero use case: AI
consultation chat grounded in birth chart, dasha, and transits.

This repo is currently a **planning + research workspace**, not a running
app. It holds the product and engineering definitions plus early feasibility
spikes; no production build exists yet.

## Repo layout

- [`docs/wayfinder/map.md`](docs/wayfinder/map.md) — product definition map:
  locked product decisions, resolved tickets, open questions.
- [`docs/wayfinder/engineering/map.md`](docs/wayfinder/engineering/map.md) —
  engineering spec map: architecture, data model, and build-sequence
  decisions for the concierge MVP.
- [`docs/wayfinder/tickets/`](docs/wayfinder/tickets/) and
  [`docs/wayfinder/engineering/tickets/`](docs/wayfinder/engineering/tickets/)
  — individual decision tickets tracked as local markdown (see each map's
  frontmatter for the tracker convention).
- [`docs/research/`](docs/research/) — domain research: Kerala astrology
  domain notes, competitor landscape, DPDP birth-data compliance.
- [`spikes/`](spikes/) — throwaway feasibility code:
  - [`astronomy-layer/`](spikes/astronomy-layer/README.md) — from-scratch
    ayanamsha/lagna/nakshatra computation on top of Skyfield + JPL DE421,
    validated against Jagannatha Hora and Drik Panchang.
  - `practice-card-prototype/` — HTML/CSS exploration of the daily
    practice-card home screen.

## Key locked decisions

- **From-scratch astrology engine.** No astrology APIs or third-party
  astrology libraries. Raw planetary positions come from real astronomical
  data (JPL DE421 via Skyfield, MIT-licensed); everything astrological above
  that — ayanamsha, nakshatra, lagna, panchanga, dasha, prashna — is derived
  from classical texts and implemented from scratch, with citations in code.
- **Stack:** Python backend (engine + API), TypeScript mobile-first web
  frontend.
- **Monetization:** Freemium + wallet credits, validated with real money
  (no mock checkout) against a pre-committed build/pivot/stop gate.
- **Guardrails:** hard floors regardless of topic — no death-timing
  predictions, no medical-cure claims, no diagnosis/treatment language.

See [`docs/wayfinder/map.md`](docs/wayfinder/map.md) for the full decision
record and rationale.
