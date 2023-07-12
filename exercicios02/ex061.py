primeiro = int(input("digite um valor para calculo de PA: "))
razao = int(input("digite o valor da razao: "))
decimo = primeiro + (10 - 1) * razao

c = primeiro

while(c < decimo + razao):
    print("{} ".format(c), end="-> ")
    c = c + razao
    
print("ACABOU")
