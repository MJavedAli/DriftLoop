# DriftLoop

**DriftLoop** is a DevOps incident reasoning POC that connects **infrastructure intent**, **runtime behavior**, and **failure signals** into a single explainable system.

It explores a simple but under-addressed question:

> Can an LLM reason about DevOps systems — not just generate text about them?

---

## The Problem

Modern DevOps systems are inherently fragmented:

- **Infra intent** lives in Terraform / Helm / Pulumi  
- **Runtime behavior** emerges in Kubernetes, autoscaling, and service mesh  
- **Incidents** surface in logs, traces, and metrics  
- **Fixes** live in PRs and tribal knowledge  

These layers evolve independently, but failures do not.

As a result, debugging becomes a manual process of reconstructing system state across disconnected sources.

---

## What DriftLoop Does

DriftLoop builds a **closed-loop reasoning system** across DevOps layers.

It ingests:

- Git commits and PR changes (declared intent)  
- Kubernetes events (orchestration signals)  
- Logs and metrics (runtime evidence)  

It then:

1. **Aligns all signals into a time-based system timeline**
2. **Correlates change → behavior → failure**
3. **Detects drift between declared and observed state**
4. **Generates an explainable root-cause hypothesis**
5. **Suggests a safe corrective action**

---

## Key Idea

This project is not about log summarization.

It is about:

> **Correlating declared intent with observed runtime behavior under time and change pressure**

This is where most debugging time is spent — and where most tools fall short.

---

## Architecture Overview
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/6119ecb4-d284-4ff5-b015-c61201df60cd" />

---

## Example Scenario

A Helm change reduces CPU requests for a service.

Observed behavior:
- Autoscaler oscillation  
- Increased latency  
- Pod restarts  

DriftLoop correlates:
- The config change  
- The timing of deployment  
- Runtime metrics and events  

And produces:

- Root cause hypothesis  
- Supporting evidence  
- Suggested fix (e.g. adjust CPU request or HPA threshold)

---

## Tech Stack

- **Backend:** FastAPI  
- **Storage:** PostgreSQL + vector store (pgvector or similar)  
- **LLM Layer:** OpenAI (or compatible)  
- **Infra Simulation:** Docker Compose / Kubernetes  
- **Observability Inputs:** Prometheus, logs, K8s events  

---

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/driftloop.git
cd driftloop
```
### 2. Start dependencies

```bash
docker-compose up -d
```
Add your API key.

### Run
```
uvicorn src.api.main:app --reload
```

### Trigger analysis
```
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "service": "checkout",
    "start_time": "2026-04-05T10:00:00Z",
    "end_time": "2026-04-05T10:15:00Z"
  }'
  ```

### Project Structure

```
driftloop/
 ├── src/
 │   ├── api/           # FastAPI endpoints
 │   ├── ingest/        # Data ingestion (Git, K8s, logs, metrics)
 │   ├── normalize/     # Timeline construction
 │   ├── state/         # DB + vector store
 │   ├── reasoning/     # LLM orchestration
 │   ├── explain/       # Output formatting
 │   └── utils/         # Shared utilities
 ├── demo/              # Sample incident + events
 ├── tests/             # Basic test scaffolding
```

### Design Principles

1. Time-first modeling

Failures are temporal.
All signals are aligned into a single timeline.

2. State over prompts

LLMs operate over structured system state, not raw logs.

3. Correlation over summarization

The goal is to link:
	- change → behavior → failure

4. Explainability
Every output should include:
	-	reasoning
	-	supporting evidence
	- 	confidence
---

### Current Status


This is a POC focused on: 
- Single-service scenario
- Simulated incident data
- Basic reasoning pipeline

---

### Roadmap

- Drift detection engine (declared vs runtime state)
- PR generation for suggested fixes
- SLO-aware reasoning
- Blast radius simulation
- Multi-service correlation

---

### Why This Matters

- LLMs are currently used as copilots for generating code and configs.
- But DevOps problems are not just about writing YAML faster.
  
They are about:
- Understanding how intent, runtime behavior, and failures interact over time.
- DriftLoop explores how LLMs can help engineers reason across that system.

---

### Contributing

This is an early-stage exploration.
Ideas, feedback, and critiques are welcome.

---

### License

MIT
