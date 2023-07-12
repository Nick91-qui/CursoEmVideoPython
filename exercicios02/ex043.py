peso = float(input('Insira sua massa: '))
altura = float(input('Insira sua altura: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print("Seu IMC é {:.2f}, você está abaixo do peso".format(imc))
elif 18.5 <= imc <25:
    print("Seu IMC é {:.2f}, você está no peso ideal".format(imc))
elif 25 <= imc < 30:
    print("Seu IMC é {:.2f}, você está no sobrepeso".format(imc))
elif 30 <= imc < 40:
    print("Seu IMC é {:.2f}, você está com obesidade".format(imc))
elif imc>= 40:
    print("Seu IMC é {:.2f}, você está com obesidade mórbida".format(imc))