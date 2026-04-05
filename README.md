# DriftLoop
An LLM-powered DevOps system that connects code changes, runtime behavior, and incident signals into one explainable loop.
DriftLoop is a DevOps incident reasoning POC that connects infra intent, runtime behavior, and incident evidence.

It helps answer:
- What changed?
- What broke?
- Why did it break?
- What should we fix?

DriftLoop ingests:
- Git/PR changes
- Kubernetes events
- logs
- metrics

Then it builds a time-aligned system view and uses an LLM to explain the incident with evidence.
