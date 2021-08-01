"""
Seção 3 - Exercicio 6
Faça um algoritmo que pergunte quanto você ganha por hora e o numero de
horas trabalhadas no mês. Calcule e mostre o total do seu salario no referido mês.

"""
quantidade_de_horas_trabalhadas = int(input(" Digite as horas trabalhadas no mês: "))
valor_da_hora = float(input("Digite o valor ganhado por hora: "))
multiplicar = quantidade_de_horas_trabalhadas * valor_da_hora
print("Total do salario referido no mês è {0}".format(multiplicar))