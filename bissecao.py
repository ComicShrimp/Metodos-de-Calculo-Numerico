import math

def equacao(x):

    # Digitar a equação para o metodo da bisseção entre os parentesis.
    return (8 - 4.5*(x - math.sin(x)))

print('=' * 10)
print('Metodo da Bisseção')
print('=' * 10)

# Variavel para determinar o inicio e o do intervalo
a = float(input('Digite o valor inicial do intevalo: '))
b = float(input('Digite o valor final do intervalo: '))

# Variavel para guardar a tolerancia máxima
tol = float(input('Digite a tolerância: '))
