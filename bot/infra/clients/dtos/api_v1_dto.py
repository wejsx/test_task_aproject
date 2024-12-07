from typing import Optional, List
from pydantic import BaseModel


class ProductDto(BaseModel):
    id: int
    tg_id: Optional[int] = None
    product_id: str
    product_name: str
    product_price: int


class GetProductDto(ProductDto):
    ...


class GetProductsDto(BaseModel):
    products: Optional[List[ProductDto]] = None


class GetCartDto(BaseModel):
    cart: Optional[List[ProductDto]] = None


class GetPurchaseDto(BaseModel):
    purchases: Optional[List[ProductDto]] = None


class UserDto(BaseModel):
    id: int
    tg_id: int
    cart: Optional[List[ProductDto]] = None
    purchases: Optional[List[ProductDto]] = None


class RegisterDto(BaseModel):
    tg_id: int


class BuyProductDto(BaseModel):
    tg_id: int
    product_id: str


class AddProductCartDto(BaseModel):
    tg_id: int
    product_id:str


class DeleteProductCartDto(BaseModel):
    tg_id: int
    product_id: int


class AddProductStoreDto(BaseModel):
    name: str
    price: int


class ResponseMessageDto(BaseModel):
    detail: str