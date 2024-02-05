print("Seja bem-vindo à Companhia de Logística Alex Sander OHS\n")
#O código apresentado é um programa que solicita ao usuário as dimensões
#O(comprimento, largura e altura) de um objeto, bem como o seu peso e a rotação desejada.
def obterDimensoes():
    while True:
        try:
            comprimento = float(input("Digite o comprimento do objeto (em cm): "))
            largura = float(input("Digite a largura do objeto (em cm): "))
            altura = float(input("Digite a altura do objeto (em cm): "))
            return comprimento, largura, altura
        except ValueError:
            print("Por favor, insira valores numéricos para as dimensões do objeto.")
            print("Por favor entre com as dimensões dsejados novamente")

#A função obterDimensoesé responsável por obter as dimensões do objeto a partir de entradas do usuário, garantindo que sejam valores numéricos.

def dimensoesObjeto():
    while True:
        altura, comprimento, largura = obterDimensoes()
        volume = altura * comprimento * largura
        print("O volume do objeto é {} cm³.".format(volume))

        if volume < 1000:
            return 10
        elif 1000 <= volume < 10000:
            return 20
        elif 10000 <= volume < 30000:
            return 30
        elif 30000 <= volume < 100000:
            return 50
        elif volume >= 100000:
            print("Erro: Não é possível aceitar um objeto com volume igual ou superior a 100000 cm³.")
        else:
            raise ValueError("As dimensões do objeto devem ser valores positivos.")

#. A função dimensoesObjetocalcula o volume do objeto e retorna um valor com base em faixas de volume específicas. Se o volume for maior ou igual a 100000 cm³, é exibido um erro.
def pesoObjeto():
    while True:
        try:
            peso = float(input("Digite o peso do objeto em kg: "))

            if peso <= 0.1:
                return 1
            elif 0.1 <= peso < 1:
                return 1.5
            elif 1 <= peso < 10:
                return 2
            elif 10 <= peso < 30:
                return 3
            elif peso >= 30:
                raise ValueError("Não aceitamos produtos tão pesados.")
            else:
                raise ValueError("O peso do objeto deve ser um valor positivo.")

        except ValueError as e:
            print("Erro:", e)

#A função pesoObjetoobtém o peso do objeto, também validando se é um valor positivo.
def rotaObjeto():
    while True:
        rota = input("Digite a rota do objeto (RS, SR, BS, SB, BR, RB): ")

        if rota == "RS" or rota == "SR":
            return 1
        elif rota == "BS" or rota == "SB":
            return 1.2
        elif rota == "BR" or rota == "RB":
            return 1.5
        else:
            print("Rota inválida. Digite uma opção válida.")

# A função rotaObjetosolicita a rota desejada ao usuário, garantindo que seja uma opção válida.
def calcularPrecoObjeto():
    dimensoes = dimensoesObjeto()
    peso = pesoObjeto()
    rota = rotaObjeto()

    total = dimensoes * peso * rota
    print("O total a ser pago é de R${:.2f} (dimensões: {} * peso: {} * rota: {})".format(total, dimensoes, peso, rota))

#A função calcularPrecoObjetochama as funções anteriores para obter as dimensões, peso e rota do objeto, realizar o calculado do preço e imprimir o resultado formatado.
calcularPrecoObjeto()