---
id: 010
title: Frontend technical architecture — framework, SSR, offline/PWA
label: wayfinder:grilling
status: open
assignee:
blocked-by: []
---

## Question

Decide the TypeScript frontend's technical shape (the plumbing, not the visual language — that's [UI/UX design — mobile-first visual language & key surfaces](013-ui-ux-mobile-first.md)). To decide: framework (Next.js vs alternatives — weigh SSR needs: panchangam pages are shareable/SEO-relevant, consultations are app-like); state/data-fetching architecture consuming the engine's canonical chart JSON contract (ticket 004); offline/PWA stance for the daily-panchangam retention hook; how canonical codes resolve to locale labels at the data layer (Latin-script Malayalam now, Malayalam script later per product decision 5 — the visual treatment of those labels belongs to the UI/UX ticket, this ticket decides where the resolution happens in the stack). Consultation-session flow detail waits on the product map's consultation-UX fog — this ticket decides the architectural frame, not the session screens.

Split off from the original combined ticket 2026-07-17: the UI/UX half (chart rendering convention, chat UI design, mobile-first component/design-token strategy) moved to ticket 013 so each stays session-sized.
