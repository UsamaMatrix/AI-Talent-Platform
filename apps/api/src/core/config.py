"""Application configuration loaded from environment variables."""

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # API — default to localhost; Docker Compose overrides with API_HOST=0.0.0.0
    api_host: str = "127.0.0.1"
    api_port: int = 8000
    api_debug: bool = False
    api_secret_key: str = Field(..., min_length=32)
    allowed_origins: list[str] = ["http://localhost:3000"]

    # Database
    database_url: str = Field(...)

    # Redis
    redis_url: str = "redis://localhost:6379/0"

    # Auth
    jwt_secret_key: str = Field(..., min_length=16)
    jwt_algorithm: str = "HS256"
    jwt_access_token_expire_minutes: int = 30

    # Logging
    log_level: str = "INFO"
    log_format: str = "json"

    # Observability
    otel_exporter_otlp_endpoint: str = ""
    otel_service_name: str = "talent-platform-api"


@lru_cache
def get_settings() -> Settings:
    return Settings()
