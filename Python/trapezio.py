# Created by: Mário Victor Ribeiro Silva
import math


def funcao(x):
    return 1 - math.pow(math.e, (-2 * x))


segmentos = int(input('Número de Segmentos: '))
a = float(input('Valor do ponto inicial (a): '))
b = float(input('Valor do ponto final (b): '))

# Verifica se o numero de segmentos é positivo
if segmentos == 1:
    resultado = ((funcao(a) + funcao(b)) / 2) * (b - a)
elif segmentos <= 0:
    resultado = 'Não é possivel usar um numero negativo de segmentos'
else:
    h = (b - a) / segmentos
    aux = 0

    while a < b:
        aux = aux + funcao(a) + funcao(a + h)
        a = a + h

    resultado = (h / 2) * aux

print('Resultado : {:.6f}'.format(resultado))
