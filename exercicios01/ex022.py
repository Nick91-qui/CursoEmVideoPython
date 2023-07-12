nome = str(input('Digite seu nome completo: ')).strip()
print(nome.upper(), '\n', nome.lower())
print('Maiúscula: {}, Minúscula: {}'.format(nome.upper(), nome.lower()))

print(len(nome) - nome.count(' '))
print('Letras = {}'.format(len(nome) - nome.count(' ')))

print('Letras primeiro nome: {}'.format(nome.find(' ')))

separa = nome.split()
print('Seu primeiro nome e {}, e tem {} letras'.format(separa[0], len(separa[0])))