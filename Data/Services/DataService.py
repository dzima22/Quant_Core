from Data.Providers.yachoo.provider import YahooREST
from Data.Providers.ecb.provider import ECBProvider
from Data.Providers.Finnhub.provider import FinnhubProvider
from Core.exceptions.exceptions import QuantTerminalException
import sys
from Core.utils.utils import parse_ecb,parse_usaspending,parse_lobbying,parse_basic_financials,data_parse_dataframes,data_parse_series,data_parse_history
from Core.configs.models import GetDailyExchangeRateParams,GetPeriodExchangeRateParams,GetInterestRateParams,GetYieldCurveParams,YachooGetHistory,YachooSymbol,GetUSASpeandingPlusLobbingParams,GetBasicFinancialsParams

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
    def data_parse_history(self, params:YachooGetHistory)-> list[dict]:
        try:
            return data_parse_history(df=self.yahoo.get_history(params=params))
        except Exception as e:
            raise QuantTerminalException(e, sys)
    def data_parse_cashflow(self, symbol:YachooSymbol)-> list[dict]:
        try:
            return data_parse_dataframes(df=self.yahoo.get_cashflow(symbol=symbol))
        except Exception as e:
            raise QuantTerminalException(e, sys)
    def data_parse_balance_sheet(self, symbol:YachooSymbol)-> list[dict]:
        try:
            return data_parse_dataframes(df=self.yahoo.get_balance_sheet(symbol=symbol))
        except Exception as e:
            raise QuantTerminalException(e, sys)
    def data_parse_financials_yachoo(self, symbol:YachooSymbol)-> list[dict]:
        try:
            return data_parse_dataframes(df=self.yahoo.get_financials(symbol=symbol))
        except Exception as e:
            raise QuantTerminalException(e, sys)
    def data_parse_quarterly_financials(self, symbol:YachooSymbol)-> list[dict]:
        try:
            return data_parse_dataframes(df=self.yahoo.get_quarterly_financials(symbol=symbol))
        except Exception as e:
            raise QuantTerminalException(e, sys)
    def data_parse_dividents(self, symbol:YachooSymbol)-> list[dict]:
        try:
            return data_parse_series(series=self.yahoo.get_dividends(symbol=symbol))
        except Exception as e:
            raise QuantTerminalException(e, sys)
    def data_parse_splits(self, symbol:YachooSymbol)-> list[dict]:
        try:
            return data_parse_series(series=self.yahoo.get_splits(symbol=symbol))
        except Exception as e:
            raise QuantTerminalException(e, sys)
    def data_parse_spending(self, params:GetUSASpeandingPlusLobbingParams)->dict:
        try:
            return parse_usaspending(self.finnhub.get_usa_spending(params=params))
        except Exception as e:
            raise QuantTerminalException(e, sys)
    def data_parse_lobbing(self, params:GetUSASpeandingPlusLobbingParams) -> dict:
        try:
            return parse_lobbying(self.finnhub.get_senate_lobbying(params=params))
        except Exception as e:
            raise QuantTerminalException(e, sys)
    def data_parse_financials(self,params:GetBasicFinancialsParams) -> dict:
        try:
            return parse_basic_financials(self.finnhub.get_basic_financials(params=params))
        except Exception as e:
            raise QuantTerminalException(e, sys)


    