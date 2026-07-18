---
id: 014
title: Primary IA pattern — chat-first vs dashboard
label: wayfinder:prototype
status: closed
assignee: akhil (claimed 2026-07-18, resolved 2026-07-18)
blocked-by: []
---

## Question

Decide the app's primary information-architecture pattern before any visual-language details are locked. Candidates: **chat-first** (the AI consultation is the home surface; jathakam/panchanga are reachable from within or alongside the chat) vs **dashboard** (a home screen surfaces chart/panchanga/dasha at a glance, chat is one destination among several) vs a hybrid. This shapes navigation chrome, how method-citations surface, and where the chart/panchanga views live relative to the conversation. Build a minimal, rough, mobile-first prototype (HTML/CSS, throwaway) showing both patterns applied to the key surfaces (home, jathakam, chat) so the founder can react to something concrete rather than a text description. Resolution records the chosen pattern and why; the prototype is linked as an asset. Unblocks [UI/UX design — mobile-first visual language & key surfaces](013-ui-ux-mobile-first.md), which was paused pending this.

## Resolution (2026-07-18)

Resolved by reference rather than a fresh comparison prototype: the product map's [Daily practice card — design prototype](../../tickets/009-daily-practice-card-design.md) (closed 2026-07-18, one day after this ticket was claimed) already settled the pattern through concrete, iterated prototype work.

**Pattern: dashboard-leaning hybrid.** "Today" (the daily practice card) is the home surface — chart/dasha/panchangam-derived content at a glance, not the chat. Chrome is a wordmark + profile chip opening a right side-drawer (identity as naal), with Jathakam / Pariharam / Panchangam as drawer-accessible rooms — no tab bar. Chat is one destination, reached via a single violet CTA ("Speak to Panchami"), not the home surface itself.

Consequence for [UI/UX design — mobile-first visual language & key surfaces](013-ui-ux-mobile-first.md): the drawer + rooms navigation chrome and the frozen home-screen tokens (Kanikkonna/Kadukka/gold/rust/rose/violet) carry forward as fixed; that ticket's remaining scope is chat UI visual/interaction design, the jathakam/grahanila layout, and the South Indian square chart rendering convention — the IA shell around them is no longer open.

No new prototype asset was produced; the decision rides entirely on ticket 009's asset ([artifact](https://claude.ai/code/artifact/82df65e6-1714-4c38-99f9-18ca0c7ba53c), [`spikes/practice-card-prototype/`](../../../../spikes/practice-card-prototype/)).
