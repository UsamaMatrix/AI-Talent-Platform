# Contributing

Thank you for your interest in contributing to the AI Talent Platform.

## Before you start

1. Check [open issues](https://github.com/UsamaMatrix/AI-Talent-Platform/issues) for existing work.
2. Open an issue before starting significant work.
3. Read [ARCHITECTURE.md](ARCHITECTURE.md) and [SECURITY.md](SECURITY.md).

## Development setup

```bash
git clone https://github.com/UsamaMatrix/AI-Talent-Platform.git
cd AI-Talent-Platform
cp .env.example .env
make setup
make dev
```

## Workflow

1. Create a branch: `feat/<issue-number>-<short-description>`
2. Make small, focused commits using [Conventional Commits](https://www.conventionalcommits.org/)
3. Run `make lint format typecheck test` before pushing
4. Open a pull request against `main`
5. Do not push directly to `main`

## Commit types

| Prefix | Use |
|---|---|
| `feat:` | New feature |
| `fix:` | Bug fix |
| `docs:` | Documentation only |
| `test:` | Tests only |
| `refactor:` | Code change without feature or fix |
| `chore:` | Build, tooling, dependencies |
| `ci:` | CI/CD changes |
| `security:` | Security fix |

## Code standards

- Python: Ruff, mypy strict, pytest
- TypeScript: ESLint, tsc strict, Vitest
- No business logic in route handlers
- No direct vendor SDK calls outside `packages/llm_gateway`
- All new features require tests

## Pull request checklist

- [ ] Tests pass (`make test`)
- [ ] Linting passes (`make lint`)
- [ ] Type checking passes (`make typecheck`)
- [ ] No secrets committed
- [ ] Documentation updated if needed
