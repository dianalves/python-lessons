largura = int(input('Ditige a largura da parede em metros: '))
altura = int(input('Digite a altura da parede em metros: '))
area = largura * altura
quantidade_tinta = area / 2
print('A area da porta é {}m2 e a quantidade de tinta necessaria é {}L'.format(area, quantidade_tinta))
