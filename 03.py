# Задача: предложить улучшения кода для уже решённых задач:

# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

## БЫЛО!!!!

# import random

# number = 8
# line = []

# for i in range(number):
#     line.append(random.randint(100, 1000)/100)

# max = float(0)
# min = float(1)

# for i in line:
#     if max < i % 1:
#         max = i % 1
#     if min > i % 1:
#         min = i % 1

# print(line)
# print(f'{max-min:.2f}')


#№ СТАЛО!!!

def find_fractional_diff(array):
    fractional_map = map(lambda num: num % 1, array)
    fractional_list = list(filter(lambda x: x != 0, fractional_map))
    fractional_min = min(fractional_list)
    fractional_max = max(fractional_list)
    return round(fractional_max - fractional_min, 2)


new_list = [1.1, 1.2, 3.1, 5, 10.01]
print(find_fractional_diff(new_list))