@echo off
set GH="C:\Program Files\GitHub CLI\gh.exe"

echo === Creating labels ===
%GH% label create "module:foundation"    --color "0075ca" --description "Foundation module" --force
%GH% label create "module:resume"        --color "e4e669" --description "Resume Intelligence module" --force
%GH% label create "module:recruiter"     --color "d93f0b" --description "AI Recruiter module" --force
%GH% label create "module:coding"        --color "0e8a16" --description "Coding Interview module" --force
%GH% label create "module:voice"         --color "1d76db" --description "Voice Interview module" --force
%GH% label create "module:evaluation"    --color "5319e7" --description "AI Evaluation module" --force
%GH% label create "module:prompt-eval"   --color "b60205" --description "Prompt Evaluation module" --force
%GH% label create "module:playground"    --color "f9d0c4" --description "Agent Playground module" --force
%GH% label create "module:dashboard"     --color "c2e0c6" --description "Interview Dashboard module" --force
%GH% label create "module:job-matcher"   --color "fef2c0" --description "AI Job Matcher module" --force
%GH% label create "security"             --color "ee0701" --description "Security issue or fix" --force
%GH% label create "documentation"        --color "0075ca" --description "Documentation" --force
%GH% label create "testing"              --color "bfd4f2" --description "Tests" --force
%GH% label create "infrastructure"       --color "e4e669" --description "Infrastructure and DevOps" --force
%GH% label create "good first issue"     --color "7057ff" --description "Good for newcomers" --force

echo === Creating milestone issues ===
%GH% issue create --title "Milestone: Resume Intelligence" --body "Implement resume upload, parsing, structured extraction and LLM-powered analysis. See ARCHITECTURE.md for data flow." --label "module:resume" --label "documentation"
%GH% issue create --title "Milestone: AI Recruiter" --body "Implement AI-assisted candidate screening, job description matching and recruiter workflow." --label "module:recruiter"
%GH% issue create --title "Milestone: Coding Interview" --body "Implement coding challenge delivery, secure sandbox execution and automated evaluation." --label "module:coding" --label "security"
%GH% issue create --title "Milestone: Voice Interview" --body "Implement voice interview recording, transcription and LLM-based evaluation." --label "module:voice"
%GH% issue create --title "Milestone: AI Evaluation" --body "Implement DeepEval and Promptfoo evaluation harness for all LLM-powered modules." --label "module:evaluation" --label "testing"
%GH% issue create --title "Milestone: Prompt Evaluation" --body "Implement prompt versioning, A/B testing and rubric-based LLM judge evaluation." --label "module:prompt-eval"
%GH% issue create --title "Milestone: Agent Playground" --body "Implement LangGraph agent playground for testing and debugging agent graphs." --label "module:playground"
%GH% issue create --title "Milestone: Interview Dashboard" --body "Implement interview management dashboard with candidate tracking and analytics." --label "module:dashboard"
%GH% issue create --title "Milestone: AI Resume Optimizer" --body "Implement AI-powered resume optimization and feedback for candidates." --label "module:resume"
%GH% issue create --title "Milestone: AI Job Matcher" --body "Implement semantic job-to-candidate matching using pgvector embeddings." --label "module:job-matcher"

echo === Creating PR ===
%GH% pr create --title "chore: bootstrap AI Talent Platform monorepo" --body "## Summary\n\nBootstraps the full monorepo foundation.\n\nCloses #1\n\n## Changes\n\n- Full directory structure\n- FastAPI backend with health endpoints, settings, logging, middleware, Alembic\n- Celery worker with health task\n- Next.js frontend with dashboard shell, landing page, sign-in placeholder\n- Provider-neutral LLM gateway (OpenAI + Anthropic adapters)\n- docker-compose.yml with PostgreSQL, Redis, MinIO, Prometheus, Grafana\n- Makefile with all dev targets\n- GitHub Actions: backend CI, frontend CI, Docker build, CodeQL, dependency review, secret scanning\n- README, ARCHITECTURE, SECURITY, CONTRIBUTING, CODE_OF_CONDUCT, LICENSE\n- Issue templates, PR template, Dependabot config\n- ADR template + ADR-001\n\n## Checklist\n\n- [x] No secrets committed\n- [x] No business logic in route handlers\n- [x] No vendor SDK calls outside llm_gateway\n- [x] Tests included for API and worker" --base master --head feat/1-bootstrap-monorepo

echo === Done ===
