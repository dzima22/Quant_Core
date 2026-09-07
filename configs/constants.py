import os 
FINHUB_BASE_URL= "https://finnhub.io/api/v1"
FINHUB_WEBSOCKET_URL="wss://ws.finnhub.io"
FINHUB_WEBSOCKET_FINAL_URL=f"{FINHUB_WEBSOCKET_URL}?token={os.getenv('FINNHUB_API_KEY')}"
ECB_BASE_URL="https://data-api.ecb.europa.eu/service/data"
