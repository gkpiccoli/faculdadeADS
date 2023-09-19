from srcs.conta import Conta
from srcs.cliente import Cliente

conta = Conta("001", "Gustavo", 50000.0, 100000.0)

print(type(conta))
print("Dados da conta:")
print("O número da conta é: {}".format(conta.numero))
print(conta.numero)
print(conta.titular)
print(conta.saldo)
print(conta.limite)

print("Depositando...")
conta.depositar(100)
print("O novo saldo é: {}".format(conta.saldo))

cliente1 = Cliente("Gustavo", "123.456.789-10", "123456")
conta1 = Conta("001", cliente1, 50000.0, 100000.0)

print(cliente1.nome)
print(cliente1.cpf)
print(cliente1.senha)

print("Efetuando saque...")
if conta.sacar(111100):
    print("Saque efetuado com sucesso!")
else:
    print("Saldo insuficiente!")
