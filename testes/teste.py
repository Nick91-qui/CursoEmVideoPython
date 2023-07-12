'''a = int(input('numero:'))
b = str(a)
tamanho = len(b)
"print(tamanho)"
"print (b[0])"
c = 0
d = 0
while c < tamanho:
    inttonum = int(b[c])
    resultado = (inttonum * inttonum)
    
    c += 1
    print(resultado)
print (resultado)
print('Fim')'''
def square_digits(num):
    result = ""
    for digit in str(num):
        squared_digit = str(int(digit) ** 2)
        result += squared_digit
    return int(result)
digit = int(input('numero:'))
print(square_digits(digit))
