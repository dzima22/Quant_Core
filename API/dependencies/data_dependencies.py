from functools import lru_cache

from Data.Services.DataService import DataService
from Data.Providers.yachoo.provider import YahooREST
from Data.Providers.ecb.provider import ECBProvider
from Data.Providers.Finnhub.provider import FinnhubProvider

from Core.cache.redis_cache import RedisCache
from Core.configs.settings import get_settings


@lru_cache
def get_cache() -> RedisCache:
    settings = get_settings()
    return RedisCache(settings.redis_url)


@lru_cache
def get_data_service() -> DataService:

    return DataService(
        yahoo=YahooREST(),
        finnhub=FinnhubProvider(),
        ecb=ECBProvider(),
        cache=get_cache(),
    )
