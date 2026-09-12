import yfinance as yf
import sys
from Data.Providers.Base.api_provider import BaseProvider
from Core.exceptions.exceptions import QuantTerminalException
from configs.models import YachooSymbol,YachooGetHistory

class YahooREST(BaseProvider):

    def _get(self,symbol:YachooSymbol):
        try:
            ticker = yf.Ticker(symbol)
            return ticker
        except Exception as e:
            raise QuantTerminalException(e,sys)
        
    def get_quote(self,symbol:YachooSymbol):
        try:
            return dict(self._get(symbol).fast_info)
        except Exception as e:
            raise QuantTerminalException(e,sys)
            
    def get_history(
        self,params:YachooGetHistory):
        try:
            return self._get(params.symbol).history(
            period=params.period,
            interval=params.interval)
        except Exception as e:
            raise QuantTerminalException(e,sys)

    def get_company(self,symbol:YachooSymbol):
        try:
            return self._get(symbol).info
        except Exception as e:
            raise QuantTerminalException(e,sys)

    def get_financials(self,symbol:YachooSymbol):
        try:
            return self._get(symbol).financials
        except Exception as e:
            raise QuantTerminalException(e,sys)
    def get_financials(self,symbol:YachooSymbol):
        try:
            return self._get(symbol).financials
        except Exception as e:
            raise QuantTerminalException(e,sys)

    def get_balance_sheet(self, symbol:YachooSymbol):
        try:
            return self._get(symbol).balance_sheet
        except Exception as e:
            raise QuantTerminalException(e,sys)

    def get_cashflow(self, symbol:YachooSymbol):
        try:
            return self._get(symbol).cashflow
        except Exception as e:
            raise QuantTerminalException(e,sys)

    def get_dividends(self, symbol:YachooSymbol):
        try:
            return self._get(symbol).dividends
        except Exception as e:
            raise QuantTerminalException(e,sys)

    def get_splits(self, symbol:YachooSymbol):
        try:
            return self._get(symbol).splits
        except Exception as e:
            raise QuantTerminalException(e,sys)
