from typing import TYPE_CHECKING

from aiogram import Router, Bot
from aiogram.filters import CommandStart

from api.keyboards import home_keyboard
from utils.const.messages import HELLO_WORLD
from infra.exceptions.errors import AppExceptions

if TYPE_CHECKING:
    from aiogram.types import Message
    from domain.services import UserService


start_route = Router()


@start_route.message(CommandStart())
async def start(message: "Message", bot: Bot, user_service: "UserService"):
    try:
        await user_service.register(message.from_user.id)
    except AppExceptions as e:
        await message.answer(
            text=e.message,
        )
    else:
        await bot.send_message(
            message.from_user.id,
            text=HELLO_WORLD.format(username=message.from_user.username),
            reply_markup=home_keyboard()
        )