def build_prompt(events, drift_findings=None):
    return f"""
You are a senior DevOps incident reasoning system.

Task:
Analyze the timeline and explain:
1. What changed
2. What runtime symptoms appeared
3. What the most likely root cause is
4. What evidence supports that cause
5. What the safest fix should be

Rules:
- Prefer causal reasoning over summary
- Distinguish between declared state and observed behavior
- Mention drift if infra config does not match runtime symptoms
- Be concise, technical, and specific
- Do not guess beyond the evidence

Timeline:
{events}

Drift findings:
{drift_findings or []}

Return:
- incident_summary
- root_cause_hypothesis
- evidence
- recommended_fix
- confidence
"""
