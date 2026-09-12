from  Data.Providers.ecb.provider import ECBProvider
from  Data.Providers.Finnhub.provider import FinnhubProvider 
from configs.models import GetUSASpeandingPlusLobbingParams, GetBasicFinancialsParams
from dotenv import load_dotenv

load_dotenv()


f=FinnhubProvider()
params = GetUSASpeandingPlusLobbingParams(symbol="AAPL",from_="2025-01-01",to="2025-09-12")

print(f.get_usa_spending(params))