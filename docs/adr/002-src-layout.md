# ADR-002: Keep `src/` flat layout for API and worker packages

Date: 2024-07-19
Status: Accepted

## Context

Hatchling requires either a named package directory matching the project name
(`talent_platform_api/`) or an explicit `[tool.hatch.build.targets.wheel] packages`
declaration. The current codebase uses `from src.xxx import ...` throughout.

Migrating to `from talent_platform_api.xxx import ...` would require renaming every
import across all source files, tests, and the Alembic env before any product module
is implemented.

## Decision

Keep the flat `src/` layout with `packages = ["src"]` in hatchling config for now.
All internal imports use `from src.xxx import ...`.

This is acceptable because:
- The package is not published to PyPI
- Docker and CI install it as an editable local package
- Ruff `known-first-party = ["src"]` correctly classifies these imports

## Consequences

- Easier: no large rename refactor before Module 0
- Harder: if the package is ever published to PyPI, a rename will be required
- Revisit: rename to `talent_platform_api/` when implementing Module 0 auth,
  as that is the first major feature branch and a clean migration point

## Alternatives considered

- Rename now: rejected — high churn before any product code exists
- Use `find_packages()` with setuptools: rejected — project standard uses hatchling
