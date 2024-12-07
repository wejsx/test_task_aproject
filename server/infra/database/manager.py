from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession, AsyncEngine

from .models.base import Base


class DataBaseManager:
    def __init__(
        self,
        url: str,
        max_overflow: int = 10,
        pool_size: int = 10
    ) -> None:
        self.engine = create_async_engine(
            url=url,
            max_overflow=max_overflow,
            pool_size=pool_size
        )
        self.session: async_sessionmaker = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            expire_on_commit=False,
        )

    async def dispose(self):
       await self.engine.dispose()

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session() as session:
            yield session

    async def create_table(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
