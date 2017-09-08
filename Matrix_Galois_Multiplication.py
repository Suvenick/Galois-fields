import numpy as np
import GFarithmetic
# Вывод матрицы


def create_empty_matrix(rows, cols):
    aux = 2 ** int(GFarithmetic.FIELD_POWER)
    m = np.random.randint(aux, size=(rows, cols))
    return m


def multiply(a, m):

    c = np.zeros(shape=(a.shape[1], m.shape[0]))
    for i in range(len(a)):
        for j in range(len(m[0])):
            for k in range(len(m)):

                c[i][j] += GFarithmetic.multiplication(a[i][k], m[k][j])
    return c


def numberAdd(a, x):
    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j] = GFarithmetic.add(a[i][j], x)
    return a

def numberMultiply(a, x):
    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j] = GFarithmetic.multiplication(a[i][j], x)
    return a

def transpon(m):
    m = m.transpose()
    return m

def deleteRowCol(a,x,y):
    a = np.delete(a, x, 0)
    a = np.delete(a, y, 1)
    return a

def detMarix(a):
    a = (a[0,0] * a[1,1]) - (a[1,0] * a[0,1])
    return a

a = create_empty_matrix(2, 2)
print(a)
print(detMarix(a))

