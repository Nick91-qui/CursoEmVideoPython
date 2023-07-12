from datetime import date
atual = date.today().year
nasc = int(input("Digite seu ano de nascimento: "))
idade = atual - nasc
print('Idade: {}'.format(idade))
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('Infantil')
elif idade < 19:
    print('JUNIOR')
elif idade < 20:
    print('SÊNIOR')
else:
    print('Master')