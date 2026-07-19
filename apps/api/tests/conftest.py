"""Pytest configuration and shared fixtures."""
import pytest
from unittest.mock import patch

# Patch settings before any import resolves them
@pytest.fixture(autouse=True)
def patch_settings():
    with patch.dict(
        "os.environ",
        {
            "DATABASE_URL": "postgresql+asyncpg://user:pass@localhost/test",
            "API_SECRET_KEY": "test_secret_key_minimum_32_chars_xx",
            "JWT_SECRET_KEY": "test_jwt_secret_key_minimum_16",
            "REDIS_URL": "redis://localhost:6379/0",
        },
    ):
        yield
