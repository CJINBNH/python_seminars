# Разбор ДЗ
# Задача №1

# a = input()
# count = 0
# if float(a) < 0:
#     a = str(float(a) * (-1))
# for i in range(len(a)):
#     if a[i] == '.':
#         continue
#     else:
#         count += int(a[i])
# print(count)

# Задача №2

# n = int(input())
# m = 1
# mass = []
# for i in range(1, n+1):
#     m *= i
#     mass.append(m)
# print(mass)

# Задача №3

# n = int(input())
# mass = [(1+1/i)**i for i in range(1, n+1)]
# print(sum(mass))

# Задача №4

# n = int(input())
# mass = [i for i in range(-n, n + 1)]
# mult = 1
# pos = list(map(int,input().split()))
# for i in pos:
#     mult *= mass[i]
# print(mult)

# Задача №5

# import random
# mass = [i for i in range(random.randint(10, 12))]
# print(mass)
# random.shuffle(mass)
# print(mass)

# Задача 1 Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.
# [1,2,3,4,4,5,5,6] -> [1,2,3,6]

# list1 = [1, 2, 3, 4, 4, 5, 5, 6]
# list2 = []
# for i in list1:
#     if list1.count(i) == 1:
#         list2.append(i)
# print(list1)
# print(list2)


# Задача 2 Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке
# строк некое число.
# [''ffff'.'3rfhg','4'] -> YES

# mass = ['asd', 'dfdg', '3poi3', '3v', 'sdfs3e4f']
# result = 'No'
# for i in mass:
#     try:
#         int(i)
#         result = 'Yes'
#         break
#     except:
#         pass
# print(result)

# Задача 3 Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит,
# что её нет.
# Пример:
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

# mass = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
# find_str = 'йцу'
# count = 0
# index = -1
# for i in range(len(mass)):
#     if mass[i] == find_str:
#         count += 1
#         if count == 2:
#             index = i
#             break
# print(index)