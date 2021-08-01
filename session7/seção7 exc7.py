"""
Seção 7 Exercicio 7

"""

quantidade = 0
necessita_esfera = 0
necessita_limpeza = 0
necessita_troca_cabo = 0
quebrado = 0
identificacao = int(input("Digite o numero de identificação do mouse: "))
while identificacao != 0:
    print("Identifique o defeito")
    print("1 = necessita de esfera")
    print("2 = necessita de limpeza")
    print("3 = necessita de troca")
    print("4 = quebrado")
    defeito = int(input("Digite o tipo de defeito: "))
    if defeito == 1:
        necessita_esfera = necessita_esfera + 1
    elif defeito == 2:
        necessita_limpeza = necessita_limpeza + 1
    elif defeito == 3:
        necessita_troca_cabo = necessita_troca_cabo + 1
    elif defeito == 4:
        quebrado = quebrado + 1
    quantidade = quantidade + 1
    identificacao = int(input("Digite o numero de identificação do mouse: "))
perc_esfera = (necessita_esfera * 100) / quantidade
perc_limpeza = (necessita_limpeza * 100) / quantidade
perc_cabo = (necessita_troca_cabo * 100) / quantidade
perc_quebrado = (quebrado * 100) / quantidade
print("Situação                  Quantidade            Percentual")
print("1 - necessita de esfera      {0}               {1:.2f}%".format(necessita_esfera, perc_esfera))
print("2 - necessita de limpeza     {0}               {1:.2f}%".format(necessita_limpeza, perc_limpeza))
print("3 - necessita de troca       {0}               {1:.2f}%".format(necessita_troca_cabo, perc_cabo))
print("4 - quebrado                 {0}               {1:.2f}%".format(quebrado, perc_quebrado))
