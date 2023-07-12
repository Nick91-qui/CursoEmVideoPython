valorcasa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor da sua renda: '))
tempo = float(input('Em quantos anos irá pagar: '))

valormensal = valorcasa / (tempo * 12)

if valormensal > (salario * 0.3):
    print('Seu empréstimo foi negado!')
else:
    print('Seu empréstimo foi aprovado!')