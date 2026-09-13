from Data.Providers.yachoo.provider import YahooREST
from Data.Providers.ecb.provider import ECBProvider
from Data.Providers.Finnhub.provider import FinnhubProvider
from Core.exceptions.exceptions import QuantTerminalException
import sys
from utils.utils import parse_ecb
from configs.models import GetDailyExchangeRateParams,GetPeriodExchangeRateParams,GetInterestRateParams,GetYieldCurveParams,YachooGetHistory

class DataService:

    def __init__(self, yahoo:YahooREST, finnhub:FinnhubProvider, ecb:ECBProvider):
        try:
            self.yahoo = yahoo
            self.finnhub = finnhub
            self.ecb = ecb
        except Exception as e:
            raise QuantTerminalException(e, sys)
    def data_parse_daily_exchange_rate(self, params: GetDailyExchangeRateParams)-> list[dict]:
        try:
            return parse_ecb(self.ecb.get_daily_avg_exchange_rate(params=params))
        except Exception as e:
            raise QuantTerminalException(e, sys)
    def data_parse_period_exchange_rate(self, params: GetPeriodExchangeRateParams)-> list[dict]:
        try:
            return parse_ecb(self.ecb.get_period_exchange_rate(params=params))
        except Exception as e:
            raise QuantTerminalException(e, sys)
    def data_parse_interest_rate(self, params: GetInterestRateParams)-> list[dict]:
        try:
            return parse_ecb(self.ecb.get_interest_rate(params=params))
        except Exception as e:
            raise QuantTerminalException(e, sys)
    def data_parse_yield_curve(self, params: GetYieldCurveParams)-> list[dict]:
        try:
            return parse_ecb(self.ecb.get_yield_curve(params=params))
        except Exception as e:
            raise QuantTerminalException(e, sys)
    def data_parse_history(self, params:YachooGetHistory):
        try:
            return self.yahoo.get_history(params=params).to_dict(orient="records")
        except Exception as e:
            raise QuantTerminalException(e, sys)