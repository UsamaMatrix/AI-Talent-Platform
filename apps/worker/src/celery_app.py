"""Celery application factory."""
import os

import structlog
from celery import Celery
from celery.signals import task_failure, task_postrun, task_prerun

logger = structlog.get_logger(__name__)

BROKER_URL = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/1")
RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/2")


def create_celery() -> Celery:
    app = Celery("talent_platform")
    app.conf.update(
        broker_url=BROKER_URL,
        result_backend=RESULT_BACKEND,
        task_serializer="json",
        result_serializer="json",
        accept_content=["json"],
        timezone="UTC",
        enable_utc=True,
        task_acks_late=True,
        task_reject_on_worker_lost=True,
        task_track_started=True,
        worker_prefetch_multiplier=1,
    )
    app.autodiscover_tasks(["src.tasks"])
    return app


celery_app = create_celery()


@task_prerun.connect
def on_task_prerun(task_id: str, task, *args, **kwargs) -> None:  # type: ignore[no-untyped-def]
    logger.info("task.started", task_id=task_id, task_name=task.name)


@task_postrun.connect
def on_task_postrun(task_id: str, task, *args, **kwargs) -> None:  # type: ignore[no-untyped-def]
    logger.info("task.completed", task_id=task_id, task_name=task.name)


@task_failure.connect
def on_task_failure(task_id: str, exception: Exception, *args, **kwargs) -> None:  # type: ignore[no-untyped-def]
    logger.error("task.failed", task_id=task_id, error=str(exception))
