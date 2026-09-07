from abc import ABC, abstractmethod
import requests,sys
from Core.exceptions.exceptions import QuantTerminalException

class BaseProvider(ABC):
    def __init__(self):
        try:
            self.session = requests.Session()
        except Exception as e:
            raise QuantTerminalException(e,sys)

    @abstractmethod
    def get(self):
        pass