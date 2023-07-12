a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
if a == b:
    print('{} é igual a {}'.format(a, b))
elif a > b:
    print('{} é maior que {}'.format(a, b))
    print('{} é menor que {}'.format(b, a))
else:
    print('{} é maior que {}'.format(b, a))
    print('{} é menor que {}'.format(a, b))

