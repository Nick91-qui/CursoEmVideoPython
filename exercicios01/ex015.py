km = float(input('Km percorridos: '))
dias = int(input('Dias do aluguel: '))
valor = (km*0.15) + (dias*60)
print('Km percorridos: {}, tempo: {} dias, valor a pagar: R${}.'.format(km, dias, valor))