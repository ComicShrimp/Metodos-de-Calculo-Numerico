import math


def cacula(valores, matr, atual, tam):
    resultado = 0
    for k in range(0, tam):
        if k != atual:
            resultado += (-1 * matr[k][atual]) * valores[k]
        else:
            resultado += matr[tam][atual]

    return resultado / matr[atual][atual]


matriz = []

n = int(input('Digite o tamanho da Matriz: '))
print('Atenção, ordem das colunas invertidas, digite seguindo de cima a baixo a matriz, ', end='')
print('e não da esquerda pra direita.')

for c in range(0, n):
    linha = []
    for l in range(0, n):
        item = float(input('M[{}][{}]: '.format(c, l)))
        linha.append(item)

    matriz.append(linha)

res = []
for r in range(0, n):
    res.append(float(input('Resutaldo da linha {} : '.format(r))))
matriz.append(res)

tolerancia = float(input('Digite a tolerancia: '))
#valores_init = str(input('Usar valores iniciais ? [y/n] '))

valore_x = [0] * n

erro = -1

interacao = 0

while erro > tolerancia or erro == -1:
    interacao += 1
    iX = valore_x[0]
    for i in range(0, n):
        valore_x[i] = cacula(valore_x, matriz, i, n)

    if iX != 0:
        erro = math.sqrt(math.pow((valore_x[0] - iX) / iX, 2))

    print('\n\nValores da interação k = {}: '.format(interacao))

    i = 0
    for h in valore_x:
        print('\nX[{}] : {}'.format(i, h))
        i += 1

    print('\nErro : {}'.format(erro))

print('\n\n Finalizado !!!')