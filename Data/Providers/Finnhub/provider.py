import os,sys
import requests
from configs.constants import FINHUB_BASE_URL
from configs.models import GetBasicFinancialsParams
from Data.Providers.Base.api_provider import BaseProvider
from Core.exceptions.exceptions import QuantTerminalException

class FinnhubProvider(BaseProvider):

    def __init__(self):
        try:
            super().__init__()
            self.session.params["token"] = os.getenv("FINNHUB_API_KEY")
        except Exception as e:
            raise QuantTerminalException(e,sys)
        
    def _get(self, endpoint: str, params: dict)-> dict:
        try:
            response = self.session.get(
                f"{FINHUB_BASE_URL}/{endpoint}",
                params=params,
                timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            raise QuantTerminalException(e,sys)
    def get_basic_financials(
        self,
        params: GetBasicFinancialsParams) -> dict:
        try:
            return self._get(
                "stock/metric",
                params.model_dump()
            )
        except Exception as e:
            raise QuantTerminalException(e, sys)

