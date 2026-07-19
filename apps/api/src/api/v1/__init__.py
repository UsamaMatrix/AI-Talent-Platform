"""API v1 router."""
from fastapi import APIRouter
from src.api.v1.routes.health import router as health_router

api_v1_router = APIRouter(prefix="/api/v1")
api_v1_router.include_router(health_router)
