"""
Seção 6 - Exercicio 5

Fazer um algoritmo que leia a variavel ´p´(peso de peixes)
e verificar se há excesso. Se houver, gravar na variavel ´e´
e na variavel ´m´o valor da multa que João deverar pagar.
Caso contrario mostrar variaveis ´zero´

"""

p = float(input('Digite o peso dos peixes: '))
if p > 50:
    m = (p - 50) * 4
    e = "excesso"
    print("Você deverar pagar R$ {0:.2f}".format(m))
else:
    m = 0
    e = 0
    print("Multas: {0}".format(m))
    print("Excesso: {0}".format(e))