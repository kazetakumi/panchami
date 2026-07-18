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

## Progress so far (paused 2026-07-18)

Four decisions landed by grilling; one sub-question remains open. Resume on that, not the settled points below.

1. **Marketing/SEO split**: `panchami.app` (or whatever the marketing domain becomes) is a **separate landing page** from `app.panchami.*`. SEO/shareability is the landing page's job, not the app's — this removes the "panchangam pages are shareable/SEO-relevant" pressure from the framework choice entirely. The app only needs to be a great app-like PWA/native app; no page inside it needs to rank in search.
2. **Framework: Expo + React Native, universal** (`react-native-web` for the browser target). One codebase targets web (phase 1), then iOS/Android (the actual destination) without a UI rewrite — phase 1 becomes a head start, not throwaway. Trade-off flagged: RN's StyleSheet model isn't full CSS — e.g. the jathakam/chat prototype's sticky-disclaimer `backdrop-filter: blur()` has no direct RN equivalent and needs an alternate treatment on both native and the RN-web build. Chart rendering (South Indian square, custom SVG) is fine via `react-native-svg`, which has a web-compatible mode under `react-native-web`.
3. **Offline stance: read-through cache only, not offline-first.** The daily card is server-generated (chart + dasha + today's panchangam) — nothing to compute client-side offline anyway. Honest offline story is "show yesterday's cached card with a staleness note," not a real sync engine. Matches the concierge MVP's 20–50 users with normal connectivity; no investment in background sync/conflict resolution.
4. **Data-fetching/state: TanStack Query for all server-state** (chart, panchanga, dasha tree, chat, wallet) — gives the read-through cache from decision 3 close to for free (stale-while-revalidate, cache persistence, works the same on Expo web and native). **Plain React state/context for local UI-only state** (drawer open/closed, composer input) — no Redux/Zustand; there's little client-only global state to justify one.

**Still open**: where canonical-code → locale-label resolution happens in the stack (backend API response already carries resolved Latin-script Malayalam labels, vs. frontend/data-layer resolves codes against a label table it owns) — product decision 5's Latin-script-now/Malayalam-script-later locale strategy needs a home. Resume here.
