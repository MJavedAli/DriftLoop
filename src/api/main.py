from fastapi import FastAPI
from src.api.routes import router

app = FastAPI(title="DriftLoop")
app.include_router(router)
