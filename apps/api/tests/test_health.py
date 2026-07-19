"""Tests for health and readiness endpoints."""

from unittest.mock import AsyncMock, patch

import pytest
from httpx import ASGITransport, AsyncClient

from src.main import app


@pytest.fixture
async def client():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as c:
        yield c


async def test_health_returns_ok(client: AsyncClient) -> None:
    response = await client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["version"] == "0.1.0"


async def test_ready_returns_ok_when_deps_healthy(client: AsyncClient) -> None:
    mock_db = AsyncMock()
    mock_db.execute = AsyncMock()
    mock_redis = AsyncMock()
    mock_redis.ping = AsyncMock(return_value=True)

    with (
        patch("src.api.v1.routes.health.get_db", return_value=mock_db),
        patch("src.api.v1.routes.health.get_redis", return_value=mock_redis),
    ):
        response = await client.get("/api/v1/ready")
    assert response.status_code == 200
