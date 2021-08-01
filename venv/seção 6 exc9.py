"""
Seção 6 - Exercicio 9
Faça um algoritmo que leia o indice de poluição medido
e emita a notificaçao adequada aos diferents grupos de empresa.
"""

indice = float(input("Digite o indice de poluição: "))
if indice >= 0.3 and indice < 0.4:
    print("Atenção! Grupo 1 suspernder atividades.")
elif indice >= 0.4 and indice < 0.5:
    print("Atenção! Grupo 1 e 2 suspender atividades.")
elif indice >= 0.5:
    print("Atenção! Todos os grupos suspender atividades.")
else: indice >= 0.2
print("Niveis aceitaveis")