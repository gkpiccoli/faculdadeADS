# Importa módulos necessários
import math
from srcs.formaGeometrica import FormaGeometrica


# [CLASSES e HERANÇA]
# Classe concreta Retângulo que herda de FormaGeometrica
class Retangulo(FormaGeometrica):
    # [ATRIBUTOS]
    # Inicializa e chama construtor da superclasse
    def __init__(self, cor, lado1, lado2):
        super().__init__(cor)
        self.__lado1 = lado1
        self.__lado2 = lado2

    # [POLIMORFISMO]
    # Implementa cálculo de área
    def calcularArea(self):
        return self.__lado1 * self.__lado2

    # Implementa cálculo de perímetro
    def calcularPerimetro(self):
        return 2 * (self.__lado1 + self.__lado2)

    # Implementa exibição de dados
    def exibirDados(self):
        return f"O retângulo de cor {self.cor} com medidas {self.__lado1} e {self.__lado2} tem área = {self.calcularArea()} e tem perímetro = {self.calcularPerimetro()}."


# Classe concreta Circunferência que herda de FormaGeometrica
class Circunferencia(FormaGeometrica):
    # [ATRIBUTOS]
    # Inicializa e chama construtor da superclasse
    def __init__(self, cor, raio):
        super().__init__(cor)
        self.__raio = raio

    # [POLIMORFISMO]
    # Implementa cálculo de área
    def calcularArea(self):
        return math.pi * math.pow(self.__raio, 2)

    # Implementa cálculo de perímetro
    def calcularPerimetro(self):
        return 2 * math.pi * self.__raio

    # Implementa exibição de dados
    def exibirDados(self):
        return f"A circunferência de cor {self.cor} com raio {self.__raio} tem área = {self.calcularArea():.2f} e tem perímetro = {self.calcularPerimetro():.2f}."


# Classe concreta Triângulo que herda de FormaGeometrica
class Triangulo(FormaGeometrica):
    # [ATRIBUTOS]
    # Inicializa e chama construtor da superclasse
    def __init__(self, cor, lado1, lado2, lado3):
        super().__init__(cor)
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__lado3 = lado3

    # [POLIMORFISMO]
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
        return f"O triângulo de cor {self.cor} com medidas {self.__lado1}, {self.__lado2}, e {self.__lado3} tem área = {self.calcularArea():.2f} e tem perímetro = {self.calcularPerimetro():.2f}."


# Parte principal do programa
if __name__ == "__main__":
    # Cria algumas formas geométricas
    print("Lista de Formas Geométricas:")
    lista_formas = [
        Retangulo("azul", 10, 20),
        Retangulo("vermelha", 3, 4),
        Circunferencia("laranja", 2),
    ]

    # Exibe os dados de cada formaa
    for forma in lista_formas:
        print(forma.exibirDados())
