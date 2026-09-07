import yfinance as yf
import sys
from Data.Providers.Base.api_provider import LibraryProvider
from Core.exceptions.exceptions import QuantTerminalException
### TO BE UPDATED 
class YahooREST(LibraryProvider):
### TO BE UPDATED 
    def get_quote(self, symbol: str):
        try:
            ticker = yf.Ticker(symbol)
            return ticker.fast_info
        except Exception as e:
            raise QuantTerminalException(e,sys)
            
    def get_history(
        self,
        symbol: str,
        period: str = "1y",
        interval: str = "1d"):
        try:
            ticker = yf.Ticker(symbol)
            return ticker.history(
            period=period,
            interval=interval)
        except Exception as e:
            raise QuantTerminalException(e,sys)

    def get_company(self, symbol: str):
        try:
            ticker = yf.Ticker(symbol)
            return ticker.info
        except Exception as e:
            raise QuantTerminalException(e,sys)


    def get_financials(self, symbol: str):
        try:
            ticker = yf.Ticker(symbol)
            return ticker.financials
        except Exception as e:
            raise QuantTerminalException(e,sys)


    def get_balance_sheet(self, symbol: str):
        try:
            ticker = yf.Ticker(symbol)
            return ticker.balance_sheet
        except Exception as e:
            raise QuantTerminalException(e,sys)


    def get_cashflow(self, symbol: str):
        try:
            ticker = yf.Ticker(symbol)
            return ticker.cashflow
        except Exception as e:
            raise QuantTerminalException(e,sys)

    def get_dividends(self, symbol: str):
        try:
            ticker = yf.Ticker(symbol)
            return ticker.dividends
        except Exception as e:
            raise QuantTerminalException(e,sys)

    def get_splits(self, symbol: str):
        try:
            ticker = yf.Ticker(symbol)
            return ticker.splits
        except Exception as e:
            raise QuantTerminalException(e,sys)
