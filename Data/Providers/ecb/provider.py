import sys
from Core.exceptions.exceptions import QuantTerminalException
from Core.configs.constants import ECB_BASE_URL
from Core.models.request_models import GetDailyExchangeRateParams,GetPeriodExchangeRateParams,GetInterestRateParams,GetYieldCurveParams
from Data.Providers.Base.api_provider import BaseProvider

class ECBProvider(BaseProvider):

    def __init__(self):
        try:    
            super().__init__()
        except Exception as e:
            raise QuantTerminalException(e, sys)
        
    def get(self, dataset: str, series: str, params:dict)-> dict:
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

    def get_daily_avg_exchange_rate(
        self,params:GetDailyExchangeRateParams)->dict:
        try:
            return self.get("EXR",
                f"D.{params.currency}.{params.reference_currency}.SP00.A",
                    {
            "startPeriod": params.start_date,
            "endPeriod": params.end_date,
            "format": "jsondata"
        })   
        except Exception as e:
            raise QuantTerminalException(e, sys)
    def get_period_exchange_rate(self,params:GetPeriodExchangeRateParams)->dict:
        try:
            return self.get("EXR",
                f"{params.frequency.value}.{params.currency}.{params.reference_currency}.SP00.{params.variation.value}",
                    {
            "startPeriod": params.start_date,
            "endPeriod": params.end_date,
            "format": "jsondata"
        })   
        except Exception as e:
            raise QuantTerminalException(e, sys)
        
    def get_interest_rate(
        self,params:GetInterestRateParams)->dict:
        try:
            return self.get("FM",
                            f"{params.frequency.value}.U2.{params.currency}.4F.KR.{params.rate.value}.{params.measure.value}",
                            {
            "startPeriod": params.start_date,
            "endPeriod": params.end_date,
            "format": "jsondata"
        })
        except Exception as e:
            raise QuantTerminalException(e, sys)

    def get_yield_curve(
        self,params:GetYieldCurveParams)->dict:
        try:
            return self.get(
                "YC",
                f"B.U2.{params.currency}.4F.{params.instrument.value}.SV_C_YM.{params.maturity.value}",
            {
            "startPeriod": params.start_date,
            "endPeriod": params.end_date,
            "format": "jsondata"
        })
        except Exception as e:
            raise QuantTerminalException(e, sys)