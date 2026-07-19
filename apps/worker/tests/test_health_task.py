"""Tests for worker tasks."""

from src.tasks.health import health_check


def test_health_check_returns_ok() -> None:
    result = health_check.apply()
    assert result.result["status"] == "ok"
