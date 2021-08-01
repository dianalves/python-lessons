"""
Seção 7 - Exercicio 6
Desenvolva um gerador de tabuada de qualquer
numero inteiro entre 1 a 10. O usuario deve
informa que de qual numero ele deseja
ver a tabuada.
"""

numero = int(input("Digite um numero: "))
while numero < 1 or numero > 10:
    print("Numero deve ser menor que 10")
    numero = int(input(" Digite um numero: "))
print("Tabuada de {0}".format(numero))
for n in range(1, 11):
    print("{0} x {1} = {2}".format(numero, n, (numero * n)))
