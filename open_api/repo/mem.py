from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import Mem


class MemRepo:

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get(self, uuid: str) -> Mem | None:
        return await self.session.scalar(select(Mem).filter(Mem.uuid == uuid))

    def create(self, ) -> Mem:
        ...