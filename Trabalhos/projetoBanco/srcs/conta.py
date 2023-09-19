class Conta:
    def __init__(self, numero, cliente, saldo=0.0, limite=0.0):
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False

    def mostra_extrato(self):
        return f"O  número da conta é {self.numero} saldo do titular {self.titular} é {self.saldo:.2f} e "
