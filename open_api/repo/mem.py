from sqlalchemy.ext.asyncio import AsyncSession


class MemRepo:

    def __init__(self, session: AsyncSession) -> None:
        self.session = session
