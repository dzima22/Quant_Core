from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    finnhub_api_key: str = ""

    redis_url: str = "redis://localhost:6379/0"

    cache_default_ttl: int = 300

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()