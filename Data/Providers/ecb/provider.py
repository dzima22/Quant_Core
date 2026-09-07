import requests,sys

from Core.exceptions.exceptions import QuantTerminalException
from configs.constants import maturities,rates
from configs.constants import ECB_BASE_URL
from configs.models import GetExchangeRateParams,GetInterestRateParams,GetYieldCurveParams

class ECBProvider:

    def __init__(self):
        try:    
            super().__init__()
        except Exception as e:
            raise QuantTerminalException(e, sys)
        
    def _get(self, dataset: str, series: str, params:dict)-> dict:
        try:
            response = self.session.get(
                f"{ECB_BASE_URL}/{dataset}/{series}",
                params=params,
                timeout=10,
            )
            response.raise_for_status()
            return response.json()

        except Exception as e:
            raise QuantTerminalException(e, sys)

    def get_exchange_rate(
        self,params:GetExchangeRateParams):
        try:
            return self._get("EXR",
                f"{params.frequency}.{params.currency}.{params.reference_currency}.{params.spot_rate}.{params.variation}",
                    {
            "startPeriod": params.start_date,
            "endPeriod": params.end_date
        })   
        except Exception as e:
            raise QuantTerminalException(e, sys)
    def get_interest_rate(
        self,params:GetInterestRateParams):
        try:
            return self._get("FM",
                            f"{params.frequency}.{params.area}.{params.currency}.4F.KR.{params.rate}.{params.measure}",
                            {
            "startPeriod": params.start_date,
            "endPeriod": params.end_date
        })
        except Exception as e:
            raise QuantTerminalException(e, sys)

    def get_yield_curve(
        self,params:GetYieldCurveParams):
        try:
            return self._get(
                "YC",
                f"B.{params.area}.{params.currency}.4F.G_N_A.{params.measure}.{params.maturity}",
            {
            "startPeriod": params.start_date,
            "endPeriod": params.end_date
        })
        except Exception as e:
            raise QuantTerminalException(e, sys)