"""
Seção 6 - Exercicio 6

Elabore um algoritmo que leia as variaveis 'c' e 'n'
respectivamente codigo e numero de horas trabalhadas de um operario.
Calcule o salario sabendo-se que ele ganha 10 reais por hora.
Quando o numero de horas exceder a 50 calcule o excesso de pagamento
armazenando-o na variavel 'e'. Caso contrario zerar tal variavel .
A hora excedente de trabalho vale 20 reais. No final do processo imprimir
o salario total e o salario excedente.
"""

print('Exercicio 6')
e = 0
c = int(input('Digite um codigo\n'))
n = int(input('Digite as horas de trabalho\n'))
if n > 50:
    e = n - 50
    n = n - e
extra = e * 20
salario = n * 10
print('Salario')
print(salario)
print('Extra')
print(extra)
