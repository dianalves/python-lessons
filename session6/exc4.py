"""
Seção 6 - Exercicio 4

Tendo como dados de entrada a altura e o sexo de uma pessoa,
construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes formulas:
Para hoemens: (72.7 * altura) - 58
Para mulheres: (62.1 * altura) - 44.7
"""
print("exercicio 4")
height = float(input('Digite sua altura: '))
gender = input('Qual é seu sexo [M/F]? ')
if gender == 'M' or gender == 'm':
    peso_ideal = (72.7 * height) - 58
if gender == 'F' or gender == 'f':
    peso_ideal = (62.1 * height) - 44.7
print('Seu peso ideal é:')
print(peso_ideal)

