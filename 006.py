# Задача №1 Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# Пример:
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;

# print(eval(input('Введите арифметическое выражение: ')))


# arith = list(arithStr)
# for i in range(len(arith)):
#     if arith[i] == '+':
#         arith[i] = 1
#     elif arith[i] == '-':
#         arith[i] = 2
#     elif arith[i] == '*':
#         arith[i] = 3
#     elif arith[i] == '/':
#         arith[i] = 4
#     else:
#         arith[i] = int(arith[i])
# print(arith)
    # if type(i) == int:
    #     a = i
    #     print(a)
    # elif type(i) == float:
    #     b = i
    #     print(b)
    # else:
    #     print('ошибка')

# Задача №2 Дана последовательность чисел. Получить список уникальных элементов
# заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

# data = [1, 2, 3, 5, 1, 5, 3, 10]
# data = list(map(int, input().split()))
# print(set(data)) - код убирает повторяющиеся элементы
# res = list(filter(lambda i: data.count(i) == 1, data))
# print(res)

# Задача №3 Цифровой корень - это рекурсивная сумма всех цифр числа.
# Учитывая n, возьмите сумму цифр n. Если это значение имеет более одной цифры,
# продолжайте уменьшать
# Примеры:
# 16 --> 1+6=7
# 942 --> 9+4+2=15 --> 1+5=6

num = int(input('Введите число: '))
# calc = 0
# while num != 0:
#     calc += num % 10
#     num = num // 10
# print(calc)

# def summ(num):
#     if num < 10:
#         return num
#     else:
#         return summ(sum(map(int, list(str(num)))))
# print(summ(num))

def calc(num):
    plus = 0
    for i in str(num):
        plus += int(i)
    return plus

def summ(num):
    if num < 10:
        return num
    else:
        return summ(calc(num))
print(summ(num))