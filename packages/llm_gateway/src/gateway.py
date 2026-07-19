"""LLM Gateway — provider registry and factory."""
from src.base import BaseLLMAdapter


_registry: dict[str, BaseLLMAdapter] = {}


def register_adapter(provider: str, adapter: BaseLLMAdapter) -> None:
    _registry[provider] = adapter


def get_adapter(provider: str) -> BaseLLMAdapter:
    if provider not in _registry:
        raise KeyError(f"LLM provider '{provider}' is not registered.")
    return _registry[provider]
