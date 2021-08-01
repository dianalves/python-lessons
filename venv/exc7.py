"""
Seção 6 - Exercicio 7

Desenvolva um algoritmo que:
1 Leia quatro numeros;
2 Calcule o quadrado de cada um;
3 Se o valor resultado do quadrado do terceiro for >= 1000, imprima-o e finalize
4 Caso contrario, imprima os valores lido e seus respectivos quadrados.
"""

print('Exercicio 7')
answer = input("Digite 4 numeros separados por espaço: ").split(' ')
potencias = [int(number)**2 for number in answer]
print(potencias)