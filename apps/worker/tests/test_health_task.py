"""Tests for worker tasks."""
from unittest.mock import MagicMock

from src.tasks.health import health_check


def test_health_check_returns_ok() -> None:
    task = health_check
    mock_request = MagicMock()
    mock_request.id = "test-task-id"
    task.request = mock_request  # type: ignore[attr-defined]
    result = health_check.run()
    assert result["status"] == "ok"
