from datetime import datetime
import Classes

def logar():
    print('Não disponível no momento')

def cadastro(id_Conta, nome, sobrenome, cpf, saldo, limite):
    objeto_conta = Classes.Conta(id_Conta, nome +" "+sobrenome, saldo, limite)
    objeto_cliente = Classes.Cliente(nome,sobrenome,cpf)
    return(objeto_conta, objeto_cliente)

def saque(conta, valor):
    conta['saldo'] -= valor

def deposito(conta, valor):
    conta['saldo'] += valor

def extrato(conta):
    print(f'##########################################################\nAtualizado em: {datetime.now()}\nConta Número: {conta.numero}\nCliente: {conta.titular}\nSaldo Atual: {conta.saldo}\n##########################################################')

def inicio():

    on_init = 1
    while (on_init == 1):
        print(f'##########################################################\nSeja bem-vindo ao Senac Bank!')

        init_operacao = int(input(f'Escolha uma opção:\n   1 - Logar\n   2 - Cadastrar\n   3 - Sair\n##########################################################\n'))

        if init_operacao == 1:
            logar()
        
        elif init_operacao == 2:
            numeroConta = f'{datetime.now().strftime("%Y")}-01'
            nome = input("Digite seu nome: ")
            sobrenome = input("Digite seu sobrenome: ")
            cpf = input("Digite seu CPF: ")
            saldo = float(input("Digite a quantia que deseja para abrir a conta: "))
            limite = float(input("Digite o limite que você deseja: "))
            objeto_conta, objeto_cliente = cadastro(numeroConta,nome,sobrenome,cpf,saldo, limite)
            operações(objeto_conta)
            on_init = 0
        
        elif init_operacao == 3:
            print("Saindo...")
            on_init = 0
        
        else:
            print("Opção inválida! Selecione uma opção válida.")

def operações(conta):
    init_operacao = int(input(f'Escolha uma opção:\n   1 - Sacar\n   2 - Depositar\n   3 - Extrato\n   4 - Sair'))

    if init_operacao == 1:
        pass
    
    elif init_operacao == 2:
        pass

    elif init_operacao == 3:
        extrato(conta)
    
    elif init_operacao == 4:
        print("Saindo...")
        exit
    
    else:
        print("Opção inválida! Selecione uma opção válida.")

inicio()