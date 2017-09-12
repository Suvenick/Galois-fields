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

Mass = np.zeros(3,dtype=int)
def det(m,Mass):
        Mat = 0
        for i in range(len(m)):
            a = deleteRowCol(m, 0, i)
            print("index=", m[0][i])
            while i >= len(a)-2:
                ind = (-1) ** i
                Mat +=m[0][i] * ind * detMarix(a)
                Mass[i] = Mat
                print(Mat)
                break
            for i in range(len(m)):
                while i < len(a) - 2:
                    det(a,Mass)
                    break
            print("Mass", Mass)
            print(a)

def Minor(a):
        det(a)
def findIndex(a, x ,y):
    row = len(a)
    for i in range(row):
            indexDel = deleteRowCol(a,x,y)
    return indexDel
a = create_empty_matrix(3, 3)
print(a)

print(det(a,Mass))