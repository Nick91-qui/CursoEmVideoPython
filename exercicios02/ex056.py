media = 0
somaidade = 0
maioridadehomem = 0
nomevelho =''
totmulher20 = 0
for p in range(1, 5):
    print('-'*25)
    print('{}ª pessoa'.format(p))
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('M / F: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade <20:
        totmulher20 += 1
media = somaidade / 4
print ('media de idade: {}'.format(media))
print('Homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Tem {} mulheres com menos de 20 anos'.format(totmulher20))