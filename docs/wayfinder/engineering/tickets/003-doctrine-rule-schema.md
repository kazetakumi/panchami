---
id: 003
title: Doctrine rule schema — how the texts become engine rules and AI knowledge
label: wayfinder:grilling
status: open
assignee:
blocked-by: [002]
---

## Question

Design the structure that turns classical doctrine into something the engine computes and the AI cites. To decide: the rule format (JSON/YAML rule objects with fields like source citation (text, chapter, verse), the rule's computable condition, its interpretation text, confidence/tradition tags); which doctrine is **computed** (dasha lengths, koota tables, yoga conditions — deterministic) vs **retrieved** (interpretive passages the AI grounds readings in); how Kerala-specific rulings (e.g., chovva dosham's 2nd-house rule) are flagged against pan-Indian doctrine; the extraction workflow (founder reads → agent-assisted structuring → founder reviews every rule, per the working arrangement); and how citations surface in the product (the "visibly demonstrating the method" positioning). Copyright constraint from ticket 002 applies: paraphrase-only, rules-as-facts. Use /domain-modeling — this schema IS the ubiquitous language of the engine.

**Paused 2026-07-18:** opened with a grilling session on the computed-vs-interpretive split (first candidate: pair a computable condition with its interpretation as one rule type for yogas/doshas/combinations, plus a separate passage-only type for pure interpretive text). The founder doesn't yet have the domain familiarity to make this call — it needs actual time with the classical texts first. **Blocked-by [Acquire the core jyothisham texts](002-acquire-core-texts.md)** added; resume once the founder has read enough to judge the split with real examples in hand.
