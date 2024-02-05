print("Bem vindo ao Controle de Estoque da Bicicletaria do Alex Sander Ohs")

pecas = []  # Lista vazia para armazenar as peças cadastradas
1
def cadastrarPeca():
    # Função para cadastrar uma nova peça
    codigo = float(input("Digite o código: "))
    nome = input("Digite o nome da peça: ")
    fabricante = input("Digite o fabricante da peça: ")
    valor = input("Digite o valor da peça: ")

    peca = {"Codigo": codigo, "Nome": nome, "Fabricante": fabricante, "Valor": valor}
    pecas.append(peca)

    print("Peça cadastrada com sucesso!")
    
def consultarTodasPecas():
    # Função para consultar todas as peças cadastradas
    print("Lista de todas as peças cadastradas:")
    for peca in pecas:
        print(peca)
    print()

def consultarPecaPorCodigo():
    codigo = input("Digite o código da peça: ")
    for peca in pecas:
        if peca["Codigo"] == float(codigo):
            print("Peça encontrada:")
            print(peca)
            return

def consultarPecasPorFabricante():
    fabricante = input("Digite o fabricante desejado: ")
    encontradas = []
    for peca in pecas:
        if peca["Fabricante"] == fabricante:
            encontradas.append(peca)

    if encontradas:
        print(f"Peças encontradas do fabricante '{fabricante}':")
        for peca in encontradas:
            print(peca)
    else:
        print(f"Nenhuma peça encontrada do fabricante '{fabricante}'.")
    print()
    
def removerPeca():
    codigo = float(input("Digite o código da peça que deseja remover: "))
    for peca in pecas:
        if peca["Codigo"] == codigo:
            pecas.remove(peca)
            print("Peça removida com sucesso!")
            return
    print("Nenhuma peça encontrada com o código informado.")
   

def exibirMenu():
    # Função para exibir o menu de opções
    print("1 - Cadastrar Peça")
    print("2 - Consultar Todas as Peças")
    print("3 - Consultar Peças por Código")
    print("4 - Consultar Peças por Fabricante")
    print("5 - Remover Peça")
    print("6 - Sair")
    
def main():
     # Função principal que controla o fluxo do programa
    while True:
        exibirMenu()
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            codigo = len(pecas) + 1  # Utiliza o tamanho da lista + 1 como código
            cadastrarPeca()
        elif opcao == "2":
            consultarTodasPecas()
        elif opcao == "3":
            consultarPecaPorCodigo()
        elif opcao == "4":
            consultarPecasPorFabricante()
        elif opcao == "5":
            removerPeca()
        elif opcao == "6":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Digite novamente.")

if __name__ == "__main__":
    main()
    #A função mainé a função principal que controla o fluxo do programa. Ela exibe o menu, recebe a opção do usuário e chama as funções correspondentes de acordo com a opção escolhida. O programa continua executando até que a opção "6" (Sair) seja escolhida.