from Core.exceptions.exceptions import QuantTerminalException
import sys
from Core.models.request_models import GetInterestRateParams,YachooSymbol,GetDailyExchangeRateParams,GetUSASpeandingPlusLobbingParams
from Data.Services.DataService import DataService



class Repository:
    def __init__(self,data_service:DataService):
        try:
            self.data_service=data_service
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