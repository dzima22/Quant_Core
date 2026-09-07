from abc import ABC, abstractmethod


class Websocket(ABC):

    @abstractmethod
    async def connect(self):
        pass
    @abstractmethod
    async def subscribe(self, symbol):
        pass
    @abstractmethod 
    async def receive(self):
        pass
    @abstractmethod 
    async def disconnect(self):
        pass