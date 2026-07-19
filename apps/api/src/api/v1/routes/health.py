"""Health and readiness endpoints."""

from fastapi import APIRouter, Depends
from redis.asyncio import Redis
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.v1.schemas.health import DependencyHealth, HealthResponse, ServiceStatus
from src.infrastructure.cache.redis_client import get_redis
from src.infrastructure.db.session import get_db

router = APIRouter(tags=["health"])
VERSION = "0.1.0"


@router.get("/health", response_model=HealthResponse, summary="Liveness probe")
async def health() -> HealthResponse:
    return HealthResponse(status=ServiceStatus.OK, version=VERSION)


@router.get("/ready", response_model=HealthResponse, summary="Readiness probe")
async def ready(
    db: AsyncSession = Depends(get_db),
    redis: Redis = Depends(get_redis),
) -> HealthResponse:
    deps: list[DependencyHealth] = []

    # PostgreSQL
    try:
        await db.execute(text("SELECT 1"))
        deps.append(DependencyHealth(name="postgres", status=ServiceStatus.OK))
    except Exception as exc:
        deps.append(DependencyHealth(name="postgres", status=ServiceStatus.DOWN, detail=str(exc)))

    # Redis
    try:
        await redis.ping()
        deps.append(DependencyHealth(name="redis", status=ServiceStatus.OK))
    except Exception as exc:
        deps.append(DependencyHealth(name="redis", status=ServiceStatus.DOWN, detail=str(exc)))

    overall = (
        ServiceStatus.OK
        if all(d.status == ServiceStatus.OK for d in deps)
        else ServiceStatus.DEGRADED
    )
    return HealthResponse(status=overall, version=VERSION, dependencies=deps)
