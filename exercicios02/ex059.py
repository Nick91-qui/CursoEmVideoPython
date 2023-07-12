n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
op = int(input('''
Escola uma das opções a seguir:
[1] Somar;
[2] Multiplicar;
[3] Maior;
[4] Novos números;
[5] encerrar programa;
'''))
while op != [1, 2, 3, 4, 5]:
    if op == 1:
        print(n1 + n2)
    if op == 2:
        print(n1 * n2)
    if op == 3:
        if n1 > n2:
            print(n1)
        else:
            print(n2)
        print(n)
    if op == 4:
        print("digite novos números: ")
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    if op == 5:
        print('Fim!')