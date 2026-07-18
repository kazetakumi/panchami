---
id: 007
title: Reading-quality eval harness — how we know the astrologer is good
label: wayfinder:grilling
status: open
assignee:
blocked-by: [006]
---

## Question

Locked constraint: the LLM is chosen by evals, not by default — so decide what the evals ARE. To decide: the eval dimensions (doctrinal correctness — does the reading match what the chart + rules actually say; method visibility — does it cite naal/dasha/lagna correctly; Kerala authenticity — vocabulary, conventions; guardrail compliance; tone per brand voice once the product map decides it); the eval set (N charts × M question types, including prashna-mode and difficult-topic probes); grading method (founder rubric review vs LLM-judge vs practitioner review — ties into the product map's cultural-authenticity ticket); and the pass bar for a provider/model to be shippable. Blocked by the harness architecture — evals exercise the harness, and the provider comparison needs the abstraction in place conceptually.
