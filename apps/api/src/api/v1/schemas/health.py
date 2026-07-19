"""Health and readiness response schemas."""
from enum import StrEnum

from pydantic import BaseModel


class ServiceStatus(StrEnum):
    OK = "ok"
    DEGRADED = "degraded"
    DOWN = "down"


class DependencyHealth(BaseModel):
    name: str
    status: ServiceStatus
    detail: str | None = None


class HealthResponse(BaseModel):
    status: ServiceStatus
    version: str
    dependencies: list[DependencyHealth] | None = None
