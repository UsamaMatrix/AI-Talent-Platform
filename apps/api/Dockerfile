FROM python:3.12-slim

WORKDIR /app

RUN pip install uv

COPY pyproject.toml .
RUN uv pip install --system --no-cache .

COPY src/ ./src/
COPY alembic/ ./alembic/
COPY alembic.ini .

RUN useradd -m -u 1001 appuser && chown -R appuser /app
USER appuser

EXPOSE 8000
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
