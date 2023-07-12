#from random import choice


#a = 'Pedra'
#b = 'Papel'
#c = 'Tesoura'
#jokenpo = [a, b, c]
#pc = choice(jokenpo)
#
#jog = str(input('Vamos jogar Jokenpo, escolha Pedra, Papel ou Tesoura: ')).capitalize()
#if jog == 'Pedra':
#    jog = a
#elif jog == 'Papel':
#    jog = b
#elif jog == 'Tesoura':
#    jog = c
#else:
#    print('Jogada inválida')
#    
#if jog != a and jog != b and jog != c:
#    print('Tente outra vez!')
#elif pc == jog:
#    print('Eu escolhi {} e você {}. Empatou!'.format(pc, jog))
#elif pc == b and jog == a:
#    print('Eu escolhi {} e você {}. Você perdeu!'.format(pc, jog))
#elif pc == c and jog == b:
#    print('Eu escolhi {} e você {}. Você perdeu!'.format(pc, jog))
#elif pc == a and jog == c:
#    print('Eu escolhi {} e você {}. Você perdeu!'.format(pc, jog))
#else:
#    print('Eu escolhi {} e você {}. Você Ganhou!'.format(pc, jog))
#    

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
jog = int(input('''[0] = Pedra, 
[1] = Papel 
[2] = Tesoura
Sua escolha: '''))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('Computador jogou {} e jogador {}'.format(itens[pc], itens[jog]))
if pc == 0:
    if jog == 0:
        print('EMPATE')
    elif jog == 1:
        print('GANHOU')
    elif jog == 2:
        print('PERDEU')
    else:
        print('Jogada inválida')

elif pc == 1:
    if jog == 1:
        print('EMPATE')
    elif jog == 2:
        print('GANHOU')
    elif jog == 0:
        print('PERDEU')
    else:
        print('Jogada inválida')

elif pc == 2:
    if jog == 2:
        print('EMPATE')
    elif jog == 0:
        print('GANHOU')
    elif jog == 1:
        print('PERDEU')
else:
    print('Jogada inválida')



