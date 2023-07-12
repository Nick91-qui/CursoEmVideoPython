from random import randint
n = 0
computador = randint(0,5)
jogador = int(input('Digite um número inteiro entre 0 e 5: '))
while jogador != computador:
    print('Tente novamente!')
    jogador = int(input('Digite um número inteiro entre 0 e 5: '))
    n += 1
    print('Você ganhou! o número é: {}, você precisou de {} tentativas'.format(computador, n))