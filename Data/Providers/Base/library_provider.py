from abc import ABC, abstractmethod

class LibraryProvider(ABC):

    @abstractmethod
    def get(self):
        pass