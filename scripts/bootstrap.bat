@echo off
echo === AI Talent Platform Bootstrap ===

where python >nul 2>&1 || (echo ERROR: Python 3.12+ required && exit /b 1)
where node >nul 2>&1 || (echo ERROR: Node.js 22+ required && exit /b 1)
where git >nul 2>&1 || (echo ERROR: Git required && exit /b 1)

if not exist .env (
    copy .env.example .env
    echo Created .env from .env.example — fill in required secrets before running make dev
)

where uv >nul 2>&1 || (
    echo Installing uv...
    pip install uv
)

echo Installing API dependencies...
cd apps\api && uv pip install --system -e ".[dev]" && cd ..\..

echo Installing worker dependencies...
cd apps\worker && uv pip install --system -e ".[dev]" && cd ..\..

echo Installing web dependencies...
cd apps\web && npm install && cd ..\..

where pre-commit >nul 2>&1 && (
    echo Installing pre-commit hooks...
    pre-commit install
)

echo.
echo Bootstrap complete. Next steps:
echo   1. Edit .env with your secrets
echo   2. Run: make dev
echo   3. Run: make migrate
