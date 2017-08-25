import numpy as np

FIELD_POWER ="3" #'32'
ZERO_POLY = "1011" #'10000000001000000000000000000111' #здесь должен быть не приводимый элемент поля x^32+x^22+x^2+x+1
number1 = str  #первый элемент поля
number2 = str  #второй элемент поля
FIELD_POW = {"2": "7", '3': "13", "4": "23", "5": "45", "6": "103", "7": "203", "8": "435", "9": "1021",
             "10": "2011", "11": "4005", "12": "4005", "13": "20033", "14": "42103", "15": "42103", "16": "210013",
             "17": "400011", "18": "1000201", "19": "2000047", "20": "4000011", "21": "10000005", "22": "20000003",
             "23": "40000041", "24": "100000207", "25": "200000011", "26": "400000107", "27": "1000000047",
             "28": "2000000011", "29": "4000000005", "30": "10040000007", "31": "20000000011", "32": "40020000007",
             "33": "100000020001", "34": "201000000007", "35": "400000000005", "36": "1000000004001"}


def initiation():
    global FIELD_POWER
    global ZERO_POLY
    st = input("Write a field power")
    aux = int(FIELD_POW.get(st), 8)
    FIELD_POWER = binary(aux)

def binary(A):
    A = A.replace('d', '')
    A = int(A)
    Cx = []
    s = ''
    while (A > 0):
        Cx.insert(0, A % 2)
        A //= 2
    for i in range(len(Cx)):
        s += str(Cx[i])
    power = int(FIELD_POWER)
    s = s.zfill(power)
    return s

#Для ввода десятичного числа начинайте с символа "d" пример: "d10110"


def add(firstnumber, secondnumber):  # сложение 2-х элементов
    power = int(FIELD_POWER)
    if firstnumber.find('d') != -1:
        firstnumber = binary(firstnumber)
        firstnumber = int(firstnumber, 2)
    else:
        firstnumber = int(firstnumber, 2)  #преобразование строк в числа)

    if secondnumber.find('d') != -1:
        secondnumber = binary(secondnumber)
        secondnumber = int(secondnumber, 2)
    else :
        secondnumber = int(secondnumber, 2)

    res = firstnumber ^ secondnumber #операция xor
    res = int(res)
    res = bin(res) #преобразование числа в 2ичную строку
    res = res.replace('b', '') # удаление вспомогательного обозначения
    res = res.zfill(power) #заполнение число 0 если оно меньше степени поля

    return res  # Возвращает строку


def multiply(firstnumb, secondnumb): #умножение двух чисел принимает строки
    power = int(FIELD_POWER)
    if firstnumb.find('d') != -1:
        firstnumb = binary(firstnumb)
    if secondnumb.find('d') != -1:
        secondnumb = binary(secondnumb)

    numb1 = np.zeros(power, dtype=int) # создание вспомогательного массива с 0
    n = 0
    for var in firstnumb: #заполнение массива 1 числом
        numb1[n] = int(var)
        n += 1
    numb2 = np.zeros(power, dtype=int) # создание вспомогательного массива
    m = 0
    for var in secondnumb: #заполнение массива 2 числом
        numb2[m] = int(var)
        m += 1
    solve = np.zeros((power, (power*2)-1), dtype=int) #содание вспомогательной матрицы
    result = np.zeros((power*2)-1, dtype=int)#создание вспомогательного массива

    i=((power*2)-1)-power
    z=0
    b=0
    for element in numb1:#заполнение матрицы для умножения
        if element == 1:
            for elem in numb2:
                solve[i][b+z] = elem
                b = b+1
            i = i-1
            z = z+1
        elif element == 0:
            i = i-1
            z = z+1

    summ = 0
    for indx in range((power*2)-1): #считаю значения в каждую ячейку
        for indx1 in range(power):
            summ = summ + solve[indx1][indx]
        result[indx] = summ % 2

    stringres = ''
    for var in range((power*2)-1):#преобразование массива в строку
        stringres = stringres+str(result[var])

    if stringres.find('1', 0, power-1) != -1:# проверка на принадлежность поля
     stringres = add(stringres, ZERO_POLY)# операция сложения с неприводимым полиномом если элемент не в поле

    return stringres #Возвращает строку после проверки на принадлежность полю


def inverse_poly(number):#нахождение обратного члена
    result = multiply(number, number)
    for i in range(int(FIELD_POWER)-2):
        result = multiply(number, result)
    return result


def division(number1, number2): #деление
    auxiliary = inverse_poly(number2)
    result = multiply(number1, auxiliary)
    return result


def subtraction(number1, number2): #вычитание
    auxiliary = inverse_poly(number2)
    result = add(number1, auxiliary)
    return result
#print(add("d5", "d7"))














