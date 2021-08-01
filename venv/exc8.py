"""
Seção 6 Exercicio 8

Faça um algoritmo que leia um numero inteiro e
mostre uma mensagem indicando se este numero é par ou impar,
e se é posotivo ou negativo,
"""

print('Exercicio 8')
n1 = int(input('Digite um numero qualquer de 1 a 100\n'))
if (n1 % 2 == 0):
    print('Numero par')
else:
    print('Numero impar')
if (n1 > 0):
    print('Numero maior que zero')
else:
    print('Numero menor do que zero')