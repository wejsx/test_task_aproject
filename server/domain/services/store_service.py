from dataclasses import dataclass
from uuid import uuid4
from typing import TYPE_CHECKING

from infra.repository import StoreRepository
from infra.exceptions import ProductNotFound

from domain import ProductEntity, ProductsEntity

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio.session import AsyncSession


@dataclass(eq=False, order=False, unsafe_hash=False)
class StoreService:
    store_repository: StoreRepository


    async def add(self, name: str, price: int, session: "AsyncSession") -> dict:
        product_id = self._generate_product_id()
        entity = ProductEntity(
            product_id=product_id,
            product_name=name,
            product_price=price
        )
        await self.store_repository.add_products(entity, session)
        return {'detail': 'Вы успешно выставили арбуз на продажу!'}
    

    async def get_product(self, product_id: str, session: "AsyncSession") -> ProductEntity:
        product = await self.store_repository.get_product(product_id, session)
        if not product:
            raise ProductNotFound(404)
        return product


    async def get_products(self, session: "AsyncSession") -> ProductsEntity | dict:
        products = await self.store_repository.get_products(session)
        if products:
            return products
        return {'detail': 'Арбузов нет в наличии!'}


    def _generate_product_id(self) -> str:
        return str(uuid4())