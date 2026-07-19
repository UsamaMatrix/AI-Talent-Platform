"""Organization repository."""

import uuid
from datetime import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.models.auth import Organization
from src.domain.repositories.base import BaseRepository


class OrganizationRepository(BaseRepository[Organization]):
    """Async repository for Organization entities."""

    model = Organization

    async def get_by_slug(self, session: AsyncSession, slug: str) -> Organization | None:
        result = await session.execute(
            select(Organization).where(
                Organization.slug == slug,
                Organization.deleted_at.is_(None),
            )
        )
        return result.scalar_one_or_none()

    async def get_active_by_id(
        self, session: AsyncSession, entity_id: uuid.UUID
    ) -> Organization | None:
        result = await session.execute(
            select(Organization).where(
                Organization.id == entity_id,
                Organization.deleted_at.is_(None),
                Organization.is_active.is_(True),
            )
        )
        return result.scalar_one_or_none()

    async def soft_delete(self, session: AsyncSession, org: Organization) -> Organization:
        org.deleted_at = datetime.utcnow()
        org.is_active = False
        await session.flush()
        return org
