"""Anthropic provider adapter.

Requires: anthropic>=0.25.0
"""
from collections.abc import AsyncGenerator
from src.base import BaseLLMAdapter, LLMRequest, LLMResponse


class AnthropicAdapter(BaseLLMAdapter):
    def __init__(self, api_key: str) -> None:
        try:
            from anthropic import AsyncAnthropic  # type: ignore[import]
        except ImportError as e:
            raise ImportError("Install anthropic>=0.25.0 to use AnthropicAdapter") from e
        self._client = AsyncAnthropic(api_key=api_key)

    async def complete(self, request: LLMRequest) -> LLMResponse:
        system = next((m.content for m in request.messages if m.role == "system"), None)
        messages = [
            {"role": m.role, "content": m.content}
            for m in request.messages
            if m.role != "system"
        ]
        kwargs = dict(
            model=request.model,
            max_tokens=request.max_tokens,
            messages=messages,
        )
        if system:
            kwargs["system"] = system
        response = await self._client.messages.create(**kwargs)
        return LLMResponse(
            content=response.content[0].text,
            model=response.model,
            provider="anthropic",
            input_tokens=response.usage.input_tokens,
            output_tokens=response.usage.output_tokens,
        )

    async def stream(self, request: LLMRequest) -> AsyncGenerator[str, None]:
        system = next((m.content for m in request.messages if m.role == "system"), None)
        messages = [
            {"role": m.role, "content": m.content}
            for m in request.messages
            if m.role != "system"
        ]
        kwargs = dict(model=request.model, max_tokens=request.max_tokens, messages=messages)
        if system:
            kwargs["system"] = system
        async with self._client.messages.stream(**kwargs) as stream:
            async for text in stream.text_stream:
                yield text
