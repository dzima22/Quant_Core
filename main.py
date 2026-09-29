from Core.models.request_models import GetUSASpeandingPlusLobbingParams, GetBasicFinancialsParams,YachooSymbol,YachooGetHistory,GetUSASpeandingPlusLobbingParams,GetYieldCurveParams,GetInterestRateParams
from dotenv import load_dotenv
from API.routers.graphs_endpoints import graph_router
from API.routers.raw_data_endpoints import raw_data_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
load_dotenv()


app = FastAPI()


@app.get("/healthy")
async def health_check():
    return {"status": "Healthy"}

app.include_router(graph_router)
app.include_router(raw_data_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

### CHECKS

# a=GetDailyExchangeRateParams(currency="USD",startPeriod="2025-01-01",endPeriod="2025-01-09",)
# d=DataService(yahoo=YahooREST,finnhub=FinnhubProvider,ecb=ECBProvider)
# result=d.data_parse_daily_exchange_rate(params=a)
# print(result)

# a=GetPeriodExchangeRateParams(currency="USD",startPeriod="2025-01",endPeriod="2025-05",reference_currency="EUR",frequency="M")
# d=DataService(yahoo=YahooREST,finnhub=FinnhubProvider,ecb=ECBProvider)
# result=d.data_parse_period_exchange_rate(params=a)
# print(result)

# a=GetInterestRateParams(currency="EUR",startPeriod="2025-01-01",endPeriod="2025-02-09",)
# d=DataService(yahoo=YahooREST(),finnhub=FinnhubProvider(),ecb=ECBProvider())
# result=d.data_parse_interest_rate(params=a)
# terminal_services=TerminalServices()
# graph=terminal_services.interest_rate_chart_generation(data=result,request_info=a)
# plt.show()


# a=GetYieldCurveParams(currency="EUR",startPeriod="2025-01-01",endPeriod="2025-02-09",)
# d=DataService(yahoo=YahooREST(),finnhub=FinnhubProvider(),ecb=ECBProvider())
# result=d.data_parse_yield_curve(params=a)
# terminal_services=TerminalServices()
# graph=terminal_services.yield_curve_chart_generation(data=result,request_info=a)
# plt.show()


# a=GetUSASpeandingPlusLobbingParams(symbol="AAPL",from_="2025-01-01",to="2026-07-01")
# d=DataService(yahoo=YahooREST,finnhub=FinnhubProvider,ecb=ECBProvider)
# result=d.data_parse_spending(params=a)
# print(result)

# a=GetBasicFinancialsParams(symbol="AAPL")
# d=DataService(yahoo=YahooREST(),finnhub=FinnhubProvider(),ecb=ECBProvider())
# result=d.data_parse_financials(params=a)
# print(result)

# a=GetUSASpeandingPlusLobbingParams(symbol="AAPL",from_="2025-02-09",to="2025-03-11")
# # d=DataService(yahoo=YahooREST(),finnhub=FinnhubProvider(),ecb=ECBProvider())
# # result=d.data_parse_spending(params=a)
# # print(result)
# r=Repository()
# result=r.get_lobbying_data(params=a)
# print(result)


# a=YachooGetHistory(symbol="AAPL",period="3mo",interval="1d")
# d=DataService(yahoo=YahooREST(),finnhub=FinnhubProvider(),ecb=ECBProvider())
# result=d.data_parse_history(params=a)
# terminal_services=TerminalServices()
# graph=terminal_services.candles_chart_generation(data=result,request_info=a)
# plt.show()

# a=YachooSymbol(symbol="AAPL")
# d=DataService(yahoo=YahooREST(),finnhub=FinnhubProvider(),ecb=ECBProvider())
# result=d.data_parse_financials_yachoo(symbol=a)
# terminal_services=TerminalServices()
# graph=terminal_services.financials_chart_generation(data=result,request_info=a)
# plt.show()
