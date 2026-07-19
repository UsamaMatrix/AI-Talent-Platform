"""Pytest configuration and shared fixtures."""

import os

import pytest


def pytest_configure(config: pytest.Config) -> None:
    """Set required env vars before any module is imported during collection."""
    os.environ.setdefault("DATABASE_URL", "postgresql+asyncpg://user:pass@localhost/test")
    os.environ.setdefault("API_SECRET_KEY", "test_secret_key_minimum_32_chars_xx")
    os.environ.setdefault("JWT_SECRET_KEY", "test_jwt_secret_key_minimum_16xx")
    os.environ.setdefault("REDIS_URL", "redis://localhost:6379/0")
