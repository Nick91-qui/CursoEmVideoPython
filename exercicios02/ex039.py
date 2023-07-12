from datetime import date
atual = date.today().year
ano = int(input("Digite seu ano de nascimento: "))
idade = atual - ano

print('Você tem {} anos'.format(idade))
if idade < 18:
    tfalta = 18 - idade
    print('Você precisará se alistar em {} ano(s)'.format(tfalta))
    anof = atual + tfalta
    print('Seu alistamento será em: {}'.format(anof))
elif idade == 18:
    print('Está na hora de se alistar')
else:
    tpassou = idade - 18
    print ('Ja se passaram {} ano(s) do tempo de alistamento'.format(tpassou))
    anop = atual - tpassou
    print('Seu alistamento foi em: {}'.format(anop))