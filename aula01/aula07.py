# (**) = potencia, (//) = divisão inteira


# ordem de precedência
# (), **, * / // %, + _

# potencia == pow(base,expoente)
# raiz == n**(1/indiceDaRaiz)
# 'string'*n == escreve a string n vezes


#formatação de texto:
# '{<n}'.format() == alinhado a esquerda
# '{>n}'.format()  == alinhado a direita
# '{^n}'.format()  == alinhado centralizado
# O 'n' indica o numero de espaços que deve ser usado para imprimir
# podesse adicionar caracteres
# \n == quebra de linha

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \no produto é {} e a divisão é {:.3f}'.format(s, m, d), end =" ")
print ('Divisao inteira {} e potência {}'.format(di, e))
