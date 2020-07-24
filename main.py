from fastapi import FastAPI
from app.api.api_v1 import api

app = FastAPI()

app.include_router(api.router, prefix='/api/v1')