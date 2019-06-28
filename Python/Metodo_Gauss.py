def pivoteamento(A):
    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            n1 = A[j][i]
            if n1 == 0:
                for k in range(i, len(A)):
                    if A[k][i] != 0:
                        troca(A, i, k)
                        n1 = A[j][i]
            n2 = A[i][i]
            if n2 == 0:
                continue
            div = n1 / n2
            A[j] = somaVetor(multipVetor(A[i], -div), A[j])
    return A


def multipVetor(v, x):
    newV = []
    for i in range(len(v)):
        newV += [v[i] * x]
    return newV


def somaVetor(v1, v2):
    newV = []
    for i in range(len(v1)):
        newV += [v1[i] + v2[i]]
    return newV


def troca(A, i, j):
    newI = []
    newJ = []
    for index in range(len(A) + 1):
        newI += [A[j][index]]
        newJ += [A[i][index]]
    A[i] = newI
    A[j] = newJ


def printMatrix(A):
    linhas = len(A)
    colunas = len(A[0])
    for i in range(linhas):
        for j in range(colunas):
            if j == colunas - 1:
                print(round(A[i][j], 6))
                print("\t")
            else:
                print(round(A[i][j]), end=" ")


A = [[2, 1, -3, -1], [-1, 3, 2, 12], [3, 1, -3, 0]]
printMatrix(A)
print("\n\n")
printMatrix(pivoteamento(A))
