from typing import List
from pydantic import BaseModel, ConfigDict


class BuyProductSchema(BaseModel):
    tg_id: int
    product_id: str

    model_config = ConfigDict(
        json_schema_extra={
            'example': {
                'tg_id': 1232183231,
                'product_id': '4e54f60a-c067-4a40-ba31-35068b278920'
            }
        }
    )


class AddProductCartSchema(BaseModel):
    tg_id: int
    product_id: str

    model_config = ConfigDict(
        json_schema_extra={
            'example': {
                'tg_id': 1232183231,
                'product_id': '4e54f60a-c067-4a40-ba31-35068b278920'
            }
        }
    )


class DeleteProductCartSchema(BaseModel):
    tg_id: int
    product_id: str

    model_config = ConfigDict(
        json_schema_extra={
            'example': {
                'tg_id': 1232183231,
                'product_id': '4e54f60a-c067-4a40-ba31-35068b278920'
            }
        }
    )


class StoreAddProductSchema(BaseModel):
    name: str
    price: int

    model_config = ConfigDict(
        json_schema_extra={
            'example': {
                'name': 'Арбуз зелени',
                'price': 200
            }
        }
    )


class StoreProductSchema(BaseModel):
    id: int
    product_id: str
    product_name: str
    product_price: int

    model_config = ConfigDict(
        json_schema_extra={
            'example': {
                'id': 1,
                'product_id': '4e54f60a-c067-4a40-ba31-35068b278920',
                'product_name': 'Арбуз зелени',
                'product_price': 200 
            }
        }
    )


class StoreGetProductsSchema(BaseModel):
    products: List[StoreProductSchema]

    model_config = ConfigDict(
        json_schema_extra={
            'example': {
                'products': [
                    {
                        'id': 1,
                        'product_id': '4e54f60a-c067-4a40-ba31-35068b278920',
                        'product_name': 'Арбуз зелени',
                        'product_price': 200 
                    },
                    {
                        'id': 2,
                        'product_id': '5x54f60a-c067-4a40-ba31-65068b278920',
                        'product_name': 'Арбуз красни',
                        'product_price': 300 
                    }
                ]
            }
        }
    )


class RegisterSchema(BaseModel):
    tg_id: int

    model_config = ConfigDict(
        json_schema_extra={
            'example': {
                'tg_id': 1232183231,
            }
        }
    )