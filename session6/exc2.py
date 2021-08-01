"""
Seção 6 - Exercìcio 2

Elabore um algoritmo que leia um numero.
Se positivo armazene-o em 'a', se for negativo, em 'b'.
No final mostrar o resultado.
"""
print('exercicio 2')
valor = int(input('digite um numero\n'))
if valor > 0:
    a = valor
    print('valor positivo')
    print(a)
else:
    b = valor
    print("valor negativo")
    print(b)
