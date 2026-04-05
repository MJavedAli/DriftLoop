from src.state.db import SessionLocal
from src.normalize.timeline import build_timeline
from src.reasoning.retriever import retrieve_context
from src.reasoning.prompts import build_prompt

# mock LLM
def fake_llm(prompt):
    return "Likely caused by recent config change affecting CPU scaling"


def analyze_incident(req):
    session = SessionLocal()
    changes, metrics = retrieve_context(session, req.service)
    timeline = build_timeline(changes, metrics)
    prompt = build_prompt(timeline)

    result = fake_llm(prompt)

    return {
        "summary": result,
        "events": timeline[:5]
    }
