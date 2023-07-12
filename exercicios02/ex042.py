a = int(input("Primeiro lado: "))
b = int(input('Segundo lado: '))
c = int(input('Terceiro lado: '))
if a + b < c or a + c < b or b + c < a:
    print('Não é um triângulo')
elif a == b and b == c:
    print("É um triângulo Equilátero")
elif a != b and a != c and b != c:
    print('É um triângulo escaleno')
else:
    print('É um triângulo isósceles')