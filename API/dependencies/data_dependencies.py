from Data.Services.DataService import DataService
from Data.Providers.yachoo.provider import YahooREST
from Data.Providers.ecb.provider import ECBProvider
from Data.Providers.Finnhub.provider import FinnhubProvider

def get_data_service() -> DataService:
    return DataService(
        yahoo=YahooREST(),
        finnhub=FinnhubProvider(),
        ecb=ECBProvider(),
    )