from dataclasses import dataclass
from typing import TYPE_CHECKING

from domain.entities import UserCartEntity, UserPurchaseEntity

from infra.mappers import (
    convert_buy_product_to_dto,
    convert_add_product_cart_to_dto,
    convert_del_product_cart_to_dto,
    convert_register_to_dto,
)

if TYPE_CHECKING:
    from infra.repository import UserRepository



@dataclass(eq=False, order=False, unsafe_hash=False)
class UserService:
    user_repository: "UserRepository"
    

    async def buy_product(self, tg_id: int, product_id: str):
        dto = convert_buy_product_to_dto(tg_id, product_id)
        return await self.user_repository.buy_product(dto)


    async def get_cart(self, tg_id: int) -> UserCartEntity:
        return await self.user_repository.get_cart(tg_id)
    

    async def get_purchase(self, tg_id: int) -> UserPurchaseEntity:
        return await self.user_repository.get_purchase(tg_id)


    async def add_product_cart(self, tg_id: int, product_id: str):
        dto = convert_add_product_cart_to_dto(tg_id, product_id)
        return await self.user_repository.add_product_cart(dto)
    

    async def delete_product_cart(self, tg_id: int, product_id: str):
        dto = convert_del_product_cart_to_dto(tg_id, product_id)
        return await self.user_repository.delete_product_cart(dto)
    

    async def register(self, tg_id: int):
        dto = convert_register_to_dto(tg_id)
        return await self.user_repository.register(dto)
    
    
    async def get_profile(self, tg_id: int):
        return await self.user_repository.get_user(tg_id)