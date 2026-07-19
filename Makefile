.PHONY: setup dev down logs migrate seed test test-api test-web lint format typecheck security

# ── Bootstrap ─────────────────────────────────────────────────────────────────
setup:
	@echo "==> Copying .env.example to .env (if not exists)"
	@if not exist .env copy .env.example .env
	@echo "==> Installing API dependencies"
	cd apps/api && uv pip install --system -e ".[dev]"
	@echo "==> Installing worker dependencies"
	cd apps/worker && uv pip install --system -e ".[dev]"
	@echo "==> Installing web dependencies"
	cd apps/web && npm install
	@echo "==> Installing pre-commit hooks"
	pre-commit install
	@echo "==> Setup complete"

# ── Docker ────────────────────────────────────────────────────────────────────
dev:
	docker compose up --build -d

down:
	docker compose down

logs:
	docker compose logs -f

# ── Database ──────────────────────────────────────────────────────────────────
migrate:
	cd apps/api && alembic upgrade head

seed:
	@echo "No seed data defined yet"

# ── Tests ─────────────────────────────────────────────────────────────────────
test: test-api test-web

test-api:
	cd apps/api && python -m pytest

test-web:
	cd apps/web && npm test

# ── Code quality ──────────────────────────────────────────────────────────────
lint:
	cd apps/api && ruff check src tests
	cd apps/worker && ruff check src tests
	cd apps/web && npm run lint

format:
	cd apps/api && ruff format src tests
	cd apps/worker && ruff format src tests

typecheck:
	cd apps/api && mypy src
	cd apps/worker && mypy src
	cd apps/web && npm run typecheck

# ── Security ──────────────────────────────────────────────────────────────────
security:
	pre-commit run gitleaks --all-files
