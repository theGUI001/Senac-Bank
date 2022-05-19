class Conta:
    def __init__(self, numero, titular,saldo,limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self .limite = limite

    def __str__(self):
        return f'Conta Número: {self.numero}\nTitular: {self.titular}\nSaldo Atual: {self.saldo}\nLimite da Conta:{self.limite}'

class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
    
    def __str__(self):
        return f'Nome Completo: {self.nome} {self.sobrenome}\n CPF: {self.cpf}'