from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message

from infra.di.container import MainContainer


class UserServiceMiddleware(BaseMiddleware):
    def __init__(self, container: MainContainer) -> None:
        self.container = container

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        data['user_service'] = self.container.user_service()
        data['store_service'] = self.container.store_service()
        return await handler(event, data)