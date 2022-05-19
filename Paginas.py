import Funcoes

## Páginas
def inicio():

    on_init = 1
    while (on_init == 1):
        print(f'Bla bla bla bem vindo')

        init_opcao = int(input(f'Escolha uma opção:\n   1 - Logar\n   2 - Cadastrar\n   3 - Sair\n'))

        if init_opcao == 1:
            Funcoes.logar()
            on_init = 0
        
        elif init_opcao == 2:
            Funcoes.cadastro()
            on_init = 0
        
        elif init_opcao == 3:
            print("Saindo...")
            on_init = 0
        
        else:
            print("Opção inválida! Selecione uma opção válida.")
