sal = float(input('Digite seu salário: '))
if(sal>1250.00):
    print('Seu salário será de: R${:.2f}'.format(sal*1.10))
else:
    print('Seu salário será de: R${:.2f}'.format(sal*1.15))

if sal > 1250:
    novo = sal * 1.10
else:
    novo = sal * 1.15
print('Novo salário é: R${:.2f}'.format(novo))