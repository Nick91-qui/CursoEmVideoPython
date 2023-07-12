import math
ca = float(input('Digite o cateto adjacente: '))
co = float(input('Digite o Cateto oposto '))
hip = math.sqrt((ca**2)+(co**2))
h1 = (ca ** 2 + co ** 2) ** (1/2)
print('Para o cateto adjacente {} e oposto {} o valor da hipotenusa é {}!'.format(ca, co, hip))

h = math.hypot(ca, co)
print('Hipotenusa é: ', h, h1)
