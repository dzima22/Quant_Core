from  Data.Providers.ecb.provider import ECBProvider
from  Data.Providers.Finnhub.provider import FinnhubProvider 
from  Data.Providers.yachoo.provider import YahooREST
from configs.models import GetUSASpeandingPlusLobbingParams, GetBasicFinancialsParams,YachooSymbol,YachooGetHistory,GetUSASpeandingPlusLobbingParams
from dotenv import load_dotenv
from Data.Services.DataService import DataService
load_dotenv()

# a=GetDailyExchangeRateParams(currency="USD",startPeriod="2025-01-01",endPeriod="2025-01-09",)
# d=DataService(yahoo=YahooREST,finnhub=FinnhubProvider,ecb=ECBProvider)
# result=d.data_parse_daily_exchange_rate(params=a)
# print(result)

# a=GetPeriodExchangeRateParams(currency="USD",startPeriod="2025-01",endPeriod="2025-05",reference_currency="EUR",frequency="M")
# d=DataService(yahoo=YahooREST,finnhub=FinnhubProvider,ecb=ECBProvider)
# result=d.data_parse_period_exchange_rate(params=a)
# print(result)

# a=GetInterestRateParams(currency="EUR",startPeriod="2025-01-01",endPeriod="2025-01-09",)
# d=DataService(yahoo=YahooREST,finnhub=FinnhubProvider,ecb=ECBProvider)
# result=d.data_parse_interest_rate(params=a)
# print(result)

# a=GetYieldCurveParams(currency="EUR",startPeriod="2025-01-01",endPeriod="2025-02-09",)
# d=DataService(yahoo=YahooREST,finnhub=FinnhubProvider,ecb=ECBProvider)
# result=d.data_parse_yield_curve(params=a)
# print(result)

# a=GetUSASpeandingPlusLobbingParams(symbol="AAPL",from_="2025-01-01",to="2026-07-01")
# d=DataService(yahoo=YahooREST,finnhub=FinnhubProvider,ecb=ECBProvider)
# result=d.data_parse_spending(params=a)
# print(result)

# a=GetBasicFinancialsParams(symbol="AAPL")
# d=DataService(yahoo=YahooREST,finnhub=FinnhubProvider,ecb=ECBProvider)
# result=d.data_parse_financials(params=a)
# print(result)
