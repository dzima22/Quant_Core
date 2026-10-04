from Data.Providers.yachoo.provider import YahooREST
from Data.Providers.ecb.provider import ECBProvider
from Data.Providers.Finnhub.provider import FinnhubProvider
from Core.exceptions.exceptions import QuantTerminalException
import sys
from Core.utils.utils import parse_ecb,parse_usaspending,parse_lobbying,parse_basic_financials,data_parse_dataframes,data_parse_series,data_parse_history
from Core.models.request_models import GetDailyExchangeRateParams,GetPeriodExchangeRateParams,GetInterestRateParams,GetYieldCurveParams,YachooGetHistory,YachooSymbol,GetUSASpeandingPlusLobbingParams,GetBasicFinancialsParams
from typing import Callable, Any

from Core.cache.redis_cache import RedisCache
from Core.cache.cache_keys import build_cache_key


class DataService:

    def __init__(self, yahoo:YahooREST, finnhub:FinnhubProvider, ecb:ECBProvider,cache: RedisCache | None = None):
        try:
            self.yahoo = yahoo
            self.finnhub = finnhub
            self.ecb = ecb
            self.cache = cache
        except Exception as e:
            raise QuantTerminalException(e, sys)
    def _cached(self,namespace: str,payload,loader: Callable[[], Any],ttl: int):
        try:
            if self.cache is None:
                return loader()

            key = build_cache_key(
                namespace,
                payload,
            )

            cached = self.cache.get(key)

            if cached is not None:
                return cached

            data = loader()

            self.cache.set(
                key=key,
                value=data,
                ttl=ttl,)
            return data
        except Exception as e:
            raise QuantTerminalException(e, sys)
    def data_parse_daily_exchange_rate(self, params: GetDailyExchangeRateParams)-> list[dict]:
        try:
            return self._cached(namespace="daily_exchange_rate",payload=params,ttl=3600,loader=lambda:parse_ecb(self.ecb.get_daily_avg_exchange_rate(params=params)))
        except Exception as e:
            raise QuantTerminalException(e, sys)
    def data_parse_period_exchange_rate(self, params: GetPeriodExchangeRateParams)-> list[dict]:
        try:
            return self._cached(namespace="period_exchange_rate",payload=params,ttl=3600,loader=lambda:parse_ecb(self.ecb.get_period_exchange_rate(params=params)))
        except Exception as e:
            raise QuantTerminalException(e, sys)
    def data_parse_interest_rate(self, params: GetInterestRateParams)-> list[dict]:
        try:
            return self._cached(namespace="interest_rate",payload=params,ttl=3600,loader=lambda:parse_ecb(self.ecb.get_interest_rate(params=params)))
        except Exception as e:
            raise QuantTerminalException(e, sys)
    def data_parse_yield_curve(self, params: GetYieldCurveParams)-> list[dict]:
        try:
            return self._cached(namespace="yield_curve",payload=params,ttl=3600,loader=lambda:parse_ecb(self.ecb.get_yield_curve(params=params)))
        except Exception as e:
            raise QuantTerminalException(e, sys)
    def data_parse_history(self, params:YachooGetHistory)-> list[dict]:
        try:
            return self._cached(namespace="history",payload=params,ttl=300,loader=lambda: data_parse_history(df=self.yahoo.get_history(params=params)))
        except Exception as e:
            raise QuantTerminalException(e, sys)
    def data_parse_cashflow(self, symbol:YachooSymbol)-> list[dict]:
        try:
            return self._cached(namespace="cashflow",payload=symbol,ttl=21600,loader=lambda:data_parse_dataframes(df=self.yahoo.get_cashflow(symbol=symbol)))
        except Exception as e:
            raise QuantTerminalException(e, sys)
    def data_parse_balance_sheet(self, symbol:YachooSymbol)-> list[dict]:
        try:
            return self._cached(namespace="balance_sheet",payload=symbol,ttl=21600,loader=lambda:data_parse_dataframes(df=self.yahoo.get_balance_sheet(symbol=symbol)))
        except Exception as e:
            raise QuantTerminalException(e, sys)
    def data_parse_financials_yachoo(self, symbol:YachooSymbol)-> list[dict]:
        try:
            return self._cached(namespace="financials_yachoo",payload=symbol,ttl=21600,loader=lambda:data_parse_dataframes(df=self.yahoo.get_financials(symbol=symbol)))
        except Exception as e:
            raise QuantTerminalException(e, sys)
    def data_parse_quarterly_financials(self, symbol:YachooSymbol)-> list[dict]:
        try:
            return self._cached(namespace="quarterly_financials",payload=symbol,ttl=21600,loader=lambda:data_parse_dataframes(df=self.yahoo.get_quarterly_financials(symbol=symbol)))
        except Exception as e:
            raise QuantTerminalException(e, sys)
    def data_parse_dividents(self, symbol:YachooSymbol)-> list[dict]:
        try:
            return self._cached(namespace="dividends",payload=symbol,ttl=21600,loader=lambda:data_parse_series(series=self.yahoo.get_dividends(symbol=symbol)))
        except Exception as e:
            raise QuantTerminalException(e, sys)
    def data_parse_splits(self, symbol:YachooSymbol)-> list[dict]:
        try:
            return self._cached(namespace="splits",payload=symbol,ttl=21600,loader=lambda: data_parse_series(series=self.yahoo.get_splits(symbol=symbol)))
        except Exception as e:
            raise QuantTerminalException(e, sys)
    def data_parse_spending(self, params:GetUSASpeandingPlusLobbingParams)->dict:
        try:
            return self._cached(namespace="spending",payload=params,ttl=3600,loader=lambda:parse_usaspending(self.finnhub.get_usa_spending(params=params)))
        except Exception as e:
            raise QuantTerminalException(e, sys)
    def data_parse_lobbing(self, params:GetUSASpeandingPlusLobbingParams) -> dict:
        try:
            return self._cached(namespace="lobbing",payload=params,ttl=3600,loader=lambda:parse_lobbying(self.finnhub.get_senate_lobbying(params=params)))
        except Exception as e:
            raise QuantTerminalException(e, sys)
    def data_parse_financials(self,params:GetBasicFinancialsParams) -> dict:
        try:
            return self._cached(namespace="financials_finnhub",payload=params,ttl=30000,loader=lambda:parse_basic_financials(self.finnhub.get_basic_financials(params=params)))
        except Exception as e:
            raise QuantTerminalException(e, sys)


    