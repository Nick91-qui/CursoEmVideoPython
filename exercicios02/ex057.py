sexo = 0
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo [M/F]: ')).upper()
    if sexo != 'M' and sexo != 'F':
        print("Dado inválido, por favor digite novamente")
    
print('Su resposta foi: {}'.format(sexo))