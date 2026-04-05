from fastapi import APIRouter
from src.api.schemas import IncidentRequest
from src.reasoning.analyzer import analyze_incident

router = APIRouter()

@router.post("/analyze")
def analyze(req: IncidentRequest):
    return analyze_incident(req)
