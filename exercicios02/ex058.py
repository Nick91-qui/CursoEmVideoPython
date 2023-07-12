from random import randint
'''n = 0
computador = randint(0, 10)
jogador = int(input('Digite um número inteiro entre 0 e 10: '))
while jogador != computador:
    print('Tente novamente!')
    jogador = int(input('Digite um número inteiro entre 0 e 10: '))
    n += 1
    print('Você ganhou! o número é: {}, você precisou de {} tentativas'.format(computador, n))
'''
computador = randint(0, 10)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('numero entre 0  e 10: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador< computador:
            print('Mais alto')
        elif jogador > computador:
            print("Mais baixo")
print('Você ganhou! o número é: {}, você precisou de {} tentativas'.format(computador, palpites))
