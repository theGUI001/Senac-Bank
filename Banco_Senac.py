import Classes

def logar():
    print("Não disponível no momento")

def pag_inicio():
    print(f'Bla bla bla bem vindo')
    operacao = input("Escolha uma opção:\n 1 - Logar\n 2 - Cadastrar\n")
    if operacao == "1" or "Logar":
        logar()
    


objeto_conta = Classes.Conta(1, 'Carlos', 120.0, 2000)
pag_inicio()
