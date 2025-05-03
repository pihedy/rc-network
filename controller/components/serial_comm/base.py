from abc import ABC, abstractmethod

class SerialCommunication(ABC):

    @abstractmethod
    def write(self, data: str) -> None:
        pass

    @abstractmethod
    def read(self) -> str:
        pass
