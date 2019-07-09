# Created by: Mário Victor Ribeiro Silva
import math

def equacao(x):

    # Digitar a equação para o metodo da bisseção entre os parentesis.
    return (8 - 4.5*(x - math.sin(x)))


print('=' * 20)
print('Metodo da Bisseção')
print('=' * 20)

# Variavel para determinar o inicio e o do intervalo
a = float(input('Digite o valor inicial do intevalo: '))
b = float(input('Digite o valor final do intervalo: '))

# Variavel para guardar a tolerancia máxima
tol = float(input('Digite a tolerância: '))

erro = -1

print('-' * 73)
print('| {:^9} | {:^9} | {:^9} | {:^9} | {:^9} | {:^9} |'.format('a', 'b', 'Xn', 'F(a)', 'F(Xn)', 'Tol.'))

while erro > tol or erro == -1:

    Xn = (a + b) / 2

    Fa = equacao(a)
    Fx = equacao(Xn)

    erro = math.sqrt(math.pow(((b - a) / 2), 2))

    print('| {:9.6f} | {:9.6f} | {:9.6f} | {:9.6f} | {:9.6f} | {:9.6f} |'.format(a, b, Xn, Fa, Fx, erro))

    if Fa * Fx < 0:
        b = Xn
    else:
        a = Xn

print('-' * 73)
