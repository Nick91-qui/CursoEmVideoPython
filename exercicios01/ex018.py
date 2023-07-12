from math import radians, sin, cos, tan
ang=float(input('Digite o ângulo: '))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tang = tan(radians(ang))

print('seno = {:.2f}, cosseno = {:.2f} tangente = {:.2f}'.format(seno, cosseno, tang))
