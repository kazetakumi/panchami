---
id: 011
title: DPDP obligations for birth-data — research
label: wayfinder:research
status: closed
assignee: research-subagent (fired 2026-07-17, charting session; resolved 2026-07-17)
blocked-by: []
---

## Question

What does the DPDP Act 2023 (and its Rules, as notified) actually require of an app storing birth date-time-place, consultation transcripts, and payment data for Indian users — and what changes when diaspora users (Gulf/US/UK) are added? Surface: whether astrological birth data is sensitive/special-category under DPDP; consent requirements (form, language, granularity, withdrawal); data-residency/cross-border transfer rules; erasure & retention obligations; breach notification; obligations size-dependent thresholds (Significant Data Fiduciary criteria — do we clear them at concierge scale?); GDPR overlap for UK/EU diaspora; and concrete implications: what the consent screen must say, what must be encrypted, what must be deletable. Output: findings doc in docs/research/ with citations to the Act/Rules text and reputable legal analyses. The data-model ticket (008) waits on this.

## Resolution (2026-07-17)

Full findings: [`docs/research/dpdp-birth-data-compliance.md`](../../../research/dpdp-birth-data-compliance.md).

- **Timeline:** DPDP Rules 2025 notified Nov 2025; substantive obligations (consent, notice, breach, erasure, rights) bind only from **~May 2027**. Until then the SPDI Rules 2011 are the operative law. The concierge MVP launches under the old regime but should build to the new one.
- **Headline correction:** DPDP has **no sensitive-data category** — birth date-time-place is ordinary personal data under Indian law. Elevated handling is justified by product positioning + diaspora law, not Indian statute. (The data-model ticket's premise was updated accordingly.)
- **Consent:** itemised, standalone, purpose-specific notice; must be available in English or any Eighth-Schedule language (Malayalam qualifies); withdrawal as easy as grant; grievances ≤90 days.
- **Cross-border:** blacklist model with no country blacklisted — hosting outside India is lawful. Only payment data has RBI localization, binding the gateway, not us.
- **Erasure vs eval transcripts:** anonymization takes data out of DPDP scope, but no statutory anonymization standard exists — interpretive position; birth timestamps are quasi-identifiers and must be generalized in any eval corpus.
- **Breach:** notify the Board + every affected user without delay, detailed report in 72h, no materiality threshold. Top penalties ₹200–250 crore.
- **The real asymmetry is diaspora:** UK/EU users bring UK GDPR via the targeting test, and astrology-consultation data plausibly hits **Art. 9 (religious/philosophical beliefs) → explicit consent**; UAE PDPL treats religion data as sensitive. One explicit, granular consent flow satisfies all regimes.
- Report includes a consent-screen spec, minimum-viable compliance checklist, and a data-model implications section addressed to the data-model ticket (consent events append-only, subject-type discriminator for third-party charts, dual-lifecycle transcripts, recompute-over-store for chart artifacts).
