# Architecture

## Principles

- Clean architecture: domain logic is isolated from infrastructure and transport layers
- Repository pattern: all database access goes through typed repository classes
- Service layer: business logic lives in service classes, never in route handlers
- Dependency injection: FastAPI `Depends()` wires infrastructure into services
- Provider-neutral LLM gateway: no module calls vendor SDKs directly

## Layer boundaries

```
Route handler → Schema (Pydantic) → Service → Repository → SQLAlchemy model
                                  ↘ LLM Gateway → Provider adapter
                                  ↘ Cache (Redis)
                                  ↘ Storage (MinIO / S3)
```

## Key packages

| Package | Responsibility |
|---|---|
| `apps/api/src/api/` | FastAPI routes and Pydantic schemas only |
| `apps/api/src/domain/` | Models, services, repository interfaces |
| `apps/api/src/infrastructure/` | DB sessions, Redis, storage adapters |
| `apps/api/src/core/` | Config, logging, middleware, error types |
| `packages/llm_gateway/` | Provider-neutral LLM interface + adapters |
| `packages/agents/` | LangGraph agent graphs |
| `packages/evaluation/` | DeepEval / Promptfoo harness |
| `sandbox/runner/` | Isolated code execution abstraction |

## Data flow — resume upload (planned)

```
POST /api/v1/resumes
  → validate file type, MIME, size
  → scan for malware (integration boundary)
  → store in MinIO
  → enqueue Celery task
  → return 202 Accepted

Celery task
  → extract text
  → call LLM gateway (resume intelligence)
  → store structured result in PostgreSQL
  → emit evaluation metrics
```

## ADRs

Architecture Decision Records are in `docs/adr/`.
