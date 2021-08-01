"""
Seção 3 - Exercicio 2

Faça um algoritmo que 'calcule o estoque medio de uma peça', sendo que,
estoque_medio = (quantidade_minima + quantidade_maxima) / 2
Calcule o estoque medio

"""
# entrada
quantidade_minima = int(input("Digite o valor minimo do seu estoque: "))
quntidade_maxima = int(input("Digite o valor maximo do seu estoque: "))
# processamento
soma = quantidade_minima + quntidade_maxima
dividi = soma / 2
# resultado
print(" Seu estoque medio é {0}".format(dividi))