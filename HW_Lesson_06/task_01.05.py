from random import randint
from collections import Counter
from memory_profiler import memory_usage
"""
Необходимо найти число, которое встречается в массиве чаще всего
"""
def memory_decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(*args, **kwargs)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f'Выполнение функции {func.__name__} заняло {mem_diff} Mib')
        return res
    return wrapper

@memory_decor
def func_3(arr):
    max_count_elem = max(arr, key=arr.count)
    max_count = arr.count(max_count_elem)
    return f'Число {max_count_elem} встречается чаще всего: {max_count} раз(а)'

@memory_decor
def count_num(arr):
    return Counter(arr).most_common(1)

array = [3, 1, 1, 3, 4, 5, 1]
for i in range(10000):
    array.append(randint(0, 20))
print(func_3(array))
print(count_num(array))
"""
Выполнение функции func_3 заняло 0.0078125 Mib
Число 6 встречается чаще всего: 504 раз(а)
Выполнение функции count_num заняло 0.0 Mib
[(6, 504)]
Решение оптимизировано с помощью класса Counter из модуля collections.
"""