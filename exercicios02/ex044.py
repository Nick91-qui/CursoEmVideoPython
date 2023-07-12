preco = float(input("Preço do produto: "))
pgto = int(input('''Escolha a forma de pagamento: 
[ 1 ] À vista dinheiro/cheque. 
[ 2 ] À vista no cartão. 
[ 3 ] 2x no credito. 
[ 4 ] 3x ou mais no crédito. 
Digite onúmero da forma de pagamento: '''))
if pgto == 1:
    print('Valor da compra: R${:.2f}'.format(preco * 0.9))
elif pgto == 2:
    print('Valor da compra: R${:.2f}'.format(preco * 0.95))
elif pgto == 3:
    parcela = preco / 2
    print('Valor da compra: R${:.2f}, em duas vezes de {}'.format(preco, parcela))
elif pgto == 4:
    total = preco * 1.2
    totparc = int(input('Quantas vezes: '))
    parcela = total / totparc
    print('Valor da compra: R${:.2f} em {} vezes de {}'.format(total, totparc, parcela))
else:
    print('Opção inválida de pagamento')
    print('Valor da compra: R${:.2f}'.format(preco))