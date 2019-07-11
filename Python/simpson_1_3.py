# Created by: Mário Victor Ribeiro Silva
import math


def funcao(x):
    return 0.2 + (25 * x) - (200 * math.pow(x, 2)) + (675 * math.pow(x, 3)) - (900 * math.pow(x, 4)) + (400 * math.pow(x, 5))


a = float(input('Valor de a: '))
b = float(input('Valor de b: '))

passos = input('Especificar passo (s/n) ? ')

if passos == 's':
    h = float(input('Digite o passo: '))
    h = (b - a) / h
else:
    h = (b - a) / 2

sompar = 0
somimpar = 0

k = 2

j = a + h

while j < b:
    if k % 2 == 0:
        sompar = sompar + funcao(j)
    else:
        somimpar = somimpar + funcao(j)

    k = k + 1
    j = j + h

If = (h / 3) * (funcao(a) + (4 * sompar) + (2 * somimpar) + funcao(b))
print('Resultado de I(f): {:.6f}'.format(If))
