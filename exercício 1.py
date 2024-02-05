print("Bem-vindo à loja do Alex Sander Ru :4364850")

valor_unitario = float(input("Digite o valor unitário do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))

#Aqui foi feito o valor flutuante do valor unitário do produto, sendo a quantidade números inteiros.
#Pedindo que insira o valor e quantidade

valor_total = valor_unitario * quantidade

if quantidade < 10:
    desconto = 0
elif quantidade <= 99:
    desconto = 0.05  # 5% de desconto para quantidades entre 10 e 99
    desconto_info = "(desconto 5%)"
elif quantidade <= 999:
    desconto = 0.1  # 10% de desconto para quantidades entre 100 e 999
    desconto_info = "(desconto 10%)"
else:
    desconto = 0.15  # 15% de desconto para quantidades a partir de 1000
    desconto_info = "(desconto 15%)"

#Aqui foi a trajetória de criar os deconto, inserindo o < para ser menos que a quantidade. indo de 1 a 9 etc.

valor_total_com_desconto = valor_total * (1 - desconto)

print("Valor total sem desconto: R$ {:.2f}".format(valor_total))
print("Valor total com desconto: R$ {:.2f} {}".format(valor_total_com_desconto, desconto_info)) 

print("Finalizamos sua compra")