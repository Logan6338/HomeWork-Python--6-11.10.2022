
# Задача: предложить улучшения кода для уже решённых задач:

# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension


# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

## БЫЛО !!!

# import random

# n = int(input('Введите размер списка: '))
# line = []
# sum = 0
# for i in range(n):
#     line.append(random.randint(0,10))
#     if i % 2 != 0:
#         sum = sum + line[i]
# print(line)
# print(f'Сумма = {sum}')

## СТАЛО !!!

def sum_odd(arr):
    return sum([item for index, item in enumerate(arr) if index % 2 == 1])


new_list = [2, 3, 5, 9, 3]
print(sum_odd(new_list))