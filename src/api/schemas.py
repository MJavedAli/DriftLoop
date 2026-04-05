from pydantic import BaseModel

class IncidentRequest(BaseModel):
    service: str
    start_time: str
    end_time: str
