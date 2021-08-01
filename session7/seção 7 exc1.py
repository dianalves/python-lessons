"""
Seção 7 - exercicio 1

faça um algoritmo que determine o maior entre N numeros.
A condição de parada é a entrada de um valor 0, ou seja,
o algoritmo deve ficar calculando o maior até que a entrada seja igual a 0 (zero).
"""

maior = 0
n = int(input("Digite um numero: "))
while n != 0:
    if n > maior:
        maior = n
        n = int(input("Digite um numero: "))
print("O maior numero é {0}".format(maior))
