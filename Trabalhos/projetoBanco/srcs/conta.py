class Conta:

    def __init__(self, numero, cliente, saldo=0.0, limite=0.0):
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite

        def depositar(self, valor):
            self.saldo += valor

        def sacar(self, valor):
            self.saldo -= valor

        def mostra_extrato(self):
            return f"O saldo do titular {self.titular} é {self.saldo}"
