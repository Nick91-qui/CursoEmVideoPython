frase = str(input('Digite uma frase: ')).upper().strip()
print('Letra A, aparece {} vezes.'.format(frase.count('A')))
print('A primeira letra A, apareceu na posição {}'.format(frase.find('A')+1)) # +1 por que a posição inicia no 0
print('A última letra A, apareceu na posição {}'.format(frase.rfind('A')+1))