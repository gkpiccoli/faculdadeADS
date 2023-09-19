from abc import ABC, abstractmethod
import math


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


class Retangulo(FormaGeometrica):
    def __init__(self, cor, lado1, lado2):
        super().__init__(cor)
        self.__lado1 = lado1
        self.__lado2 = lado2

    def calcularArea(self):
        return self.__lado1 * self.__lado2

    def calcularPerimetro(self):
        return 2 * (self.__lado1 + self.__lado2)

    def exibirDados(self):
        return (
            f"O retangulo de cor {self.cor} com medidas {self.__lado1} e {self.__lado2} "
            f"tem área = {self.calcularArea()} e tem perímetro = {self.calcularPerimetro()}."
        )


class Circunferencia(FormaGeometrica):
    def __init__(self, cor, raio):
        super().__init__(cor)
        self.__raio = raio

    def calcularArea(self):
        return math.pi * math.pow(self.__raio, 2)

    def calcularPerimetro(self):
        return 2 * math.pi * self.__raio

    def exibirDados(self):
        return (
            f"A circunferência de cor {self.cor} com raio {self.__raio} "
            f"tem área = {self.calcularArea():.2f} e tem perímetro = {self.calcularPerimetro():.2f}."
        )


class Triangulo(FormaGeometrica):
    def __init__(self, cor, lado1, lado2, lado3):
        super().__init__(cor)
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__lado3 = lado3

    def calcularArea(self):
        s = (self.__lado1 + self.__lado2 + self.__lado3) / 2
        return math.sqrt(
            s * (s - self.__lado1) * (s - self.__lado2) * (s - self.__lado3)
        )

    def calcularPerimetro(self):
        return self.__lado1 + self.__lado2 + self.__lado3

    def exibirDados(self):
        return (
            f"O triângulo de cor {self.cor} com medidas {self.__lado1}, {self.__lado2}, e {self.__lado3} "
            f"tem área = {self.calcularArea():.2f} e tem perímetro = {self.calcularPerimetro():.2f}."
        )


if __name__ == "__main__":
    print("Lista de formas geométricas:")
    lista_formas = []
    lista_formas.append(Retangulo("azul", 10, 20))
    lista_formas.append(Circunferencia("laranja", 2))
    lista_formas.append(Triangulo("verde", 3, 4, 5))

    for forma in lista_formas:
        print(forma.exibirDados())
