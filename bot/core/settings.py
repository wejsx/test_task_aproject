from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, Field


class BotAiogramSettings(BaseModel):
    token: str


class ApiClientV1(BaseModel):
    get_products_url: str
    get_product_url: str
    register_url: str
    add_product_store_url: str
    buy_product_url: str
    add_product_cart_url: str
    get_cart_url: str
    get_purchase_url: str
    get_user_url: str
    del_product_cart_url: str


class AppSettings(BaseSettings):
    bot: BotAiogramSettings
    api_v1: ApiClientV1
    
    model_config = SettingsConfigDict(
        env_file='.env.example',
        env_file_encoding='utf-8',
        env_ignore_empty=True,
        env_nested_delimiter='__',
        env_prefix='APP_SETTINGS__',
    )


settings = AppSettings()