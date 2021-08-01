"""
Seção 6 - Exercicio 7

Desenvolva um algoritmo que:
1 Leia quatro numeros;
2 Calcule o quadrado de cada um;
3 Se o valor resultado do quadrado do terceiro for >= 1000, imprima-o e finalize
4 Caso contrario, imprima os valores lido e seus respectivos quadrados.
"""

print('Exercicio 7')
n1 = int(input("Digite um primeiro numero\n"))
n2 = int(input("Digite um segundo numero\n"))
n3 = int(input("Digite um terceiro numero\n"))
n4 = int(input("Digite um quarto numero\n"))
q1 = n1 ** 2
q2 = n2 ** 2
q3 = n3 ** 2
q4 = n4 ** 2
if q3 >= 1000:
    print('Valor maior que 1000')
    print('q3')
else:
    print('Sem valores maior que 1000')
    print(n1, q1)
    print(n2, q2)
    print(n3, q3)
    print(n4, q4)
