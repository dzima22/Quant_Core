import json
import sys
from configs.constants import FINHUB_WEBSOCKET_FINAL_URL
import websockets
from Core.exceptions.exceptions import QuantTerminalException
from Data.Providers.Base.web_socket_provider import Websocket


class FinnhubWebSocket(Websocket):

    def __init__(self):
        try:
            self.websocket = None
        except Exception as e:
            raise QuantTerminalException(e,sys)
        
    async def connect(self):
        try:
            self.websocket = await websockets.connect(FINHUB_WEBSOCKET_FINAL_URL)
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