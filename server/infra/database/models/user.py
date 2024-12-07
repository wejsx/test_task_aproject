from typing import Optional, List

from sqlalchemy import String, Integer, BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class ItemBaseModel(Base):
    __abstract__ = True
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    tg_id: Mapped[BigInteger] = mapped_column(BigInteger, ForeignKey('users.tg_id'))
    product_id: Mapped[str] = mapped_column(String(100))
    product_name: Mapped[str] = mapped_column(String(1000))
    product_price: Mapped[int] = mapped_column(Integer)


class UserCartModel(ItemBaseModel):
    __tablename__ = 'user_cart'


class UserPurchasesModel(ItemBaseModel):
    __tablename__ = 'user_purchases'


class UserModel(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True, index=True, nullable=True)
    cart: Mapped[Optional[List["UserCartModel"]]] = relationship("UserCartModel", cascade="all, delete-orphan", lazy='selectin')
    purchases: Mapped[Optional[List["UserPurchasesModel"]]] = relationship("UserPurchasesModel", cascade="all, delete-orphan", lazy='selectin')

    def __repr__(self) -> str:
        return f'<UserModel(id={self.id}, tg_id={self.tg_id}\n' \
        f'cart={self.cart}\n' \
        f'purchases={self.purchases})>'
