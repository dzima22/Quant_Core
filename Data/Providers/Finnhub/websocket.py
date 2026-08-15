import json
import os,sys
from configs.constants import finhub_websocket_url
import websockets
from dotenv import load_dotenv
from Core.exceptions.exceptions import QuantTerminalException
load_dotenv()


class FinnhubWebSocket:

    def __init__(self):
        try:
            self.url = os.path.join(finhub_websocket_url,f"{os.getenv('FINNHUB_API_KEY')}")
            self.websocket = None
        except Exception as e:
            raise QuantTerminalException(e,sys)
        
    async def connect(self):
        try:
            self.websocket = await websockets.connect(self.url)
        except Exception as e:
            raise QuantTerminalException(e,sys)
        
    async def subscribe(self, symbol):
        try:
            await self.websocket.send(
                json.dumps(
                    {
                        "type": "subscribe",
                        "symbol": symbol,
                    }
                )
            )
        except Exception as e:
            raise QuantTerminalException(e,sys)

    async def receive(self):
        try:
            return await self.websocket.recv()
        except Exception as e:
            raise QuantTerminalException(e,sys)
        
    async def disconnect(self):
        try:
            await self.websocket.close()
        except Exception as e:
            raise QuantTerminalException(e,sys)