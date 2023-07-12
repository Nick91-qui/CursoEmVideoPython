num = int(input('Diegite um número inteiro: '))
print(''' Escolha uma das bases para converção:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
conv = int(input('Sua opção: '))

if conv == 1:
    print('{} convertido para BINÁRIO é = {}'.format(num, bin(num)))
elif conv == 2:
    print('{} convertido para OCTAL é = {}'.format(num, oct(num)))
elif conv == 3:
    print('{} convertido para HEXADECIMAL é = {}'.format(num, hex(num)))
else:
    print('conversão inválida')