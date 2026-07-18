---
id: 008
title: Data model & DPDP posture
label: wayfinder:grilling
status: open
assignee:
blocked-by: [011]
---

## Question

Decide the persistent data model and the privacy posture around it. **Premise corrected by the DPDP research (ticket 011): DPDP has no sensitive-data category — birth data is ordinary personal data under Indian law; the elevated handling is driven by product positioning and by UK/EU GDPR Art. 9 (religious/philosophical beliefs → explicit consent) + UAE PDPL for diaspora users.** Entities in play: user/account, birth profile (date-time-place), computed chart artifacts (store vs recompute; dasha trees precompute), consultations & transcripts, wallet/credit ledger stub (schema slot only — real design waits on product pricing), consent records (AI disclosure + birth-data consent per DPDP). To decide: what's encrypted at rest and how; data residency implications for the infra ticket; retention & deletion (DPDP right-to-erasure vs wanting transcripts for eval/improvement); whether third-party charts (asking about a spouse/child) are modeled — the product map's guardrail ticket has the consent angle, this ticket has the schema angle. Blocked by the DPDP research ticket, which surfaces the actual legal obligations first.
