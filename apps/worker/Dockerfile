FROM python:3.12-slim

WORKDIR /app

RUN pip install uv

COPY pyproject.toml .
RUN uv pip install --system --no-cache .

COPY src/ ./src/

RUN useradd -m -u 1001 appuser && chown -R appuser /app
USER appuser

CMD ["celery", "-A", "src.celery_app:celery_app", "worker", "--loglevel=info"]
