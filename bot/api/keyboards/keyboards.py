from typing import TYPE_CHECKING

from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

if TYPE_CHECKING:
    from domain.entities import StoreEntity


def home_keyboard():
    builder = InlineKeyboardBuilder()

    builder.add(
        InlineKeyboardButton(
            text="Магазин Арбузов", callback_data="get_products"
        )
    )
    builder.add(
        InlineKeyboardButton(
            text="Выставить арбуз на продажу", callback_data="add_product_store"
        )
    )
    builder.add(
        InlineKeyboardButton(
            text="Профиль", callback_data="profile"
        )
    )
    builder.adjust(1, 1)
    return builder.as_markup()


def store_keyboard(products: "StoreEntity"):
    builder = InlineKeyboardBuilder()

    for product in products.products:
        builder.add(
            InlineKeyboardButton(
                text=product.product_name,
                callback_data=f'get_product_{product.product_id}',
            )
        )

    builder.add(
        InlineKeyboardButton(
            text='Главное меню',
            callback_data='main_menu',
        )
    )
    builder.adjust(2, 2)
    return builder.as_markup()


def product_keyboard(product_id: str, empty: bool = False):
    builder = InlineKeyboardBuilder()

    if empty:
        builder.add(
            InlineKeyboardButton(
                text='Вернуться назад',
                callback_data='get_products',
            )
        )      
        builder.adjust(1, 1)
        return builder.as_markup()

    builder.add(
        InlineKeyboardButton(
            text='Купить',
            callback_data=f'buy_product_{product_id}',
        )
    )
    builder.add(
        InlineKeyboardButton(
            text='Добавить в корзину',
            callback_data=f'add_cart_{product_id}',
        )
    )
    builder.add(
        InlineKeyboardButton(
            text='Вернуться назад',
            callback_data='get_products',
        )
    )

    builder.adjust(1, 1)
    return builder.as_markup()