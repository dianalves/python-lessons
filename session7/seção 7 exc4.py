"""
Construa um algoritmo que leia 10 valores inteiros e positivos e:
1 Encontre o maior valor
2 Encontre o menor valor
3 Calcule a media dos numeros lidos
"""

maior = -200
menor = 201
soma = 0
for n in range(1, 11):
    valor = int(input("Digite um valor: "))
    if valor > 0:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
        soma = soma + valor
    else:
        valor = int(input("Digite um valor: "))
media = soma / 10
print("O maior numero é {0}".format(maior))
print("O menor numero é {0}".format(menor))
print(" A media dos numeros é {0}".format(media))
