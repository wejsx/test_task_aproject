from dataclasses import dataclass
from typing import TYPE_CHECKING, Union

from infra.mappers import (
    convert_user_cart_to_entity,
    convert_user_purchase_to_entity,
    convert_user_to_entity,
)

if TYPE_CHECKING:
    from domain.entities import UserCartEntity, UserPurchaseEntity, UserEntity
    from infra.clients import (
        ApiV1Client,
        ResponseMessageDto,
        BuyProductDto,
        AddProductCartDto,
        DeleteProductCartDto,
        RegisterDto,
        UserDto,
    )


@dataclass(eq=False, unsafe_hash=False, order=False)
class UserRepository:
    api_client: "ApiV1Client"

    async def get_cart(self, tg_id: int) -> "UserCartEntity":
        data = await self.api_client.get_cart(tg_id)
        entity = convert_user_cart_to_entity(data)
        return entity
    
    
    async def get_purchase(self, tg_id: int) -> "UserPurchaseEntity":
        data = await self.api_client.get_purchase(tg_id)
        entity = convert_user_purchase_to_entity(data)
        return entity
    

    async def buy_product(self, product: "BuyProductDto") -> "ResponseMessageDto":
        data = await self.api_client.buy_product(product)
        return data
    

    async def add_product_cart(self, product: "AddProductCartDto") -> "ResponseMessageDto":
        data = await self.api_client.add_product_cart(product)
        return data
    

    async def delete_product_cart(self, product: "DeleteProductCartDto") -> "ResponseMessageDto":
        data = await self.api_client.delete_product_cart(product)
        return data
    

    async def register(self, data: "RegisterDto") -> "ResponseMessageDto":
        data = await self.api_client.register(data)
        return data
    
    
    async def get_user(self, tg_id: int) -> Union["UserDto", "ResponseMessageDto"]:
        data = await self.api_client.get_user(tg_id)
        entity_or_dto = convert_user_to_entity(data)
        return entity_or_dto
