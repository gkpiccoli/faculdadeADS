# Importando a classe ABC (Abstract Base Classes) e o decorador abstractmethod
from abc import ABC, abstractmethod


# [CLASSES]
# Definição da classe abstrata FormaGeometrica
class FormaGeometrica(ABC):
    # [ATRIBUTOS]
    # Construtor da classe, inicializa com uma cor
    def __init__(self, cor):
        self.__cor = cor  # Atributo privado para armazenar a cor

    # [ENCAPSULAMENTO]
    # Propriedade para acessar o valor da cor
    @property
    def cor(self):
        return self.__cor

    # Método para alterar a cor da forma
    def alterarCor(self, cor):
        self.__cor = cor

    # [POLIMORFISMO]
    # Métodos abstratos que deverão ser implementados pelas classes filhas
    @abstractmethod
    def calcularArea(self):
        pass

    @abstractmethod
    def calcularPerimetro(self):
        pass

    @abstractmethod
    def exibirDados(self):
        pass
