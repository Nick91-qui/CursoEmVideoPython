# laço -for- precisa de um -range- limite.
# while == enquanto
'''
for c in range(1, 10):
    print (c)
print('fim')

c = 1
while c < 10:
    print (c)
    c += 1
print('Fim')

for c in range(1, 5):
    n = input('Digite um número: ')
print('Fim')

n = 1
r = 'S'
#while n != 0:

#print('Fim')

while r == 'S':
    n = int(input('Digite um número: '))
    r = str(input('continue? [S/N]: ')).upper()
print('Fim!')
'''

n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('{} pares e  {} ímpares'.format(par, impar))