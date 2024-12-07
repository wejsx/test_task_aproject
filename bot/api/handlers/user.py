from typing import TYPE_CHECKING

from aiogram import Router, Bot, F
from aiogram.fsm.context import FSMContext

from api.keyboards import home_keyboard, store_keyboard, product_keyboard
from infra.exceptions.errors import AppExceptions
from api.states import AddProductStoreState

from utils.const.messages import (
    SUCCESS_BUY_PRODUCT,
    SUCCESS_ADD_PRODUCT_CART,
    HELLO_WORLD,
    PROFILE,
)

if TYPE_CHECKING:
    from aiogram.types import CallbackQuery
    from domain.services import UserService, StoreService


user_route = Router()


@user_route.callback_query(F.data.startswith('buy_product_'))
async def buy_product(callback: "CallbackQuery", bot: Bot, user_service: "UserService", store_service: "StoreService"):
    product_id = callback.data.split('_')[-1]
    try:
        await user_service.buy_product(
            callback.from_user.id,
            product_id
        )
    except AppExceptions as e:
        await callback.answer(
            text=e.message,
            show_alert=True
        )
    else:
        await callback.message.edit_text(
            text=SUCCESS_BUY_PRODUCT,
            reply_markup=home_keyboard()
        )


@user_route.callback_query(F.data.startswith('add_cart_'))
async def add_product_cart(callback: "CallbackQuery", user_service: "UserService"):
    product_id = callback.data.split('_')[-1]
    try:
        await user_service.add_product_cart(
            callback.from_user.id,
            product_id
        )
    except AppExceptions as e:
        await callback.answer(
            text=e.message,
            show_alert=True
        )
    else:
        await callback.message.edit_text(
            text=SUCCESS_ADD_PRODUCT_CART,
            reply_markup=home_keyboard()
        )


@user_route.callback_query(F.data == 'profile')
async def get_profile(callback: "CallbackQuery", user_service: "UserService"):
    try:
        data = await user_service.get_profile(
            callback.from_user.id
        )
    except AppExceptions as e:
        await callback.answer(
            text=e.message,
            show_alert=True
        )
    else:
        await callback.message.edit_text(
            text=PROFILE.format(
                id=data.id,
                tg_id=data.tg_id,
                cart=[i.model_dump() for i in data.cart],
                purchases=[i.model_dump() for i in data.purchases]
            ),
            reply_markup=home_keyboard(),
        )


@user_route.callback_query(F.data == 'main_menu')
async def main_menu(callback: "CallbackQuery"):
    await callback.message.edit_text(
        text=HELLO_WORLD.format(
            username=callback.from_user.username,
        ),
        reply_markup=home_keyboard()
    )