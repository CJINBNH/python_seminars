# Первый семинар

# Вывод квадрата числа

# print(int(input('Введите число: ')**2))

# Проверить является ли чмсло a квадратом числа b

# a = int(input())
# b = int(input())
# if a ** 2 == b:
#     print('yes')
# else:
#     print('no')

# Обратный вариант

# a = int(input())
# b = int(input())
# if a**2 == b or b**2 == a:
#     print('yes')
# else:
#     print('no')

# Введение переменных с помощью списка

# c = input().split()
# a = int(c[0])
# b = int(c[1])
# if a**2 == b or b**2 == a:
#     print('yes')
# else:
#     print('no')

# На вход принимаем 5 чисел и находим максимальное из них

# a = int(input())
# max = a

# for i in range(4):
#     b = int(input())
#     if b > max:
#         max = b
# print(max)

# Тоже решение с помощью списка

# a = list(map(int,input().split()))
# maximum = max(a)
# print(maximum)

# коротко

# print(max(list(map(int,input().split()))))

# Задача написать программу, которая выводит числа от -N до N

# Решение с циклом while

# N = int(input())
# i = -N
# while i <= N:
#     print(i)
#     i +=1

# С помощью range

# N = int(input())
# mass = []
# for i in range(-N,N+1,1):
#     mass.append(i)
# print(mass)

# Написать программу, которая принимает на вход дробное число, и выводит цифру из позиции десятых долей
# 1.23 -> 2

# print('Введите дробное число: ')
# a = float(input())
# b = int(a * 10) % 10
# print(b)

# второй вариант решения, через индекс элемента строки

# a = str(float(input())
# print(a[a.find('.') + 1])

# Программа принимает число и проверяет кратность этого числа 5, 10, 15, но не 30

# a = int(input())
# if a % 5 == 0 and (a % 10 == 0 or a % 15 == 0) and a % 30 != 0:
#     print('Ok')
# else: print('Error')

