preco = float(input('Insira o preço: '))
desconto = preco - (preco*0.05)
print('O novo preço com desconto é: R${:.2f}.'.format(desconto))