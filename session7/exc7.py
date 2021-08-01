"""
Seção 3 - Exercicio 7
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo
que calcule seu peso ideal, usando a seguinte formula: (72.7 * altura) - 58
"""
altura = float(input("Qual a sua altura? "))
multiplicar = altura * 72.7
subtrair = multiplicar - 58
print("O seu peso ideal é: {0}".format(subtrair))