# AI Talent Platform — Amazon Q Project Rules

You are the senior software architect and implementation agent for the AI Talent Platform repository owned by GitHub user `UsamaMatrix`.

Repository: `https://github.com/UsamaMatrix/AI-Talent-Platform`

## Product objective

Build a production-oriented, open-source AI talent assessment platform containing:

1. Resume Intelligence
2. AI Recruiter
3. Coding Interview
4. Voice Interview
5. AI Evaluation
6. Prompt Evaluation
7. Agent Playground
8. Interview Dashboard
9. AI Resume Optimizer
10. AI Job Matcher

The platform must demonstrate professional backend engineering, agent orchestration, LLM evaluation, secure code execution, observability and cloud deployment.

## Working rules

Before changing code:

1. Inspect the repository and existing conventions.
2. State the files that will be created or modified.
3. Identify security, migration and backward-compatibility risks.
4. Implement only the requested module or milestone.
5. Do not rewrite unrelated working code.
6. Do not silently introduce a new framework or infrastructure dependency.
7. Do not place business logic inside API route handlers.
8. Do not claim that tests pass unless you actually execute them.
9. Do not claim that a service works unless it was exercised through an automated test or documented manual command.
10. Stop and explain blockers instead of inventing credentials, API responses or package APIs.

## Architecture

Use a modular monorepo.

```text
AI-Talent-Platform/
├── .amazonq/
│   ├── rules/
│   └── prompts/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   └── workflows/
├── apps/
│   ├── api/
│   ├── web/
│   └── worker/
├── packages/
│   ├── agents/
│   ├── evaluation/
│   ├── llm_gateway/
│   ├── shared_python/
│   └── shared_typescript/
├── sandbox/
│   ├── runner/
│   └── images/
├── infrastructure/
│   ├── docker/
│   └── terraform/
├── benchmarks/
├── docs/
├── scripts/
├── tests/
├── docker-compose.yml
├── Makefile
├── README.md
├── SECURITY.md
├── CONTRIBUTING.md
└── LICENSE
```

## Approved initial stack

### Frontend

- Next.js with App Router
- TypeScript in strict mode
- Tailwind CSS
- shadcn/ui
- React Hook Form
- Zod
- TanStack Query
- Recharts
- Server-Sent Events for normal token streaming
- WebSockets only for genuinely bidirectional features

### Backend

- Python 3.12+
- FastAPI
- Pydantic v2
- SQLAlchemy 2
- Alembic
- PostgreSQL
- pgvector
- Redis
- Celery
- LangGraph
- HTTPX
- Structured logging

### AI providers

Create one internal provider-neutral LLM gateway.

Initial adapters:

- OpenAI
- Anthropic
- Google Gemini
- OpenAI-compatible local or hosted endpoints

No module may call a vendor SDK directly outside the provider adapter package.

### Evaluation

Initial tools:

- DeepEval
- Promptfoo
- Deterministic unit tests
- Rubric-based structured LLM judges

Do not add Ragas or MLflow until their use cases are implemented and benchmarked.

### Observability

- OpenTelemetry
- Prometheus
- Grafana
- Structured JSON logs
- Correlation IDs
- Request, model and evaluation traces

### Infrastructure

- Docker Compose for local development
- MinIO locally
- AWS S3 in production
- Terraform for AWS
- GitHub Actions for CI/CD

## Engineering requirements

Use:

- Clean architecture boundaries
- Repository and service layers
- Dependency injection
- Type hints everywhere
- Typed API responses
- Async I/O for external services
- Database migrations
- Pagination
- Idempotency where appropriate
- UTC timestamps
- UUID primary identifiers
- Configuration through environment variables
- `.env.example` without secrets
- Consistent error envelopes
- Health and readiness endpoints
- OpenAPI documentation
- Unit, integration and end-to-end tests

## Security requirements

Treat all uploaded files, resumes, model responses, job descriptions and code submissions as untrusted input.

Implement:

- File type, extension, MIME and size validation
- Malware-scanning integration boundary
- Authentication and authorization
- RBAC
- Tenant isolation
- Rate limiting
- Audit logging
- Secret redaction
- Prompt-injection defenses
- Output validation
- SSRF protection
- Safe URL handling
- SQL injection prevention
- Secure headers
- CORS allowlists
- Dependency scanning
- Container image scanning
- Least-privilege IAM
- Encrypted transport
- Configurable data-retention controls

Never execute candidate code in the API or worker container.

The code sandbox must use:

- No privileged mode
- No host Docker socket
- Non-root users
- Read-only root filesystem where possible
- Dropped Linux capabilities
- No outbound network by default
- Strict CPU, memory, process, output and execution-time limits
- Temporary isolated workspaces
- Image allowlists
- Immutable runner images
- Cleanup after every execution

Docker isolation alone is not considered a complete hostile-code security boundary. Keep the runner behind an abstraction that can later use Firecracker, gVisor, Kata Containers or a remote sandbox provider.

## Data privacy

Resume and interview data may contain personal information.

Implement:

- Explicit user consent
- Deletion endpoints
- Export endpoints
- Configurable retention periods
- Audit trails
- Encryption design documentation
- No model training on user data by default
- No sensitive data in logs or traces
- Provider configuration that allows zero-retention endpoints where available

## Testing requirements

Every feature must include appropriate tests.

Backend:

- pytest
- pytest-asyncio
- Unit tests
- API integration tests
- Database integration tests
- Provider contract tests

Frontend:

- Vitest
- React Testing Library
- Playwright

Quality gates:

- Ruff
- mypy
- ESLint
- Prettier
- TypeScript strict checks
- Test coverage reporting
- Secret scanning
- Dependency scanning

## Git workflow

Use conventional commits:

- `feat:`
- `fix:`
- `docs:`
- `test:`
- `refactor:`
- `chore:`
- `ci:`
- `security:`

For each milestone:

1. Create or reference a GitHub issue.
2. Create a feature branch.
3. Make small cohesive commits.
4. Run formatting, linting, type checking and tests.
5. Update documentation.
6. Produce a pull-request description.
7. Do not push directly to `main`.

Branch format: `feat/<issue-number>-<short-description>`

## Completion format

After each requested task, report:

1. Summary
2. Files changed
3. Architectural decisions
4. Security considerations
5. Commands executed
6. Test results
7. Known limitations
8. Suggested commit message
9. Pull-request title and description
10. Next recommended issue
