sexo = 0
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo [M/F]: '))
    if sexo != 'M' and sexo != 'F':
        print("digite novamente")
    
print('Fim')