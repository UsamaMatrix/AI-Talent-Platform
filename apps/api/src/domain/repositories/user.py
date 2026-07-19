"""User repository."""

import uuid
from datetime import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.models.auth import User
from src.domain.repositories.base import BaseRepository


class UserRepository(BaseRepository[User]):
    """Async repository for User entities."""

    model = User

    async def get_by_email(self, session: AsyncSession, normalized_email: str) -> User | None:
        result = await session.execute(
            select(User).where(
                User.normalized_email == normalized_email,
                User.deleted_at.is_(None),
            )
        )
        return result.scalar_one_or_none()

    async def get_active_by_id(self, session: AsyncSession, entity_id: uuid.UUID) -> User | None:
        result = await session.execute(
            select(User).where(
                User.id == entity_id,
                User.deleted_at.is_(None),
                User.is_active.is_(True),
            )
        )
        return result.scalar_one_or_none()

    async def soft_delete(self, session: AsyncSession, user: User) -> User:
        user.deleted_at = datetime.utcnow()
        user.is_active = False
        await session.flush()
        return user
