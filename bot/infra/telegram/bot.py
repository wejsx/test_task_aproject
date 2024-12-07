from aiogram import Bot, Dispatcher

from core.settings import settings
from api.handlers import start_route, store_route, store_state_route, user_route
from infra.telegram.middlewares import UserServiceMiddleware
from infra.di.container import MainContainer

bot = Bot(token=settings.bot.token)
dp = Dispatcher()
container = MainContainer()
dp.update.middleware(UserServiceMiddleware(container))
dp.include_routers(*[
        start_route, store_route, 
        store_state_route, user_route
    ]
)