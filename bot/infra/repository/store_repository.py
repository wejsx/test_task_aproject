from dataclasses import dataclass
from typing import TYPE_CHECKING, Union

from infra.clients import GetProductDto
from infra.mappers import (
    convert_get_product_to_entity,
    convert_store_to_entity,
)

if TYPE_CHECKING:
    from domain.entities import ProductEntity, StoreEntity
    from infra.clients import (
        ApiV1Client,
        AddProductStoreDto,
        ResponseMessageDto,
    )


@dataclass(eq=False, unsafe_hash=False, order=False)
class StoreRepository:
    api_client: "ApiV1Client"

    async def add_product(self, product: "AddProductStoreDto") -> "ResponseMessageDto":
        return await self.api_client.add_product_store(product)
    

    async def get_product(self, product_id: str) -> Union["ResponseMessageDto", "ProductEntity"]:
        data = await self.api_client.get_product(product_id)
        entity_or_dto = convert_get_product_to_entity(data)
        return entity_or_dto
    
    
    async def get_products(self) -> "StoreEntity":
        data = await self.api_client.get_products()
        entity = convert_store_to_entity(data)
        return entity