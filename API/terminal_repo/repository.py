from Core.exceptions.exceptions import QuantTerminalException
import sys
from Core.models.request_models import (
    GetInterestRateParams,
    YachooSymbol,
    GetDailyExchangeRateParams,
    GetUSASpeandingPlusLobbingParams,
    GetPeriodExchangeRateParams,
    YachooGetHistory,
    GetYieldCurveParams,
)
from Data.Services.DataService import DataService


class Repository:
    def __init__(self, data_service: DataService):
        try:
            self.data_service = data_service
        except Exception as e:
            raise QuantTerminalException(e, sys)

    def get_exchange_rate_data(self, params: GetPeriodExchangeRateParams) -> list[dict]:
        try:
            parsed_data = self.data_service.data_parse_period_exchange_rate(
                params=params
            )
            return parsed_data
        except Exception as e:
            raise QuantTerminalException(e, sys)

    def get_daily_exchange_rate_data(
        self, params: GetDailyExchangeRateParams
    ) -> list[dict]:
        try:
            parsed_data = self.data_service.data_parse_daily_exchange_rate(
                params=params
            )
            return parsed_data
        except Exception as e:
            raise QuantTerminalException(e, sys)

    def get_balance_sheet_data(self, symbol: YachooSymbol) -> list[dict]:
        try:
            parsed_data = self.data_service.data_parse_balance_sheet(symbol=symbol)
            return parsed_data
        except Exception as e:
            raise QuantTerminalException(e, sys)

    def get_interest_rate_data(self, params: GetInterestRateParams) -> list[dict]:
        try:
            parsed_data = self.data_service.data_parse_interest_rate(params=params)
            return parsed_data
        except Exception as e:
            raise QuantTerminalException(e, sys)

    def get_lobbying_data(self, params: GetUSASpeandingPlusLobbingParams) -> list[dict]:
        try:
            parsed_data = self.data_service.data_parse_lobbing(params=params)
            return parsed_data
        except Exception as e:
            raise QuantTerminalException(e, sys)

    def get_usa_spending(self, params: GetUSASpeandingPlusLobbingParams) -> list[dict]:
        try:
            parsed_data = self.data_service.data_parse_spending(params=params)
            return parsed_data
        except Exception as e:
            raise QuantTerminalException(e, sys)

    def get_history_data(self, params: YachooGetHistory) -> list[dict]:
        try:
            parsed_data = self.data_service.data_parse_history(params=params)
            return parsed_data
        except Exception as e:
            raise QuantTerminalException(e, sys)

    def get_yield_curve_data(self, params: GetYieldCurveParams) -> list[dict]:
        try:
            parsed_data = self.data_service.data_parse_yield_curve(params=params)
            return parsed_data
        except Exception as e:
            raise QuantTerminalException(e, sys)

    def get_cashflow_data(self, symbol: YachooSymbol) -> list[dict]:
        try:
            parsed_data = self.data_service.data_parse_cashflow(symbol=symbol)
            return parsed_data
        except Exception as e:
            raise QuantTerminalException(e, sys)

    def get_dividents_data(self, symbol: YachooSymbol) -> list[dict]:
        try:
            parsed_data = self.data_service.data_parse_dividents(symbol=symbol)
            return parsed_data
        except Exception as e:
            raise QuantTerminalException(e, sys)

    def get_financials(self, symbol: YachooSymbol) -> list[dict]:
        try:
            parsed_data = self.data_service.data_parse_financials_yachoo(symbol=symbol)
            parsed_quarterly_data = self.data_service.data_parse_quarterly_financials(
                symbol=symbol
            )
            final = parsed_data + parsed_quarterly_data
            return final
        except Exception as e:
            raise QuantTerminalException(e, sys)
