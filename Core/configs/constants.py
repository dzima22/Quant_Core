import os

FINHUB_BASE_URL = "https://finnhub.io/api/v1"
FINHUB_WEBSOCKET_URL = "wss://ws.finnhub.io"
FINHUB_WEBSOCKET_FINAL_URL = (
    f"{FINHUB_WEBSOCKET_URL}?token={os.getenv('FINNHUB_API_KEY')}"
)
ECB_BASE_URL = "https://data-api.ecb.europa.eu/service/data"
METRICS_FOR_GRAPH = {
    "Total Revenue": "Revenue",
    "Gross Profit": "Gross Profit",
    "Operating Income": "Operating Income",
    "EBITDA": "EBITDA",
    "Net Income": "Net Income",
    "Diluted EPS": "Diluted EPS",
}
CANDLE_WIDTHS = {
    "1d": 0.6,
    "5d": 0.6,
    "1mo": 20,
    "3mo": 20,
    "6mo": 30,
    "1y": 30,
    "2y": 50,
    "5y": 50,
    "10y": 60,
}
