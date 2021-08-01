"""
Seção 6 - Exercicio 5

Fazer um algoritmo que leia a variavel 'p' (peso de peixes)
e verifique se há excessos. Se houver, gravar na variavel 'e' (excesso)
e na variavel 'm' o valor de multa que João devera pagar.
Caso contrario mostrar tais variaveis com o conteudo 'zero'.
"""

print('Exercicio 5')
e = 0
m = 0
peso = float(input('digite um numero\n'))
if peso > 50:
    e = peso - 50
    m = e * 4
# print('Peso')
# print(peso)
# print('Excesso de peso')
# print(e)
# print('Multa a pagar')
# print(m)
print(f'Peso {peso}\nExcesso de peso {e}\nMulta a pagar = R$ {m}')
