"""Consistent error envelope used across all API responses."""

from pydantic import BaseModel


class ErrorDetail(BaseModel):
    field: str | None = None
    message: str


class ErrorResponse(BaseModel):
    error: str
    details: list[ErrorDetail] | None = None
    correlation_id: str | None = None
