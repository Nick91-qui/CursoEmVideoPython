n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
op = 0
while op != 5:
    op = int(input('''
    Escola uma das opções a seguir:
    [1] Somar;
    [2] Multiplicar;
    [3] Maior;
    [4] Novos números;
    [5] encerrar programa;
    '''))
    if op == 1:
        print(('o resultado de {} + {} é: {}') .format(n1, n2, n1 + n2))
    elif op == 2:
        print(('o resultado de {} x {} é: {}') .format(n1, n2, n1 + n2))
    elif op == 3:
        if n1 > n2:
            print(('O maior número é: {}').format(n1))
        else:
            print(('O maior número é: {}').format(n2))
        
    elif op == 4:
        print("digite novos números: ")
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif op == 5:
        print('Fim!')
    else:
        print('Opção inválida, tente novamente.')
    print('=-=' * 10)
