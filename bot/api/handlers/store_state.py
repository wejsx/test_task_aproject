from typing import TYPE_CHECKING

from aiogram import Router

from infra.exceptions.errors import AppExceptions

from api.keyboards import home_keyboard
from api.states import (
    AddProductStoreState
)

if TYPE_CHECKING:
    from aiogram import Bot
    from aiogram.fsm.context import FSMContext
    from aiogram.types import Message
    from domain.services import UserService, StoreService

store_state_route = Router()


@store_state_route.message(AddProductStoreState.body)
async def add_product(message: "Message", bot: "Bot", state: "FSMContext", user_service: "UserService", store_service: "StoreService"):
    try:
        name, price = message.text.split(',')
        data = await store_service.add_product(name, price)
    except AppExceptions as e:
        await bot.send_message(
            message.from_user.id,
            text=e.message,
        )
    else:
        await bot.send_message(
            message.from_user.id,
            text=data.detail,
            reply_markup=home_keyboard()
        )