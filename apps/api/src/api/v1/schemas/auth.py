"""Pydantic schemas for the authentication domain."""

import uuid
from datetime import datetime

from pydantic import BaseModel, EmailStr, Field


class OrganizationRead(BaseModel):
    id: uuid.UUID
    name: str
    slug: str
    is_active: bool
    created_at: datetime

    model_config = {"from_attributes": True}


class OrganizationCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    slug: str = Field(..., min_length=1, max_length=100, pattern=r"^[a-z0-9-]+$")


class UserRead(BaseModel):
    id: uuid.UUID
    email: EmailStr
    full_name: str
    is_active: bool
    email_verified: bool
    created_at: datetime

    model_config = {"from_attributes": True}


class UserCreate(BaseModel):
    email: EmailStr
    full_name: str = Field(..., min_length=1, max_length=255)
    organization_id: uuid.UUID


class PermissionRead(BaseModel):
    id: uuid.UUID
    code: str
    description: str

    model_config = {"from_attributes": True}


class RoleRead(BaseModel):
    id: uuid.UUID
    organization_id: uuid.UUID
    name: str
    description: str | None
    is_system: bool

    model_config = {"from_attributes": True}


class RoleCreate(BaseModel):
    organization_id: uuid.UUID
    name: str = Field(..., min_length=1, max_length=100)
    description: str | None = Field(None, max_length=500)


class MembershipRead(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    organization_id: uuid.UUID
    role_id: uuid.UUID
    is_active: bool
    joined_at: datetime

    model_config = {"from_attributes": True}


class AuditLogRead(BaseModel):
    id: uuid.UUID
    organization_id: uuid.UUID | None
    actor_id: uuid.UUID | None
    action: str
    target_type: str
    target_id: str | None
    correlation_id: str | None
    ip_address: str | None
    created_at: datetime
    # metadata excluded from read schema — never expose raw audit metadata to clients

    model_config = {"from_attributes": True}
