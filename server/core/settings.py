from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, PostgresDsn


class DBSettings(BaseModel):
    url: PostgresDsn


class AppSettings(BaseSettings):
    db: DBSettings

    model_config = SettingsConfigDict(
        env_file='.env.example',
        env_file_encoding='utf-8',
        env_ignore_empty=True,
        env_nested_delimiter='__',
        env_prefix='APP_SETTINGS__',
        
    )


settings = AppSettings()