"""OpenAI provider adapter.

Requires: openai>=1.0.0
Install separately — not bundled in the gateway package to keep it provider-optional.
"""
from collections.abc import AsyncGenerator
from src.base import BaseLLMAdapter, LLMRequest, LLMResponse


class OpenAIAdapter(BaseLLMAdapter):
    def __init__(self, api_key: str, base_url: str | None = None) -> None:
        try:
            from openai import AsyncOpenAI  # type: ignore[import]
        except ImportError as e:
            raise ImportError("Install openai>=1.0.0 to use OpenAIAdapter") from e
        self._client = AsyncOpenAI(api_key=api_key, base_url=base_url)

    async def complete(self, request: LLMRequest) -> LLMResponse:
        response = await self._client.chat.completions.create(
            model=request.model,
            messages=[{"role": m.role, "content": m.content} for m in request.messages],
            temperature=request.temperature,
            max_tokens=request.max_tokens,
            stream=False,
        )
        choice = response.choices[0]
        return LLMResponse(
            content=choice.message.content or "",
            model=response.model,
            provider="openai",
            input_tokens=response.usage.prompt_tokens if response.usage else 0,
            output_tokens=response.usage.completion_tokens if response.usage else 0,
        )

    async def stream(self, request: LLMRequest) -> AsyncGenerator[str, None]:
        async with await self._client.chat.completions.create(
            model=request.model,
            messages=[{"role": m.role, "content": m.content} for m in request.messages],
            temperature=request.temperature,
            max_tokens=request.max_tokens,
            stream=True,
        ) as stream:
            async for chunk in stream:
                delta = chunk.choices[0].delta.content
                if delta:
                    yield delta
