# Разбор ДЗ
# Задача №2

# from sympy import isprime

# def dev_for_primes(a):
#     primeList = []
#     for i in range(2, a):
#         if a % i == 0:
#             while a % i == 0:
#                 primeList.append(i)
#                 a //= i
#     return primeList
# a = int(input())
# print(dev_for_primes(a))

# Задача №4

# import random
# def gen_pol(n):
#     polinom = ''
#     for i in range(n + 1):
#         if i == 0:
#             polinom += str(random.randint(1, n)) + '*x**' + str(n - i)
#         elif i == n:
#             polinom += '+' + str(random.randint(1, n))
#         else:
#             polinom += '+' + str(random.randint(1, n)) + '*x**' + str(n - i)
#     polinom += ' = 0'
#     return polinom
# n = int(input())
# with open("generatedpol.txt", "w") as f:
#     f.write(gen_pol(n))
# print(gen_pol(n))

# Задача №5

# import sympy as sp
# x = sp.Symbol('x')
# with open("pol1.txt", "r") as pol1:
#     a = pol1.read()
# print(a)
# with open("pol2.txt", "r") as pol2:
#     b = pol2.read()
# print(b)
# c = sp.simplify(a+'+'+b)
# with open("text.txt", "w") as f:
#     f.write(str(c))
# print(c)

# Задачи семинара
# Задача №1 В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# Пример:
# Ввод: 1 2 4 5 -> 3

# with open("seminar5.txt", "r") as sm5:
#     a = sm5.read()
# print(a)
# listNum = [int(i) for i in a.split()]
# b = []
# for i in range(1, len(listNum)):
#     if listNum[i - 1] != listNum[i] - 1:
#         b.append(listNum[i] - 1)
# print(f'{b} пропущенные в последовательности числа')

# решение с помощью методов

# берем список значений из файла и преобразуем в числовой
# def getData(nums):
#     data = open(nums, 'r')
#     list1 = data.read()
#     list1 = list(map(int, list1.split()))
#     data.close()
#     return list1
# def findNum(nums):
#     for i in nums:
#         print(len(nums))
#         if nums[i + 1] - nums[i] == 1:
#             print(nums[i])
#         else:
#             print(nums[i])
#             return nums[i] + 1
# fnums = 'seminar5.txt'
# list2 = getData(fnums)
# print(list2)
# print(findNum(list2))

# Задача №2 Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую
# последовательность. Порядок элементов менять нельзя.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

# condList = [1, 5, 2, 3, 4, 6, 1, 7]
# print(condList)
# for i in range(len(condList)):
#     resList = []
#     if condList[i - 1] < condList[i]:
#         resList.append(condList[i])
#     else:
#         continue
# print(resList)

# решение с помощью метода

# condList = [1, 5, 2, 3, 4, 6, 1, 7]
# def getUp(list):
#     upList = []
#     for i in range(len(list)):
#         if list[i] == max(list[:i+1]) and list[i] not in upList:
#             upList.append(list[i])
#     return upList
# print(getUp(condList))

# Задача №3 Напишите программу, удаляющую из текста все слова, содержащие "абв".
# Пример: абв абвгд гдеёжз непшщтг -> гдеёжз непшщтг

# textStr = 'абв абвгд гдежз непшщзй'
# def delWords(str1):
#     str1 = list(filter(lambda x: 'абв' not in x, str1.split()))
#     return " ".join(str1)
# textStr = delWords(textStr)
# print(textStr)