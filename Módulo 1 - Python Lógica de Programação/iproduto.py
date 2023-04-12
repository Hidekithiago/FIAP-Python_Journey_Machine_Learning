from abc import ABC, abstractmethod

class IProduto(ABC):
    @abstractmethod
    def investir(self, valor):
        pass