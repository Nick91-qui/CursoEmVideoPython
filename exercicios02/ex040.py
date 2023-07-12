n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('Reprovado, sua média foi {:.1f}'.format(media))
elif 7 > media >= 5:
    print('Recuperação, sua média foi {:.1f}'.format(media))
elif media >= 7:
    print('Apovado. sua média foi {:.1f}'.format(media))
else:
    print('Valor inválido')