from dataclasses import dataclass
from typing import TYPE_CHECKING

from infra.exceptions import ProductNotFound, ProductRemoveCartNotFound
from domain import CartEntity, PurchaseEntity, UserEntity, UserPurchaseEntity, UserCartEntity

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio.session import AsyncSession
    from infra.repository import UserRepository, StoreRepository


@dataclass(eq=False, order=False, unsafe_hash=False)
class UserService:
    user_repository: "UserRepository"
    store_repository: "StoreRepository"

    async def buy_product(self, tg_id: int, product_id: str, session: "AsyncSession") -> dict:
        product = await self.store_repository.get_product(
            product_id,
            session=session
        )
        if not product:
            raise ProductNotFound(404)
        
        check_product_in_cart = self.user_repository.get_product_from_cart(tg_id, product_id, session)
        if check_product_in_cart:
            await self.user_repository.remove_product_cart(
                product_id,
                tg_id,
                session
            )
        entity = PurchaseEntity(
            tg_id=tg_id,
            product_id=product.product_id,
            product_name=product.product_name,
            product_price=product.product_price
        )
        await self.user_repository.add_product_purchase(entity, session)
        return {'detail': 'Вы успешно купили арбуз!'}
    

    async def add_cart(self, tg_id, product_id: str, session: "AsyncSession") -> dict:
        product = await self.store_repository.get_product(
            product_id,
            session=session
        )
        if not product:
            raise ProductNotFound(404)
        entity = CartEntity(
            tg_id=tg_id,
            product_id=product.product_id,
            product_name=product.product_name,
            product_price=product.product_price
        )
        await self.user_repository.add_product_cart(entity, session)
        return {'detail': 'Арбуз успешно добавлен в корзину!'}
    
    async def get_purchase(self, tg_id: int, session: "AsyncSession") -> UserPurchaseEntity:
        data = await self.user_repository.get_purchase(tg_id, session)
        return data
    

    async def get_cart(self, tg_id: int, session: "AsyncSession") -> UserCartEntity:
        data = await self.user_repository.get_cart(tg_id, session)
        return data

    
    async def delete_product_cart(self, tg_id: int, product_id: str, session: "AsyncSession") -> dict:
        status = await self.user_repository.remove_product_cart(product_id, tg_id, session)
        if not status:
            raise ProductRemoveCartNotFound(404)
        return {'detail': 'Арбуз успешно удален!'}
    
    
    async def register(self, tg_id: int, session: "AsyncSession") -> UserEntity | dict:
        check_user = await self.user_repository.get_user(tg_id, session)
        if check_user:
            return {'detail': 'Пользователь существует!'}
        await self.user_repository.add_user(tg_id, session)
        return {'detail': 'Добро пожаловать в магазин арбузов!'}


    async def get_user(self, tg_id: int, session: "AsyncSession") -> UserEntity | dict:
        user = await self.user_repository.get_user(tg_id, session)
        if not user:
            return {'detail': 'Пользователь не найден!'}
        return user