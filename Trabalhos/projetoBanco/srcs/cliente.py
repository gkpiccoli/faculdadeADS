class Cliente:
    def __init__(self, nome, cpf, senha):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha

    def __str__(self):
        return f"Nome: {self.nome}\nCPF: {self.cpf}\nSenha: {self.senha}"

    def __repr__(self):
        return f"Nome: {self.nome}\nCPF: {self.cpf}\nSenha: {self.senha}"

    def get_nome(self):
        return self.nome

    def get_cpf(self):
        return self.cpf

    def get_senha(self):
        return self.senha

    def set_nome(self, nome):
        self.nome = nome

    def set_cpf(self, cpf):
        self.cpf = cpf

    def set_senha(self, senha):
        self.senha = senha
