# Created by: Mário Victor Ribeiro Silva
import math

# função que retorna o valor da equação utilizado no problema
def funcao(x):
    return math.pow(x, 3)

# Obtem os valores necessários
initp = float(input('Valor do Ponto inicial : '))
h = float(input('Tamanho do Passo: '))

# Retorna os 3 tipos de diferenças finitas
print('Metodo Progressivo : {:.6f}'.format((funcao(initp + h) - funcao(initp)) / h))
print('Metodo Regressivo : {:.6f}'.format((funcao(initp) - funcao(initp - h)) / h))
print('Metodo Central : {:.6f}'.format((funcao(initp + h) - funcao(initp - h)) / 2 * h))
