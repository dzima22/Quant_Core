import os,sys
import requests
from dotenv import load_dotenv
from configs.constants import finhub_base_url
from Data.Providers.Base.provider import BaseProvider
from Core.exceptions.exceptions import QuantTerminalException
load_dotenv()

class FinnhubProvider(BaseProvider):

    def __init__(self):
        try:
            self.base_url = finhub_base_url
            self.api_key = os.getenv("FINNHUB_API_KEY")
            self.session = requests.Session()
        except Exception as e:
            raise QuantTerminalException(e,sys)
        
    def _get(self, endpoint: str, params=None):
        try:
            if params is None:
                params = {}

            params["token"] = self.api_key

            response = self.session.get(
                f"{self.base_url}/{endpoint}",
                params=params,
                timeout=10)

            response.raise_for_status()
            return response.json()
        except Exception as e:
            raise QuantTerminalException(e,sys)
        
    def get_quote(self, symbol: str):
        try:
            return self._get(
                "quote",
                {
                    "symbol": symbol,
                }
            )
        except Exception as e:
            raise QuantTerminalException(e,sys)
        
    def search(self, query: str):
        try:
            return self._get(
                "search",
                {
                    "q": query,
                }
            )
        except Exception as e:
            raise QuantTerminalException(e,sys)
        
    def get_company(self, symbol: str):
        try:
            return self._get(
                "stock/profile2",
                {
                    "symbol": symbol,
                }
            )
        except Exception as e:
            raise QuantTerminalException(e,sys)
        
    def get_company_news(
        self,
        symbol: str,
        start_date: str,
        end_date: str):
        try:
            return self._get(
                "company-news",
                {
                    "symbol": symbol,
                    "from": start_date,
                    "to": end_date,
                }
            )
        except Exception as e:
            raise QuantTerminalException(e,sys)