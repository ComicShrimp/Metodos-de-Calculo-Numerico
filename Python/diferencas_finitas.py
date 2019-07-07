import math

# Modificar de Acordo com a questão
def funcao(x):
    return math.pow(x, 3) #+ 4 * x - 15


initp = float(input('Valor do Ponto inicial : '))
h = float(input('Tamanho do Passo: '))

print('Metodo Progressivo : {}'.format((funcao(initp + h) - funcao(initp)) / h))
print('Metodo Regressivo : {}'.format((funcao(initp) - funcao(initp - h)) / h))
print('Metodo Central : {}'.format((funcao(initp + h) - funcao(initp - h)) / 2 * h))
