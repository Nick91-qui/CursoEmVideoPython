from datetime import date
atual = date.today().year
contmaior = 0
contmenor = 0
for pess in range(1, 7):
    nasc = int(input('Insira o ano que a {}ª pessoa nasceu: '.format(pess)))
    idade = atual - nasc
    if idade >= 18:
       contmaior += 1
    else:
       contmenor += 1
print('{} Maiores de idade e {} com menores de idade'.format(contmaior, contmenor))
    