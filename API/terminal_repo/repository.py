from Core.exceptions.exceptions import QuantTerminalException
import sys
from Core.configs.models import GetInterestRateParams,GetYieldCurveParams,YachooGetHistory,YachooSymbol,GetDailyExchangeRateParams,GetUSASpeandingPlusLobbingParams
from Data.Services.TerminalServices import TerminalServices
from Data.Services.DataService import DataService
from matplotlib.figure import Figure
from API.dependencies.data_dependencies import get_data_service


class Repository:
    def __init__(self):
        try:
            self.terminal_service=TerminalServices()
            self.data_service=get_data_service()

        except Exception as e:
            raise QuantTerminalException(e, sys)
    def yield_curve(self,request_info:GetYieldCurveParams)-> Figure:
        try:
            parsed_data=self.data_service.data_parse_yield_curve(params=request_info)
            chart=self.terminal_service.yield_curve_chart_generation(data=parsed_data,request_info=request_info)
            return chart
        except Exception as e:
            raise QuantTerminalException(e, sys)
    def interest_rate(self,request_info:GetInterestRateParams)-> Figure:
        try:
            parsed_data=self.data_service.data_parse_interest_rate(params=request_info)
            chart=self.terminal_service.interest_rate_chart_generation(data=parsed_data,request_info=request_info)
            return chart
        except Exception as e:
            raise QuantTerminalException(e, sys)
    def candles(self,request_info:YachooGetHistory)-> Figure:
        try:
            parsed_data=self.data_service.data_parse_history(params=request_info)
            chart=self.terminal_service.candles_chart_generation(data=parsed_data,request_info=request_info)
            return chart
        except Exception as e:
            raise QuantTerminalException(e, sys)
    def main_financials(self,request_info:YachooSymbol)-> Figure:
        try:
            parsed_data=self.data_service.data_parse_financials_yachoo(symbol=request_info)
            chart=self.terminal_service.financials_chart_generation(data=parsed_data,request_info=request_info)
            return chart
        except Exception as e:
            raise QuantTerminalException(e, sys)
    def get_daily_exchange_rate_data(self,params: GetDailyExchangeRateParams)-> list[dict]:
        try:
            parsed_data=self.data_service.data_parse_daily_exchange_rate(params=params)
            return parsed_data
        except Exception as e:
            raise QuantTerminalException(e, sys)
    def get_balance_sheet_data(self,symbol: YachooSymbol)-> list[dict]:
        try:
            parsed_data=self.data_service.data_parse_balance_sheet(symbol=symbol)
            return parsed_data
        except Exception as e:
            raise QuantTerminalException(e, sys)
    def get_interest_rate_data(self,params:GetInterestRateParams)-> list[dict]:
        try:
            parsed_data=self.data_service.data_parse_interest_rate(params=params)
            return parsed_data
        except Exception as e:
            raise QuantTerminalException(e, sys)
    def get_lobbying_data(self,params: GetUSASpeandingPlusLobbingParams)-> list[dict]:
        try:
            parsed_data=self.data_service.data_parse_lobbing(params=params)
            return parsed_data
        except Exception as e:
            raise QuantTerminalException(e, sys)
    def get_usa_spending(self,params: GetUSASpeandingPlusLobbingParams)-> list[dict]:
        try:
            parsed_data=self.data_service.data_parse_spending(params=params)
            return parsed_data
        except Exception as e:
            raise QuantTerminalException(e, sys)