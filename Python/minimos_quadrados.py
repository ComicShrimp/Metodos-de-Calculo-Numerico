# Creted by: Mário Victor Ribeiro Silva
import math

pontos = int(input('Número de Pontos: '))

x = []

i = 0

print('\nX\n')

# Obtem valores de X
while i < pontos:
    x.append(float(input('X ({}): '.format(i))))
    i = i + 1

print('\nY\n')

y = []
i = 0

# Obtem valores de Y
while i < pontos:
    y.append(float(input('Y ({}): '.format(i))))
    i = i + 1

valorEncontrar = float(input('Para qual valor ? '))

i = 0

# Variaveis utilizadas
somax = 0
somay = 0
somax2 = 0
somaxy = 0
quadradoSomaX = 0

# Laço para realizar o somatorio de todos os pontos
while i < pontos:
    somax = somax + x[i]
    somay = somay + y[i]
    somax2 = somax2 + math.pow(x[i], 2)
    somaxy = somaxy + (x[i] * y[i])
    i = i + 1

quadradoSomaX = math.pow(somax, 2)

a1 = ((pontos * somaxy) - (somax * somay)) / (pontos * somax2 - quadradoSomaX)
a0 = ((somax2 * somay) - (somaxy * somax)) / (pontos * somax2 - quadradoSomaX)

resultado = a0 + a1 * valorEncontrar

print('Equação: {:.6f} + {:.6f} * x'.format(a0, a1))
print('Valor final: {:.6f}'.format(resultado))
