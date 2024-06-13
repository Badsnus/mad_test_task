from typing import Sequence

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from models import Mem


class MemRepo:

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def all(self, limit: int, offset: int) -> Sequence[Mem]:
        return (await self.session.scalars(
            select(Mem).offset(offset).limit(limit),
        )).all()

    async def get(self, uuid: str) -> Mem | None:
        return await self.session.scalar(select(Mem).filter(Mem.uuid == uuid))

    async def create(self, text: str, file_extension: str) -> Mem:
        mem = Mem(text=text, file_extension=file_extension)

        self.session.add(mem)
        await self.session.commit()
        return mem

    async def update(self, mem: Mem, **kwargs) -> Mem:
        for key, value in kwargs.items():
            setattr(mem, key, value)

        self.session.add(mem)
        await self.session.commit()
        return mem

    async def delete(self, mem: Mem) -> None:
        await self.session.delete(mem)
        await self.session.commit()
