from srcs.formaGeometrica import FormaGeometrica


class Retangulo(FormaGeometrica):
    def __init__(self, cor, lado1, lado2):
        super().__init__(cor)
        self.__lado1 = lado1
        self.__lado2 = lado2

    @property
    def lado1(self):
        return self.__lado1

    @property
    def lado2(self):
        return self.__lado2

    def calcularArea(self):
        return self.__lado1 * self.__lado2

    def calcularPerimetro(self):
        return 2 * (self.__lado1 + self.__lado2)

    def exibirDados(self):
        return (
            f"O retangulo de cor {self.cor} com medidas {self.__lado1} e {self.__lado2} "
            f"tem área = {self.calcularArea()} e tem perímetro = {self.calcularPerimetro()}."
        )

# PARTE 1 OK
# retangulo1 = Retangulo("azul", 10, 20)
# print("Área = ", retangulo1.calcularArea())
# print("Perímetro = ", retangulo1.calcularPerimetro())
# retangulo2 = Retangulo("vermelha", 3, 4)
# print(retangulo2.exibirDados())

retangulo1 = Retangulo("azul", 10, 20)
print(
    f"O retângulo de lados {retangulo1.lado1} e {retangulo1.lado2} tem a cor {retangulo1.cor}."
)
print(
    "Sua área é",
    retangulo1.calcularArea(),
    "e seu perímetro é",
    retangulo1.calcularPerimetro(),
    ".",
)
retangulo2 = Retangulo("vermelha", 3, 4)
print(retangulo2.exibirDados())
