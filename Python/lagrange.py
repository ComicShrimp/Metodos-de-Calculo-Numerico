# Created by: Mário Victor Ribeiro Silva

# Função para verificar se o valor passado é um numero
def isnumber(var):
    try:
        float(var)
        return True
    except:
        pass

    return False


# Inicialização das variaveis
inp = 0
i = int(input('Numero de pontos: '))
x = []
fx = []
k = 0

print('\nX\n')

# Obtenção dos valores de X
while k < i:
    k = k + 1
    inp = input('Valor de x ({}) : '.format(k))
    if isnumber(inp):
        x.append(float(inp))

print('\nFx\n')
inp = 0
j = 0

# Obtenção dos valores de Y
while j < i:
    j = j + 1
    inp = input('Valor de Y ({}) : '.format(j))
    if isnumber(inp):
        fx.append(float(inp))
    else:
        print('\nDeve ser um numero.\n')
        j = j - 1

valor = float(input('Valor de x a ser encontrado: '))


y = 0

for n in range(0, i):
    Lx = 1
    for p in range(0, i):

        if p != n:
            Lx = Lx * ((valor - x[p]) / (x[n] - x[p]))

    y = y + (Lx * fx[n])

print('\nx: {}'.format(x))
print('Fx : {}'.format(fx))
print('\nValor de F({}) : {:.6f}'.format(valor, y))
