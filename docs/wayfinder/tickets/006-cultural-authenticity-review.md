---
id: 006
title: Cultural authenticity review — practitioner involvement
label: wayfinder:grilling
status: closed
assignee: akhil
resolved: 2026-07-18
blocked-by: []
---

## Question

The research report (§6.8) recommends a practising Kerala astrologer review the interpretive content before launch — prashna digitization especially is culturally sensitive territory. Decide: do we engage a practitioner advisor for the MVP, and in what role (one-time content review, ongoing advisor, public endorsement for credibility copy)? If yes: how to find one open to an AI product (Kerala Jyothisha Parishath? Government Sanskrit College Thiruvananthapuram jyothisham department?), what we ask them to vet (AI reading samples, jathakam rendering, prashna mode framing, **and — per map decisions 11–15, 2026-07-18 — the wellness-layer content: mantra selection and correct usage, pariharam framing of practices, sankalpa wording; misused mantras are a sharper authenticity risk than prose readings**), and budget. If no: what's the alternative authenticity check before real users see readings?

## Resolution (2026-07-18)

**No practitioner review for the MVP.** The alternative authenticity check is internal and citation-grounded, two parts:

1. **Learn-then-interpret with citations.** The founder learns the tradition from the acquired classical texts; the AI interprets only from the built knowledge base; every practice, mantra, and interpretive claim carries a citation to its source. The AI never invents pariharam or doctrine. This extends the engine's citation ethos (engineering constraint 1) to interpretive and wellness content.
2. **Safe-mantra scope for the MVP.** The 8–12 practices use only widely known, well-documented mantras with published provenance, framed as practice ("a steadying practice for this period"), never as prescribed remedy. No temple-ritual or deva-prashna-adjacent territory.

Review and testing are done by the founder against sources — **explicitly no concierge-user authenticity feedback question** (considered and struck by the founder; validation runs without that loop).

**Consequences:**
- Credibility copy **cannot claim practitioner review** — constraint inherited by [Brand & name](007-brand-and-name.md).
- [Practice library — content definition](008-practice-library-content.md) is **unblocked**; its vetting workflow *is* this check (citation rule + safe-mantra scope + founder sign-off).
- Engaging a practitioner advisor remains a legitimate **post-validation upgrade**, especially if authenticity problems surface during the concierge run.

**Risk accepted knowingly** (grilled 2026-07-18): concierge users' families have astrologers; an authenticity failure in this community is a distribution failure; internal checks validate doctrine-as-written, not living practice. The founder accepts this for the pre-validation phase.
