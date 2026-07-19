# ADR-001: Provider-neutral LLM gateway

Date: 2024-01-01
Status: Accepted

## Context

The platform needs to call multiple LLM providers (OpenAI, Anthropic, Google Gemini, local endpoints). Calling vendor SDKs directly from feature modules creates tight coupling and makes provider switching expensive.

## Decision

All LLM calls must go through `packages/llm_gateway`. Feature modules depend only on `BaseLLMAdapter`. Provider adapters are registered at startup. No vendor SDK may be imported outside the adapter files.

## Consequences

- Easier: swap providers, add new providers, mock in tests, enforce zero-retention config per provider
- Harder: slightly more boilerplate per new provider

## Alternatives considered

- LangChain: rejected — too much abstraction overhead and version instability
- Direct SDK calls: rejected — creates vendor lock-in across all modules
