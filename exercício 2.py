
print("*       Bem-vindo à Loja do Alex Sander                    *")
print("     ************** Cardápio *************                 *")
print("*                                                          *")
print("* | Código |    Descrição                    | Valor |     *")
print("* |   100  |    1. Cachorro-Quente           | 9,00  |     *")
print("* |   101  |    2. Cachorro-Quente Duplo     | 17,00 |     *")
print("* |   102  |    3. X-Salada                  | 13,00 |     *")
print("* |   103  |    4. X-Bacon                   | 14,00 |     *")
print("* |   104  |    5. X-Tudo                    | 18,00 |     *")
print("* |   105  |    6. X-Egg                     | 11,00 |     *")
print("* |   200  |    7. Refrigerante Lata         | 5,00  |     *")
print("* |   201  |    8. Chá Gelado                | 4,00  |     *")
print("     *************************************                 *")

#Aqui eu criei o cardápio de uma forma simples e com asteriscos para realçar os nomes

produtos = { 100: ["Cachorro-Quente", 9.00],101: ["Cachorro-Quente Duplo", 11.00],
     102: ["X-Egg", 12.00],
     103: ["X-Salada", 13.00],
     104: ["X-Bacon", 14.00],
     105: ["X-Tudo", 17.00],
     200: ["Refrigerante Lata", 5.00],
     201: ["Chá Gelado", 4.00] 
    }

#Nesse dicionário, cada chave representa um código de produto (como 100, 101, etc.)
#

valor_total = 0


while True:
    codigo = int(input("Digite o código do produto desejado: "))
    
    if codigo not in produtos:
        print("Opção inválida!")
        continue
    
    produto = produtos[codigo]
    valor_total += produto[1]
    
    print(f"Produto: {produto[0]} - Valor: R$ {produto[1]:.2f}")
    
    continuar = input("Deseja pedir mais alguma coisa? (S/N): ")
    
    if continuar.upper() == "N":
        break
    
#Faz uma verificação das informações dos dados, perguntando se deseja pedir mais alguma coisa
# Caso não deseje ele para de perguntar se deseja alguma coisa.
    
print(f"\nValor total a pagar: R$ {valor_total:.2f}")
  

    
    
    
    
    
