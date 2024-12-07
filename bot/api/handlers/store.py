from typing import TYPE_CHECKING

from aiogram import Router, Bot, F
from aiogram.fsm.context import FSMContext

from api.keyboards import home_keyboard, store_keyboard, product_keyboard
from infra.exceptions.errors import AppExceptions
from api.states import AddProductStoreState

from utils.const.messages import (
    STORE_EMPTY,
    STORE_NOT_EMPTY,
    PRODUCT_DESCRIPTION,
    PRODUCT_DESCRIPTION_EMPTY,
    ADD_PRODUCT_STORE,
)

if TYPE_CHECKING:
    from aiogram.types import Message, CallbackQuery
    from domain.services import UserService, StoreService


store_route = Router()


@store_route.callback_query(F.data == 'get_products')
async def get_products(callback: "CallbackQuery", bot: Bot, user_service: "UserService", store_service: "StoreService"):
    try:
        print(f'вызов гет продукс')
        products = await store_service.get_products()
    except AppExceptions as e:
        await callback.answer(
            text=e.message,
            show_alert=True
        )
    else:
        await callback.message.edit_text(
            text=STORE_EMPTY if len(products.products) < 1 else STORE_NOT_EMPTY,
            reply_markup=store_keyboard(products)
        )


@store_route.callback_query(F.data.startswith('get_product_'))
async def get_product(callback: "CallbackQuery", bot: Bot, user_service: "UserService", store_service: "StoreService"):
    product_id = callback.data.split('_')[-1]
    try:
        product = await store_service.get_product(product_id)
    except AppExceptions as e:
        await callback.answer(
            text=e.message,
            show_alert=True
        )
    else:
        await callback.message.edit_text(
            text=PRODUCT_DESCRIPTION_EMPTY if isinstance(product, str) else\
            PRODUCT_DESCRIPTION.format(
                name=product.product_name,
                price=product.product_price
            ),
            reply_markup=product_keyboard(True) if isinstance(product, str) else\
            product_keyboard(product.product_id)
        )


@store_route.callback_query(F.data == 'add_product_store')
async def add_product_store(callback: "CallbackQuery", state: FSMContext):
    await callback.message.edit_text(
        text=ADD_PRODUCT_STORE
    )
    await state.set_state(AddProductStoreState.body)
