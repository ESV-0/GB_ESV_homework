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
1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)
сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
""" Сортировка Шелла. """
from random import randint
from timeit import timeit

def shell(seq):
    inc = len(seq) // 2
    while inc:
        for i, el in enumerate(seq):
            while i >= inc and seq[i - inc] > el:
                seq[i] = seq[i - inc]
                i -= inc
            seq[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return seq

m = 10
orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]

print(f'{shell(orig_list)}')
print(f'Медиана: {orig_list[m]}')
# замеры 10
print(
    timeit(
        "shell(orig_list[:])",
        globals=globals(),
        number=1000))
m = 100
orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'{shell(orig_list)}')
print(f'Медиана: {orig_list[m]}')
# замеры 100
print(
    timeit(
        "shell(orig_list[:])",
        globals=globals(),
        number=1000))

m = 1000
orig_list = [randint(-100, 100) for _ in range(2 * m + 1)]
print(f'{shell(orig_list)}')
print(f'Медиана: {orig_list[m]}')
# замеры 1000
print(
    timeit(
        "shell(orig_list[:])",
        globals=globals(),
        number=1000))
"""
Результаты тестов.
(m = 10)
0.005603799945674837
(m = 100)
0.10253240005113184
(m = 1000)
1.6654475999530405
"""