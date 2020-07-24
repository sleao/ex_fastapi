from fastapi import APIRouter
from app.api.api_v1.endpoints import example

router = APIRouter()

router.include_router(example.router, prefix='/example', tags=['example'])