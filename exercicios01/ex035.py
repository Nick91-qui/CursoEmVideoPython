a = int(input('Insira o comprimeto da primeira reta: '))
b = int(input('Insira o comprimeto da segunda reta: '))
c = int(input('Insira o comprimeto da terceira reta: '))

if a+b>c and a+c>b and b+c>a:
    print('Os lados {}, {} e {}, formam um triângulo'.format(a, b, c))
else:
    print('Os lados {}, {} e {}, não formam um triângulo'.format(a, b, c))
