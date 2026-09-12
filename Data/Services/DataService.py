from Data.Providers.yachoo.provider import YahooREST
from Data.Providers.ecb.provider import ECBProvider
from Data.Providers.Finnhub.provider import FinnhubProvider

class DataService:

    def __init__(self, yahoo:YahooREST, finnhub:FinnhubProvider, ecb:ECBProvider):
        self.yahoo = yahoo
        self.finnhub = finnhub
        self.ecb = ecb