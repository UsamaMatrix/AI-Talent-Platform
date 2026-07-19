"""Authentication service interfaces (protocols only — no implementation)."""

import uuid
from typing import Protocol

from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.models.auth import AuditLog, Membership, Organization, RefreshToken, User


class IUserService(Protocol):
    """User lifecycle operations — implementation deferred to Module 0B."""

    async def create_user(
        self,
        session: AsyncSession,
        email: str,
        full_name: str,
        organization_id: uuid.UUID,
    ) -> User: ...

    async def deactivate_user(self, session: AsyncSession, user_id: uuid.UUID) -> User: ...

    async def get_user(self, session: AsyncSession, user_id: uuid.UUID) -> User | None: ...


class IOrganizationService(Protocol):
    """Organization lifecycle operations."""

    async def create_organization(
        self, session: AsyncSession, name: str, slug: str
    ) -> Organization: ...

    async def deactivate_organization(
        self, session: AsyncSession, org_id: uuid.UUID
    ) -> Organization: ...


class IMembershipService(Protocol):
    """Membership and role assignment operations."""

    async def add_member(
        self,
        session: AsyncSession,
        user_id: uuid.UUID,
        organization_id: uuid.UUID,
        role_id: uuid.UUID,
    ) -> Membership: ...

    async def remove_member(self, session: AsyncSession, membership_id: uuid.UUID) -> None: ...


class IRefreshTokenService(Protocol):
    """Refresh token lifecycle — implementation deferred to Module 0B."""

    async def revoke_token(self, session: AsyncSession, token_hash: str) -> RefreshToken | None: ...

    async def revoke_all_for_user(self, session: AsyncSession, user_id: uuid.UUID) -> int: ...


class IAuditService(Protocol):
    """Audit log write operations — append-only, no secrets in metadata."""

    async def log(
        self,
        session: AsyncSession,
        action: str,
        target_type: str,
        actor_id: uuid.UUID | None = None,
        organization_id: uuid.UUID | None = None,
        target_id: str | None = None,
        correlation_id: str | None = None,
        metadata: dict[str, object] | None = None,
        ip_address: str | None = None,
    ) -> AuditLog: ...
