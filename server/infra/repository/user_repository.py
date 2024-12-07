from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from sqlalchemy.exc import DatabaseError
from sqlalchemy.future import select

from infra.database import UserCartModel, UserPurchasesModel, UserModel
from infra.exceptions import DataBaseException

from domain import (
    CartEntity,
    PurchaseEntity,
    UserEntity, 
    UserCartEntity, 
    UserPurchaseEntity,
    ProductEntity,
)


if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio.session import AsyncSession


@dataclass(eq=False, order=False, unsafe_hash=False)
class UserRepository:

    async def get_user(self, tg_id: int, session: "AsyncSession") -> Optional[UserEntity]:
        try:
            result = await session.execute(select(UserModel).filter(UserModel.tg_id == tg_id))
            user = result.scalars().first()
        except DatabaseError as e:
            await session.rollback()
            raise DataBaseException(400) from e
        else:
            if not user:
                return None
            return UserEntity.model_validate(user)


    async def add_product_cart(self, entity: CartEntity, session: "AsyncSession") -> ProductEntity:
        cart_model = UserCartModel(
            tg_id=entity.tg_id,
            product_id=entity.product_id,
            product_name=entity.product_name,
            product_price=entity.product_price,
        )
        
        try:
            session.add(cart_model)
            await session.commit()
        except DatabaseError as e:
            await session.rollback()
            raise DataBaseException(400) from e
        else:
            await session.refresh(cart_model)
            return CartEntity.model_validate(cart_model)


    async def add_product_purchase(self, entity: PurchaseEntity, session: "AsyncSession") -> ProductEntity:
        purchase_model = UserPurchasesModel(
            tg_id=entity.tg_id,
            product_id=entity.product_id,
            product_name=entity.product_name,
            product_price=entity.product_price,
        )
        
        try:
            session.add(purchase_model)
            await session.commit()
        except DatabaseError as e:
            print(e)
            await session.rollback()
            raise DataBaseException(400) from e
        else:
            await session.refresh(purchase_model)
            return PurchaseEntity.model_validate(purchase_model)


    async def get_cart(self, tg_id: int, session: "AsyncSession") -> UserCartEntity:
        try:
            result = await session.execute(select(UserCartModel).filter(UserCartModel.tg_id == tg_id))
            cart = result.scalars().all()
        except DatabaseError as e:
            await session.rollback()
            raise DataBaseException(400) from e
        else:
            if not cart:
                return UserCartEntity(cart=[])
            return UserCartEntity(cart=cart)
        
    
    async def get_product_from_cart(self, tg_id: int, product_id: str, session: "AsyncSession") -> CartEntity:
        try:
            result = await session.execute(select(UserCartModel).filter((UserCartModel.tg_id == tg_id) & (UserCartModel.product_id == product_id)))
            product = result.scalars().first()
        except DatabaseError as e:
            await session.rollback()
            raise DataBaseException(400) from e
        else:
            if not product:
                return None
            return UserCartEntity.model_validate(product)
    
    
    async def remove_product_cart(self, product_id: int, tg_id: int, session: "AsyncSession") -> Optional[bool]:
        try:
            result = await session.execute(select(UserCartModel).filter((UserCartModel.tg_id == tg_id) & (UserCartModel.product_id == product_id)))
            cart = result.scalars().first()
        except DatabaseError as e:
            await session.rollback()
            raise DataBaseException(400) from e
        else:
            if not cart:
                return None
            await session.delete(cart)
            await session.commit()
            return True
        

    async def get_purchase(self, tg_id: int, session: "AsyncSession") -> Optional[UserPurchaseEntity]:
        try:
            result = await session.execute(select(UserPurchasesModel).filter(UserPurchasesModel.tg_id == tg_id))
            purchases = result.scalars().all()
        except DatabaseError as e:
            await session.rollback()
            raise DataBaseException(400) from e
        else:
            if not purchases:
                return UserPurchaseEntity(purchases=[])
            return UserPurchaseEntity(purchases=purchases)
        
    
    async def add_user(self, tg_id: int, session: "AsyncSession") -> UserEntity:
        user_model = UserModel(
            tg_id=tg_id
        )
        try:
            session.add(user_model)
            await session.commit()
        except DatabaseError as e:
            print(e)
            await session.rollback()
            raise DataBaseException(400) from e
        else:
            await session.refresh(user_model)
            return UserEntity.model_validate(user_model)