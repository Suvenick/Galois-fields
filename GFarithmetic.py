import numpy as np

FIELD_POWER ="3" #Field power
ZERO_POLY = "1011" #'10000000001000000000000000000111' #здесь должен быть не приводимый элемент поля x^32+x^22+x^2+x+1

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
    Cx = []
    s = ''
    while (A > 0):
        Cx.insert(0, A % 2)
        A //= 2
    for i in range(len(Cx)):
        s += str(Cx[i])
    return s

#Для ввода десятичного числа начинайте с символа "d" пример: "d10110"


def add(firstnumber, secondnumber):  # сложение 2-х элементо
    res = firstnumber ^ secondnumber #операция xor
    return res  # Возвращает строку



def multiplication(firstnumer, secondnumber):
    secondnumber = bin(secondnumber)
    secondnumber = secondnumber[2:]
    secondnumber = secondnumber[::-1]
    aux = len(secondnumber)
    auxila = int(ZERO_POLY, 2)
    i = 0
    x = 0
    res = 0
    while i < aux:
        if secondnumber[i] == '1':
            helps = 0
            if i == 0:
                res = firstnumer
            while x < i:
                firstnumer = firstnumer << 1
                helps = firstnumer
                if firstnumer >= 2 ** int(FIELD_POWER):
                    firstnumer = firstnumer ^ auxila
                    helps = firstnumer
                x += 1
            res = res ^ helps
        i += 1
    return res


def inverse_poly(number):  #нахождение обратного члена
    exponent = int(FIELD_POWER)
    exponent = (2 ** exponent)-2
    result = fast_pow(number, exponent)
    return result


def fast_pow(firstnumber, secondnumber):
    secondnumber = binary(secondnumber)
    print(secondnumber)
    result = 1
    aux = len(secondnumber)
    for i in secondnumber[:aux-1]:
        a = 1
        print(a)
        a += 1
        if i == '1':
            result = multiplication(result, firstnumber)
            result = multiplication(result, result)
        else:
            result = multiplication(result, result)
    if secondnumber[aux-1] == '1':
        result = multiplication(result, firstnumber)
    return result


def division(number1, number2): #деление
    auxiliary = inverse_poly(number2)
    result = multiplication(number1, auxiliary)
    return result


def subtraction(number1, number2): #вычитание
    auxiliary = inverse_poly(number2)
    result = add(number1, auxiliary)
    return result


