from abc import ABC, abstractmethod


class FillingStation(ABC):
    @abstractmethod
    def check(self, fuel: str, city: str) -> str:
        pass
