from typing import AsyncGenerator

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from models.base import AsyncSessionLocal
from repo.mem import MemRepo


class DB:
    def __init__(self, session: AsyncSession) -> None:
        self.mem = MemRepo(session)


async def get_session() -> AsyncGenerator:
    async with AsyncSessionLocal() as session:
        yield session


async def get_db(session: AsyncSession = Depends(get_session)) -> AsyncGenerator:
    yield DB(session)
