import Classes, Funcoes


def pag_inicio():
    print(f'Bla bla bla bem vindo')
    operacao = input("Escolha uma opção:\n 1 - Logar\n 2 - Cadastrar\n 3 - Sair\n")
    
    if operacao == "1" or "Logar":
        Funcoes.logar()
    
    elif operacao == "2" or "Cadastrar":
        Funcoes.cadastro()
    
    elif operacao == "3" or "Sair":
        exit

#objeto_conta = Classes.Conta(1, 'Carlos', 120.0, 2000)

#pag_inicio()
