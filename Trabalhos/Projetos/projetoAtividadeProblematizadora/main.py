# Importa módulos necessários
from abc import ABC, abstractmethod
import math


# Classe abstrata FormaGeometrica que serve de padrão para as subclasses
class FormaGeometrica(ABC):
    # Inicializa a cor
    def __init__(self, cor):
        self.__cor = cor

    # Propriedade para acessar a cor
    @property
    def cor(self):
        return self.__cor

    # Método para alterar a cor
    def alterarCor(self, cor):
        self.__cor = cor

    # Método abstrato para calcular área
    @abstractmethod
    def calcularArea(self):
        pass

    # Método abstrato para calcular perímetro
    @abstractmethod
    def calcularPerimetro(self):
        pass

    # Método abstrato para exibir dados
    @abstractmethod
    def exibirDados(self):
        pass


# Classe concreta Retângulo
class Retangulo(FormaGeometrica):
    # Inicializa e chama construtor da superclasse
    def __init__(self, cor, lado1, lado2):
        super().__init__(cor)
        self.__lado1 = lado1
        self.__lado2 = lado2

    # Implementa cálculo de área
    def calcularArea(self):
        return self.__lado1 * self.__lado2

    # Implementa cálculo de perímetro
    def calcularPerimetro(self):
        return 2 * (self.__lado1 + self.__lado2)

    # Implementa exibição de dados
    def exibirDados(self):
        return (
            f"O retângulo de cor {self.cor} com medidas {self.__lado1} e {self.__lado2} "
            f"tem área = {self.calcularArea()} e tem perímetro = {self.calcularPerimetro()}."
        )


# Classe concreta Circunferência
class Circunferencia(FormaGeometrica):
    # Inicializa e chama construtor da superclasse
    def __init__(self, cor, raio):
        super().__init__(cor)
        self.__raio = raio

    # Implementa cálculo de área
    def calcularArea(self):
        return math.pi * math.pow(self.__raio, 2)

    # Implementa cálculo de perímetro
    def calcularPerimetro(self):
        return 2 * math.pi * self.__raio

    # Implementa exibição de dados
    def exibirDados(self):
        return (
            f"A circunferência de cor {self.cor} com raio {self.__raio} "
            f"tem área = {self.calcularArea():.2f} e tem perímetro = {self.calcularPerimetro():.2f}."
        )


# Classe concreta Triângulo
class Triangulo(FormaGeometrica):
    # Inicializa e chama construtor da superclasse
    def __init__(self, cor, lado1, lado2, lado3):
        super().__init__(cor)
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__lado3 = lado3

    # Implementa cálculo da área
    def calcularArea(self):
        s = (self.__lado1 + self.__lado2 + self.__lado3) / 2
        return math.sqrt(
            s * (s - self.__lado1) * (s - self.__lado2) * (s - self.__lado3)
        )

    # Implementa cálculo do perímetro
    def calcularPerimetro(self):
        return self.__lado1 + self.__lado2 + self.__lado3

    # Implementa exibição de dados
    def exibirDados(self):
        return (
            f"O triângulo de cor {self.cor} com medidas {self.__lado1}, {self.__lado2}, e {self.__lado3} "
            f"tem área = {self.calcularArea():.2f} e tem perímetro = {self.calcularPerimetro():.2f}."
        )


# Parte principal do programa
if __name__ == "__main__":
    # Cria algumas formas geométricas
    print("Lista de Formas Geométricas:")
    lista_formas = []
    lista_formas.append(Retangulo("azul", 10, 20))
    lista_formas.append(Retangulo("vermelha", 3, 4))
    lista_formas.append(Circunferencia("laranja", 2))

    # Exibe os dados de cada forma
    for forma in lista_formas:
        print(forma.exibirDados())
