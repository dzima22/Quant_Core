import requests,sys

from Core.exceptions.exceptions import QuantTerminalException
from configs.constants import maturities,rates

class ECBProvider:

    def __init__(self):
        try:    
            self.base_url = "https://data-api.ecb.europa.eu/service/data"
            self.session = requests.Session()
        except Exception as e:
            raise QuantTerminalException(e, sys)
        
    def _get(self, dataset: str, series: str, params=None):

        if params is None:
            params = {}

        try:
            response = self.session.get(
                f"{self.base_url}/{dataset}/{series}",
                params=params,
                timeout=10,
            )

            response.raise_for_status()

            return response.json()

        except Exception as e:
            raise QuantTerminalException(e, sys)

    def get_exchange_rate(
        self,
        currency: str,
        start_date: str = None,
        end_date: str = None):
        try:
            params = {}

            if start_date:
                params["startPeriod"] = start_date

            if end_date:
                params["endPeriod"] = end_date

            return self._get(
                "EXR",
                f"D.{currency}.EUR.SP00.A",
                params)   
        except Exception as e:
            raise QuantTerminalException(e, sys)
    def get_interest_rate(
        self,
        rate_type: str = "deposit",
        start_date: str = None,
        end_date: str = None,
    ):
        try:
            if rate_type not in rates:
                raise ValueError(
                    f"Unknown interest rate: {rate_type}"
                )

            params = {}

            if start_date:
                params["startPeriod"] = start_date

            if end_date:
                params["endPeriod"] = end_date

            return self._get(
                "FM",
                rates[rate_type],
                params)
        except Exception as e:
            raise QuantTerminalException(e, sys)

    def get_yield_curve(
        self,
        maturity: str,
        start_date: str = None,
        end_date: str = None,
    ):
        try:
            maturity = maturity.upper()

            if maturity not in maturities:
                raise ValueError(
                    f"Unsupported maturity: {maturity}")

            params = {}

            if start_date:
                params["startPeriod"] = start_date

            if end_date:
                params["endPeriod"] = end_date

            return self._get(
                "YC",
                f"B.U2.EUR.4F.G_N_A.SV_C_YM.{maturities[maturity]}",
                params)
        except Exception as e:
            raise QuantTerminalException(e, sys)