from abc import ABC, abstractmethod

class HelloRepository(ABC):

    @abstractmethod
    def get_hello_message(self) -> str:
        pass