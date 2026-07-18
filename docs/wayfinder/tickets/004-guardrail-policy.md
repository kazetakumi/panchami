---
id: 004
title: Per-topic guardrail policy
label: wayfinder:grilling
status: closed
assignee: akhil
resolved: 2026-07-18
blocked-by: []
---

## Question

Detail the moderate guardrails stance into an explicit per-topic ruling table the engineering map can implement. Topics needing a ruling (engage-with-hedging / deflect-to-professional / hard-refuse): health & disease queries, mental-health crises, death & longevity (hard floor: no death-timing), pregnancy & childbirth, marriage timing & divorce, legal disputes, financial/investment decisions, job & career, remedies/parihara (suggesting poojas — cultural authenticity vs monetization-of-fear concern), and queries about third parties (checking someone else's chart without consent — DPDP angle). Also: the standing disclaimer wording and AI-disclosure placement. Ground rulings in the research report §6 (Consumer Protection Act 2019, ASCI code, DPDP). **Wellness-layer additions (map decision 12, 2026-07-18): (i) wellness-claims line — practices are framed as wellness, never treatment; no "reduces anxiety/stress" outcome claims, no diagnosis language anywhere in product or marketing; (ii) distress-signposting protocol — how the AI recognizes a user in real distress (in consultation chat or around practices) and what it does: response wording, professional-help signposting (which helplines for Kerala vs diaspora?), and whether/how the founder is alerted during the concierge phase.**

## Resolution (2026-07-18)

### Per-topic ruling table (implementable by the engineering map)

| Topic | Ruling | Detail |
|---|---|---|
| Job & career | Engage | Bread-and-butter; dasha/transit framing, standard hedging. |
| Marriage timing, divorce | Engage, hedged | Core use case; traditional windows; never "your marriage will fail" determinism. |
| Legal disputes | Engage, hedged | Vyavahara framing: favorable/unfavorable periods only, never outcomes; "not legal advice" line applies. |
| Money & ventures | Engage, hedged | Favorable periods for ventures yes; specific investment instructions never; "not financial advice" line applies. |
| Health & disease | Engage narrowly | Traditional *tendencies* with wellness framing ("6th-house stress period; prioritize rest"); never name diseases, diagnose, or suggest remedies for medical conditions (Drugs & Magic Remedies Act adjacency); symptomatic queries always get "see a doctor." |
| Death & longevity | **Hard refuse timing** | Locked hard floor. Longevity anxiety met with empathy, redirected to health stewardship; ayur-dasha chapters excluded from permissible outputs. |
| Pregnancy & childbirth | Engage, hedged; **one hard refuse** | Santana timing questions engaged. **Fetal sex prediction hard-refused — PCPNDT Act criminalizes sex-determination communication. Non-negotiable.** No miscarriage/complication predictions. |
| Mental distress | **Protocol, not prediction** | Drop the astrological frame, acknowledge, signpost: Kerala — DISHA 1056, Tele-MANAS 14416; national — KIRAN 1800-599-0019; diaspora — locale lines (US 988, UK 116 123). Never predict on suicidal/self-harm topics. |
| Remedies / pariharam | Safe-mantra scope only | Per the [authenticity resolution](006-cultural-authenticity-review.md): cited practices, practice-framed never remedy-framed. **The AI never prescribes poojas, temple services, or paid rituals** — the monetization-of-fear line; we sell nothing there. |
| Wellness claims | **Hard floor** | Map decision 12: wellness language only; never diagnosis or treatment claims, in product or marketing. |
| Third-party charts | **Refuse in MVP** | No birth details but the user's own. When asked about another person, the AI refuses the chart **but may point at prashna mode** (questions without a birth chart — the querent's own session). Family-framing-with-attestation is the post-validation revisit. Simplifies DPDP posture: only user's own birth data processed. |

### Distress protocol — concierge-phase tail

**Founder alerts ON, disclosed.** Any distress-protocol trigger flags the transcript for immediate founder review — operational safety QA plus duty-of-care at community scale. Onboarding states in plain words that flagged safety conversations may be reviewed by the founder during the early phase. Policy revisited post-validation.

### Disclosure & disclaimer

- **AI disclosure:** plain sentence on the onboarding welcome screen before any consultation ("Your astrologer is an AI, trained in Kerala jyothisham" — the brand headline doing legal duty) + persistent visible "AI" marker in the consultation header. Never buried in ToS.
- **Standing disclaimer:** one calm line, persistently visible on consultation and jathakam/report views: *"Guidance rooted in traditional Kerala jyothisham — not medical, legal, or financial advice."* Short by design — confidence, not fear.
- **Exact wording** (consent, disclosure, distress-review line; English now, Malayalam later) is drafted-to-react-to in the graduated ticket [Onboarding & consent copy](011-consent-disclosure-copy.md).

**Consequences:** engineering map's guardrail-enforcement fog is now specifiable (this table is the spec input); DPDP-consent-copy fog graduates → ticket 011; third-party-chart refusal simplifies the data model (user's own birth data only).
