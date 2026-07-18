---
id: 001
title: Validation metrics — what numbers make "validated" true
label: wayfinder:grilling
status: closed
assignee: akhil
resolved: 2026-07-18
blocked-by: [002]
---

## Question

The concierge MVP runs with 20–50 invited Malayali users. What measured outcomes constitute a validated product definition — the go/no-go thresholds for investing in the full build? Candidates to pin down: return-visit rate over what window, consultations per user, willingness-to-pay signal (real recharge vs mock checkout, conversion %), qualitative bar (would-be-very-disappointed score?), and the observation period length. **Wellness-layer addition (map decisions 10–16, 2026-07-18): distinguish *consultation return* from *daily-practice-card return* — the card exists to move the second number, and the pivot's retention hypothesis is unvalidated unless daily-card return is measured on its own.**

## Resolution (2026-07-18)

**Money is real.** When free credits run out, users pay actual money — ₹25 UPI/GPay (India) or $0.99 payment link (diaspora); a UPI ID and a spreadsheet suffice at concierge scale. No mock checkout: simulated intent is inflated intent, and willingness-to-pay is the burden of proof.

**Observation window: 4 weeks.** Week 1–2 usage is novelty; all retention metrics are read in **weeks 3–4 only**.

**Primary metric — payment (gates go/no-go):**
- **≥30% of exhausters pay.** Of activated users (completed chart + first consultation) who used both free credits, at least 30% pay for a third consultation.
- **Guard-rail: ≥50% of activated users exhaust both free credits** — otherwise demand failed upstream of pricing and the conversion read is moot.
- **Floor: ≥8 real paying users** (percentages lie at N=20–50).
- **Repeat signal: ≥3 users pay at least twice** — one payment can be politeness; a recharge is a customer.

**Retention metrics (gate go/no-go; the wellness pivot's own hypothesis):**
- **Daily-card return: ≥40% of activated users open the daily card ≥3 days/week during weeks 3–4.** Deliberately aggressive — the pivot's justification dies if the card is a week-1 toy.
- **Consultation depth: ≥60% of activated users hold ≥2 consultations** across the window (episodic-return baseline, contrast to card-driven return).

**Pre-committed 2×2 diagnostic** (written down now to prevent week-5 rationalization):
| | Payment hits | Payment misses |
|---|---|---|
| **Card-return hits** | **Build.** | Wellness works, consultation value doesn't → rethink monetization, keep the layer. |
| **Card-return misses** | Consultations work, retention thesis failed → keep the hero, cut the layer's cost. | **Stop.** |

**Playback (resolves the map's validation-playback fog):** end of week 4, the founder scores the pre-registered thresholds in the spreadsheet and writes a one-page verdict against the 2×2. The go/no-go follows the numbers unless a written case is made that a specific number lied.

**Qualitative — diagnostic only, never gating:** one end-of-window survey to all activated users, two questions: the Sean Ellis question ("How would you feel if you could no longer use this?", benchmark ≥40% "very disappointed") and "Would you recommend it to family — why / why not?". Explains the numbers and harvests brand language; behavior gates, words explain. Consistent with the [authenticity-review resolution](006-cultural-authenticity-review.md): no authenticity/content-vetting question is asked.

**Instrumentation consequence (engineering map):** card opens, consultation counts/edges, and payments must be tracked per user from day one of the concierge run. Blocked by pricing (002) because the willingness-to-pay metric can't be defined until what's paid-for is.
