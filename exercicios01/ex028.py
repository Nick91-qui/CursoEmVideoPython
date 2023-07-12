#import random
#n = [0, 1, 2, 3, 4, 5]
#sorteio = random.choice(n)
#p = int(input('Digite um núdero de 0 a 5: '))
#if p==sorteio:
#    print('Você acertou')
#else:
#    print('Tente outra vez')
#print(sorteio)

from random import randint
computador = randint(0,5)
jogador = int(input('Digite um número inteiro entre 0 e 5: '))
if jogador == computador:
    print('Venceu!')
else:
    print('Ganhei, pensei no número {}, e não no {}'.format(computador, jogador))