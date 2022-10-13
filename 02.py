
# Задача: предложить улучшения кода для уже решённых задач:

# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension


# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

## БЫЛО!!!

# import random

# n = int(input('Введите размер списка: '))
# line1 = []
# line2 = []
# for i in range(n):
#     line1.append(random.randint(0,10))

# if len(line1) % 2 == 0:
#     l = int((len(line1) / 2))
# else:
#     l = int((len(line1)/2)+1)

# for i in range(l):
#     line2.append(line1[i]*line1[-(i+1)])

# print(line1)
# print(line2)

## СТАЛО!!!

def pairs_multiplication(array):
    length = len(array)
    iterations = length // 2 + length % 2
    return [array[i] * array[-i - 1] for i in range(iterations)]


new_list = [2, 3, 4, 5, 6]
print(pairs_multiplication(new_list))