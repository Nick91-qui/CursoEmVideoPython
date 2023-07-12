distancia = float(input('Informe a distãncia percorrida: '))
if(distancia<=200):
    print('Valor: RS {:.2f}'.format(distancia * 0.5))
else:
    print('Valor: RS {:.2f}'.format(distancia * 0.45))

#dist = float(input('Distancia: '))
#if dist <= 200:
#    preço = dist * 0.5
#else:
#    preço = dist * 0.45
#print('Preço = R${:.2f}!'.format(preço))
# ou:
# preço = dist * 0.50 if dist <= 200 elsse dist *0.45
#print('Preço = R${:.2f}!'.format(preço))