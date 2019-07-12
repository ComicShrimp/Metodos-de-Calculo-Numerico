# Created by: Mário Victor Ribeiro Silva
import math


def funcao(x):
    return 0.2 + (25 * x) - (200 * math.pow(x, 2)) + (675 * math.pow(x, 3)) - (900 * math.pow(x, 4)) + (400 * math.pow(x, 5))


a = float(input('Valor de a: '))
b = float(input('Valor de b: '))

passos = input('Especificar passo (s/n) ? ')

# obtem o tamanho do passo
if passos == 's':
    seg = float(input('Quantidade de segmentos (Deve ser divisivil por 3): '))
    h = (b - a) / seg
else:
    seg = 3
    h = (b - a) / seg

If = 0

f = a
i = 0

while i < seg / 3:
    If = funcao(f) + 3 * funcao(f + h) + 3 * funcao(f + (2 * h)) + funcao(f + (3 * h))
    f = f + (3 * h)
    i = i + 1

If = ((3 * h) / 8) * If

print('Resultado de If : {:.6f}'.format(If))
