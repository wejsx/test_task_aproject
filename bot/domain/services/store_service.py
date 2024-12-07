from dataclasses import dataclass
from typing import TYPE_CHECKING, Union


from infra.mappers import (
    convert_add_product_store_to_dto
)
from domain.entities import ProductEntity, StoreEntity

if TYPE_CHECKING:
    from infra.repository import StoreRepository
    

@dataclass(eq=False, order=False, unsafe_hash=False)
class StoreService:
    store_repository: "StoreRepository"


    async def add_product(self, name: str, price: int):
        dto = convert_add_product_store_to_dto(name, price)
        return await self.store_repository.add_product(dto)
    

    async def get_product(self, product_id: str) -> Union[str, ProductEntity]:
        data = await self.store_repository.get_product(product_id)
        if isinstance(data, ProductEntity):
            return data
        return data.detail
    
    
    async def get_products(self) -> StoreEntity:
        return await self.store_repository.get_products()