"""Provider-neutral LLM gateway — base interface.

All vendor SDK calls must go through an adapter that implements BaseLLMAdapter.
No module outside this package may import vendor SDKs directly.
"""
from abc import ABC, abstractmethod
from collections.abc import AsyncGenerator
from dataclasses import dataclass


@dataclass
class LLMMessage:
    role: str  # "system" | "user" | "assistant"
    content: str


@dataclass
class LLMRequest:
    messages: list[LLMMessage]
    model: str
    temperature: float = 0.7
    max_tokens: int = 2048
    stream: bool = False


@dataclass
class LLMResponse:
    content: str
    model: str
    provider: str
    input_tokens: int = 0
    output_tokens: int = 0


class BaseLLMAdapter(ABC):
    """All provider adapters must implement this interface."""

    @abstractmethod
    async def complete(self, request: LLMRequest) -> LLMResponse: ...

    @abstractmethod
    async def stream(self, request: LLMRequest) -> AsyncGenerator[str, None]: ...
