---
id: 003
title: Doctrine rule schema — how the texts become engine rules and AI knowledge
label: wayfinder:grilling
status: open
assignee:
blocked-by: []
---

## Question

Design the structure that turns classical doctrine into something the engine computes and the AI cites. To decide: the rule format (JSON/YAML rule objects with fields like source citation (text, chapter, verse), the rule's computable condition, its interpretation text, confidence/tradition tags); which doctrine is **computed** (dasha lengths, koota tables, yoga conditions — deterministic) vs **retrieved** (interpretive passages the AI grounds readings in); how Kerala-specific rulings (e.g., chovva dosham's 2nd-house rule) are flagged against pan-Indian doctrine; the extraction workflow (founder reads → agent-assisted structuring → founder reviews every rule, per the working arrangement); and how citations surface in the product (the "visibly demonstrating the method" positioning). Copyright constraint from ticket 002 applies: paraphrase-only, rules-as-facts. Use /domain-modeling — this schema IS the ubiquitous language of the engine.
