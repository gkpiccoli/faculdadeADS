from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    def __init__(self, cor):
        self.__cor = cor

    @property
    def cor(self):
        return self.__cor

    def alterarCor(self, cor):
        self.__cor = cor

    @abstractmethod
    def calcularArea(self):
        pass

    @abstractmethod
    def calcularPerimetro(self):
        pass

    @abstractmethod
    def exibirDados(self):
        pass
