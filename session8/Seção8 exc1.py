"""
Seção 8 - Exercicio 1
Faça um algoritmo que carregue um vetor de 5 elementos inteiros
e em seguida armazene em um vetor apenas os numeros pares maiores que 0
No final mostre os elementos do vetor na tela.
"""

vetor = []
pares = []
for n in range(0, 5):
    vetor.append(n)
    if n % 2 == 0:
        pares.append(n)
for p in pares:
    print(p)