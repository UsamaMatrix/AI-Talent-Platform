"""Health check task — verifies worker is alive."""
from celery import shared_task
import structlog

logger = structlog.get_logger(__name__)


@shared_task(
    name="tasks.health_check",
    bind=True,
    max_retries=3,
    default_retry_delay=5,
    autoretry_for=(Exception,),
    retry_backoff=True,
)
def health_check(self) -> dict[str, str]:  # type: ignore[no-untyped-def]
    logger.info("health_check.running", task_id=self.request.id)
    return {"status": "ok", "task_id": self.request.id or ""}
