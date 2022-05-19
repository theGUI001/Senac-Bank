from datetime import date
import Classes

def logar():
    print('Não disponível no momento')

def cadastro(id_Conta, nome, saldo, limite):
    objeto_conta = Classes.Conta(id_Conta, nome, saldo, limite)
    print(objeto_conta)


def inicio():

    on_init = 1
    while (on_init == 1):
        print(f'Bla bla bla bem vindo')

        init_opcao = int(input(f'Escolha uma opção:\n   1 - Logar\n   2 - Cadastrar\n   3 - Sair\n'))

        if init_opcao == 1:
            logar()
            on_init = 0
        
        elif init_opcao == 2:
            numeroConta = date.today()
            nome = input("Digite seu nome: ")
            saldo = float(input("Digite a quantia que deseja para abrir a conta: "))
            limite = float(input("Digite o limite que você deseja: "))
            cadastro(numeroConta,nome,saldo, limite)
            on_init = 0
        
        elif init_opcao == 3:
            print("Saindo...")
            on_init = 0
        
        else:
            print("Opção inválida! Selecione uma opção válida.")

inicio()