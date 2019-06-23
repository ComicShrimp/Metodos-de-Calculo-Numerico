import math as m
from decimal import Decimal


def calculaErro(Xp, Xn):
    return abs((Xn - Xp) / Xp)


def funcao(x):
    return round(8 - 4.5 * (x - m.sin(x)), 6)


def secante(X0, X1, e):
    while True:
        x2 = X1 - ((funcao(X1) * (X0 - X1)) / (funcao(X0) - funcao(X1)))
        err = calculaErro(X0, X1)
        print("X0: " + str(round(X0, 6)) + " X1: " + str(round(X1, 6)) + " X2: " + str(round(x2, 6)) + " Erro: " + str(
            round(Decimal(err), 6)))
        print()
        X0 = X1
        X1 = x2
        if err <= e or funcao(x2) == 0:
            return x2


print("A raiz aproximada da função é: " + str(round(secante(2.8, 2.6, 0.002), 6)))
