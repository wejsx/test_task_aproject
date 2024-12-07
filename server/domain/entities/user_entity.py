from typing import Optional, List
from pydantic import BaseModel, ConfigDict


class BaseItemEntity(BaseModel):
    id: Optional[int] = None
    tg_id: int
    product_id: str
    product_name: str
    product_price: int

    model_config = ConfigDict(
        from_attributes=True
    )

class CartEntity(BaseItemEntity):
    ...


class PurchaseEntity(BaseItemEntity):
    ...


class UserCartEntity(BaseModel):
    cart: List[CartEntity]


class UserPurchaseEntity(BaseModel):
    purchases: List[PurchaseEntity]


class UserEntity(BaseModel):
    id: int
    tg_id: int
    cart: Optional[List[CartEntity]] = []
    purchases: Optional[List[PurchaseEntity]] = []

    model_config = ConfigDict(
        from_attributes=True
    )