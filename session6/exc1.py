"""
Seção 6 - Exercicio 1

1 - ler uma variavel numerica e imprimir se ela for maior que 100,
    caso contrario imprimi-la com o valor zero.
"""
n = int(input('Digite um numero\n'))
if n > 100:
    print("O valor digitado foi maior que 100")
else:
    n = 0
    print('Infelizmente o numero digitado não foi maior que 100')
