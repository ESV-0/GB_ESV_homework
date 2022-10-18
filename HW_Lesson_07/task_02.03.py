"""
Задание 2.
Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.
Решите задачу тремя способами:
3) с помощью встроенной функции поиска медианы
сделайте замеры на массивах длиной 10, 100, 1000 элементов
В конце сделайте аналитику какой трех из способов оказался эффективнее
"""
from statistics import median
from timeit import timeit
from random import randint

m = 10
orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]

print(f'Медиана: {median(orig_list[:])}')
# замеры 10
print(
    timeit(
        "median(orig_list[:])",
        globals=globals(),
        number=1000))
m = 100
orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]

print(f'Медиана: {median(orig_list[:])}')
# замеры 100
print(
    timeit(
        "median(orig_list[:])",
        globals=globals(),
        number=1000))

m = 1000
orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]

print(f'Медиана: {median(orig_list[:])}')
# замеры 1000
print(
    timeit(
        "median(orig_list[:])",
        globals=globals(),
        number=1000))

"""

Результаты тестов.
(m = 10)
0.0006401999853551388
(m = 100)
0.00588339997921139
(m = 1000)
0.16467839991673827

"""