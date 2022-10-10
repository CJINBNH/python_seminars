# Разбор задач из ДЗ

# Задача №1
# создаем список, заполненный случайными числами
# import random
# a = [random.randint(1, 2) for i in range(7)]
# print(a)
# # описываем функцию, выбирающую нечетные позиции списка и суммирующую значения на этих позициях
# def sumOfNum(mass):
#     count = 0
#     for i in range(1, len(mass), 2):
#         count += mass[i]
#     print(count)
# sumOfNum(a)

# Задача №2
# import random
# a = [random.randint(1, 10) for i in range(7)]
# print(a)
# описываем функцию, которая создаст список из произведений крайних элементов начального списка
# def multOfPairs(mass):
#     resMass = []
#     if len(mass) % 2 == 0:
#         for i in range(len(mass) // 2):
#             resMass.append(mass[i] * mass[len(mass) - 1 - i])
#     else:
#         for i in range(len(mass) // 2 + 1):
#             resMass.append(mass[i] * mass[len(mass) - 1 - i])
#     print(resMass)
# multOfPairs(a)

# Задача №3
# Срезы, ищем точку в строке и срезаем все значения после точки

# str = '123.98459'
# f = str.find('.')
# print(int(str[f + 1::]))

# listOfNum = [0.125, 5.205, 44.92, 43]
# def slice(n):
#     fstr = str(n)
#     f = fstr.find('.')
#     fstr = float('0.' + fstr[f + 1::])
#     return fstr
# def diffOfVal(list):
#     resultList = []
#     for i in list:
#         resultList.append(slice(i))
#     print(max(resultList) - min(resultList))
# diffOfVal(listOfNum)

# Задача перевести десятичное число в двоичную систему исчисления

# n = int(input())
# print(str(bin(n))[2::])

# Задачи для решения на семинаре:
# Задача №1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.
# Ввод: 2 3 5 -> 2 5

# def numStr(log = 'Введите строку из чисел, разделенных пробелами'):
#     try:
#         return list(map(int, input(log).split()))
#     except:
#         return numStr('Введены некорректные значения. Повторите ввод: ')
# def getResult(str):
#     return(min(str), max(str))
# nums = numStr()
# print(getResult(nums))

# Задача №2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python(sympy)

# 1)

# def eq(a, b, c):
#     d = b ** 2 - 4 * a * c
#     if d > 0:
#         x1 = (-b + d ** 0.5) / (2 * a)
#         x2 = (-b - d ** 0.5) / (2 * a)
#         print(x1, x2)
#     elif d == 0:
#         x1 = -b / (2 * a)
#         print(x1)
#     else:
#         print('корней нет')
# eq(2, -9, 7)

# sympy

# Задача №3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное)
# этих двух чисел. Ввод 3 , 10 -> 30