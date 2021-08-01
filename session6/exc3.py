"""
Seção 6 - Exercicio 3

Ler um numero e verificar se ele é par ou impar.
Quando for par armazenar esse valor em 'p' e quando for impar armazena-lo em 'i'.
Exibir 'p' e 'i' no final do processamento.
"""

print('Exercicio 3')
p = 0
i = 0
valor = int(input('digite um numero\n'))
if valor % 2 == 0:
    p = valor
    print('par')
else:
    i = valor
    print('impar')
print(p)
print(i)
