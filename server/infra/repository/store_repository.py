from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from sqlalchemy.exc import DatabaseError
from sqlalchemy.future import select

from domain import ProductEntity, ProductsEntity

from infra.database import ProductsModel
from infra.exceptions import DataBaseException


if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio.session import AsyncSession


@dataclass(eq=False, order=False, unsafe_hash=False)
class StoreRepository:

    async def get_products(self, session: "AsyncSession") -> Optional[ProductsEntity]:
        try:
            result = await session.execute(select(ProductsModel).order_by(ProductsModel.id.desc()))
            products = result.scalars().all()
        except DatabaseError as e:
            await session.rollback()
            raise DataBaseException(400) from e
        else:
            return ProductsEntity(products=products)
        

    async def get_product(self, product_id: str, session: "AsyncSession") -> ProductEntity | None:
        try:
            result = await session.execute(select(ProductsModel).filter(ProductsModel.product_id == product_id))
            product = result.scalars().first()
        except DatabaseError as e:
            await session.rollback()
            raise DataBaseException(400) from e
        else:
            if not product:
                return None
            return ProductEntity.model_validate(product)
        
        
    async def add_products(self, entity: ProductEntity, session: "AsyncSession") -> ProductEntity:
        product_model = ProductsModel(
            product_id=entity.product_id,
            product_name=entity.product_name,
            product_price=entity.product_price,
        )
        try:
            session.add(product_model)
            await session.commit()
        except DatabaseError as e:
            await session.rollback()
            raise DataBaseException(400) from e
        else:
            await session.refresh(product_model)
            return ProductEntity.model_validate(product_model)