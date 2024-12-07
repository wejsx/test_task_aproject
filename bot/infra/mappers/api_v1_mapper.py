from typing import TYPE_CHECKING, Union

from domain.entities import (
    ProductEntity,
    StoreEntity,
    UserCartEntity,
    UserPurchaseEntity,
    UserEntity,
)

from infra.clients import (
    AddProductStoreDto, 
    BuyProductDto, 
    AddProductCartDto,
    DeleteProductCartDto,
    RegisterDto,
    GetProductDto,
    ResponseMessageDto,
    UserDto,
)

if TYPE_CHECKING:
    from infra.clients import (
        GetProductsDto,
        GetCartDto,
        GetPurchaseDto,
    )


def convert_add_product_store_to_dto(name: str, price: int) -> AddProductStoreDto:
    return AddProductStoreDto(name=name, price=price)

def convert_get_product_to_entity(data: Union[GetProductDto, ResponseMessageDto]) -> ProductEntity:
    if isinstance(data, GetProductDto):
        return ProductEntity(**data.model_dump())
    return data

def convert_store_to_entity(products: "GetProductsDto") -> StoreEntity:
    return StoreEntity(**products.model_dump())

def convert_user_cart_to_entity(cart: "GetCartDto") -> UserCartEntity:
    return UserCartEntity(**cart.model_dump())

def convert_user_purchase_to_entity(purchase: "GetPurchaseDto") -> UserPurchaseEntity:
    return UserPurchaseEntity(**purchase.model_dump())

def convert_buy_product_to_dto(tg_id: int, product_id: str) -> BuyProductDto:
    return BuyProductDto(tg_id=tg_id, product_id=product_id)

def convert_add_product_cart_to_dto(tg_id: int, product_id: str) -> AddProductCartDto:
    return AddProductCartDto(tg_id=tg_id, product_id=product_id)

def convert_del_product_cart_to_dto(tg_id: int, product_id: str) -> DeleteProductCartDto:
    return DeleteProductCartDto(tg_id=tg_id, product_id=product_id)

def convert_register_to_dto(tg_id: int) -> RegisterDto:
    return RegisterDto(tg_id=tg_id)

def convert_user_to_entity(data: Union[UserDto, ResponseMessageDto]) -> UserEntity:
    if isinstance(data, UserDto):
        return UserEntity(**data.model_dump())
    return data