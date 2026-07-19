.PHONY: setup dev down logs migrate seed test test-api test-web \
        lint format typecheck security ci

# ── Bootstrap ─────────────────────────────────────────────────────────────────
setup:
	@echo "==> Installing API dependencies"
	cd apps/api && uv pip install --system -e ".[dev]"
	@echo "==> Installing worker dependencies"
	cd apps/worker && uv pip install --system -e ".[dev]"
	@echo "==> Installing web dependencies"
	cd apps/web && npm install
	@echo "==> Setup complete. Copy .env.example to .env and fill in secrets."

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
	cd apps/api && pytest -v
	cd apps/worker && pytest -v

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
	cd apps/web && npm run typecheck

# ── Security ──────────────────────────────────────────────────────────────────
security:
	pre-commit run gitleaks --all-files

# ── Local CI (mirrors GitHub Actions) ────────────────────────────────────────
ci:
	@echo "==> [1/9] API format check"
	cd apps/api && ruff format --check src tests
	@echo "==> [2/9] API lint"
	cd apps/api && ruff check src tests
	@echo "==> [3/9] API type check"
	cd apps/api && mypy src
	@echo "==> [4/9] API tests"
	cd apps/api && pytest -v
	@echo "==> [5/9] Worker format check"
	cd apps/worker && ruff format --check src tests
	@echo "==> [6/9] Worker lint"
	cd apps/worker && ruff check src tests
	@echo "==> [7/9] Frontend lint"
	cd apps/web && npm run lint
	@echo "==> [8/9] Frontend type check"
	cd apps/web && npm run typecheck
	@echo "==> [9/9] Frontend unit tests + build"
	cd apps/web && npm test && npm run build
	@echo "==> CI complete"
