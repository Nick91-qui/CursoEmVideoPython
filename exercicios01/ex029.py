vel = int(input('Sua velocidade aqui: '))
if vel > 80:
    print('Você foi multado em R${}'.format((vel - 80) *7))
print('Siga em frente!')

#if vel > 80:
#   multa = (vel-80)*7
#   print('Multa = R${}'.format(multa))