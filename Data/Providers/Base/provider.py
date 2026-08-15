from abc import ABC, abstractmethod


class BaseProvider(ABC):

    @abstractmethod
    def get_quote(self, symbol):
        pass

    @abstractmethod
    def get_history(self, symbol, period="1y"):
        pass

    @abstractmethod
    def search(self, query):
        pass