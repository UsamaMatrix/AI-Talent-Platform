"""Generic repository protocol."""

import uuid
from typing import Protocol

from sqlalchemy.ext.asyncio import AsyncSession


class Repository[T](Protocol):
    """Minimal async repository contract."""

    async def get_by_id(self, session: AsyncSession, entity_id: uuid.UUID) -> T | None: ...

    async def save(self, session: AsyncSession, entity: T) -> T: ...

    async def delete(self, session: AsyncSession, entity: T) -> None: ...


class BaseRepository[T]:
    """Concrete base with common SQLAlchemy helpers."""

    model: type[T]

    async def get_by_id(self, session: AsyncSession, entity_id: uuid.UUID) -> T | None:
        return await session.get(self.model, entity_id)

    async def save(self, session: AsyncSession, entity: T) -> T:
        session.add(entity)
        await session.flush()
        await session.refresh(entity)
        return entity

    async def delete(self, session: AsyncSession, entity: T) -> None:
        await session.delete(entity)
        await session.flush()
