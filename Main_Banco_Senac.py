import Classes, Funcoes


def pag_inicio():
    
    print(f'Bla bla bla bem vindo')
    
    init_opcao = int(input(f'Escolha uma opção:\n   1 - Logar\n   2 - Cadastrar\n   3 - Sair\n'))
    
    print(f'Opção selecionada: {init_opcao}')
    
    if(init_opcao == 1):
        Funcoes.logar()
    if(init_opcao == 2):
        Funcoes.cadastro()
    if(init_opcao == 3):
        print("Saindo...")
        exit

#objeto_conta = Classes.Conta(1, 'Carlos', 120.0, 2000)

pag_inicio()
