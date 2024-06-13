from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from models import Mem


class MemRepo:

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get(self, uuid: str) -> Mem | None:
        return await self.session.scalar(select(Mem).filter(Mem.uuid == uuid))

    async def create(self, text: str) -> Mem:
        mem = Mem(text=text)

        self.session.add(mem)
        await self.session.commit()
        return mem

    async def update(self, uuid: str, **kwargs) -> Mem | None:
        stmt = (
            update(Mem)
            .where(Mem.uuid == uuid)
            .values(**kwargs)
            .returning(Mem)
        )

        mem = (await self.session.execute(stmt)).fetchone()
        await self.session.commit()
        return mem

    async def delete(self, uuid: str) -> None:
        await self.session.execute(delete(Mem).where(Mem.uuid == uuid))
        await self.session.commit()
