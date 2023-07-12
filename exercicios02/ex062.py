primeiro = int(input("digite um valor para calculo de PA: "))
razao = int(input("digite o valor da razao: "))
decimo = primeiro + (10 - 1) * razao

c = primeiro

while(c < decimo + razao):
    print("{} ".format(c), end="-> ")
    c = c + razao


razao2 = (int(input('Quer apresentar mais termos? ')))
if (razao2 != 0):
    while(c < decimo + razao2):
        print("{} ".format(c), end="-> ")
        c = c + razao2

    
print("ACABOU")