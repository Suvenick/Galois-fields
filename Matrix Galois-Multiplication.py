ch = 'y'
flag = 0
import testProject

# Вывод матрицы
def pr(c):
    for i in range(len(c)):
        for j in range(len(c[0])):
            print(c[i][j], '\t', end=' ')
        print()


def multiply(a, bT):
    # умножаем A*B
    if len(a[0]) != len(b):
        print("Невозможно умножить")
        input()
    # инициализируем матрицу C
    c = [[0 for row in range(len(bT[0]))] for col in range(len(a))]
    for i in range(len(a)):
        for j in range(len(bT[0])):
            for k in range(len(bT)):
                c[i][j] += testProject.multiplication(a[i][k], bT[k][j])
    pr(c)

def assign(a):
    for i in range(r):
        for j in range(c):
            a[i][j] = int(input())


while ch == 'y':
        print("Введите параметры матрицы А\n")
        # initialize Matrix A
        r = int(input("Введите количество строк матрицы A: "))
        c = int(input("Введите количество столбцов матрицы A: "))
        a = [[0 for row in range(r)] for col in range(c)]
        print("Матрица A")
        assign(a)
        print("Матрица A:")
        pr(a)
        input()

        # initialize matrix B
        print("Введите параметры матрицы B\n")
        r = int(input("Введите количество строк матрицы B: "))
        c = int(input("Введите количество столбцов матрицы B: "))
        b = [[0 for row in range(c)] for col in range(r)]
        print("Матрица B")
        assign(b)
        print("Матрица B:")
        pr(b)
        print("Траспонированная матрица B:")
        bT = [[0 for row in range(r)] for col in range(c)]
        for i in range(r):
            for j in range(c):
                bT[j][i] = b[i][j]
        pr(bT)
        input()

        while ch == 'y':
            if flag != 1:
                print("-------------------------------------------------------")
                # Печать матрицы A
                print("Матрица A:", '\n')
                pr(a)

                # Печать матрицы B
                print("\nМатрица B:", '\n')
                pr(b)

                # Печать матрицы С
                print("\nРезультат умножения на транспонированную матрицу", '\n')
                multiply(a, bT)
                break