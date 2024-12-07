from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional, Union

from core.settings import settings
from infra.clients.dtos.api_v1_dto import (
    GetProductsDto,
    ResponseMessageDto,
    RegisterDto,
    UserDto,
    GetCartDto,
    GetPurchaseDto,
    AddProductStoreDto,
    AddProductCartDto,
    BuyProductDto,
    DeleteProductCartDto,
    GetProductDto,
)

if TYPE_CHECKING:
    from infra.clients import HTTPClient



@dataclass(eq=False, order=False, unsafe_hash=False)
class ApiV1Client:
    http_client: "HTTPClient"

    async def get_products(self) -> Optional[GetProductsDto]:
        url = settings.api_v1.get_products_url
        print(f'отправляем гет запроооооссс')
        response = await self.http_client.get(url)
        return GetProductsDto(**response)


    async def get_product(self, product_id: str) ->  Union[GetProductDto, ResponseMessageDto]:
        url = settings.api_v1.get_product_url
        params = {'product_id': product_id}
        response = await self.http_client.get(url, params)
        if 'detail' in response:
            return ResponseMessageDto(**response)
        return GetProductDto(**response)

    
    async def register(self, data: RegisterDto) -> ResponseMessageDto:
        url = settings.api_v1.register_url
        json = data.model_dump()
        response = await self.http_client.post(url, json)
        return ResponseMessageDto(**response)


    async def get_cart(self, tg_id: int) -> GetCartDto:
        url = settings.api_v1.get_cart_url
        params = {'tg_id': tg_id}
        response = await self.http_client.get(url, params)
        return GetCartDto(**response)
    

    async def get_purchase(self, tg_id: int) -> GetPurchaseDto:
        url = settings.api_v1.get_purchase_url
        params = {'tg_id': tg_id}
        response = await self.http_client.get(url, params)
        return GetPurchaseDto(**response)
    

    async def add_product_cart(self, data: AddProductCartDto) -> ResponseMessageDto:
        url = settings.api_v1.add_product_cart_url
        json = data.model_dump()
        response = await self.http_client.post(url, json)
        return ResponseMessageDto(**response)
    
    
    async def add_product_store(self, data: AddProductStoreDto) -> ResponseMessageDto:
        url = settings.api_v1.add_product_store_url
        json = data.model_dump()
        response = await self.http_client.post(url, json)
        return ResponseMessageDto(**response)
    
    
    async def buy_product(self, data: BuyProductDto) -> ResponseMessageDto:
        url = settings.api_v1.buy_product_url
        json = data.model_dump()
        response = await self.http_client.post(url, json)
        return ResponseMessageDto(**response)
    

    async def delete_product_cart(self, data: DeleteProductCartDto) -> ResponseMessageDto:
        url = settings.api_v1.del_product_cart_url
        json = data.model_dump()
        response = await self.http_client.post(url, json)
        return ResponseMessageDto(**response)


    async def get_user(self, tg_id: int) -> Union[UserDto, ResponseMessageDto]:
        url = settings.api_v1.get_user_url
        params = {'tg_id': tg_id}
        response = await self.http_client.get(url, params)
        if 'detail' in response:
            return ResponseMessageDto(**response)
        return UserDto(**response)