from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, PostgresDsn


class ApiClientV1(BaseModel): #TODO: УБРАТЬ
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


class BotAiogramSettings(BaseModel): #TODO: УБРАТЬ
    token: str


class DBSettings(BaseModel):
    url: PostgresDsn


class AppSettings(BaseSettings):
    db: DBSettings
    api_v1: ApiClientV1 #TODO: УБРАТЬ
    bot: BotAiogramSettings #TODO: УБРАТЬ

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        env_ignore_empty=True,
        env_nested_delimiter='__',
        env_prefix='APP_SETTINGS__',
        
    )


settings = AppSettings()