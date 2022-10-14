
from memory_profiler import memory_usage
from numpy import array

def memory_decor(func):
    def wrapper(*args):
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f'Выполнение функции {func.__name__} заняло {mem_diff} Mib')
        return res
    return wrapper

@memory_decor
def even_id(nums):
    """Сохранение индексов четных элементов list comprehensions"""
    new_arr = [i for i, val in enumerate(nums) if val % 2 == 0]
    return new_arr
"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    37     30.7 MiB     30.7 MiB           1   @profile
    38                                         def even_id(nums):
    39                                             "Сохранение индексов четных элементов list comprehensions"
    40    222.7 MiB     92.2 MiB    10000003       new_arr = [i for i, val in enumerate(nums) if val % 2 == 0]
    41    222.7 MiB      0.0 MiB           1       return new_arr
Выполнение функции even_id заняло 191.8203125 Mib
"""


@memory_decor
def even_id_numpy(nums):
    """Сохранение индексов четных элементов numpy"""
    new_arr = array([i for i, val in enumerate(nums) if val % 2 == 0])
    return new_arr
"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    49    222.7 MiB    222.7 MiB           1   @profile()
    50                                         def even_id_numpy(nums):
    51                                             "Сохранение индексов четных элементов numpy"
    52    413.3 MiB -65529.0 MiB    10000003       new_arr = array([i for i, val in enumerate(nums) if val % 2 == 0])
    53    242.2 MiB   -171.1 MiB           1       return new_arr
Выполнение функции even_id_numpy заняло 20.640625 Mib
"""
num = range(10000000)
lst = even_id(num)
arr = even_id_numpy(num)
"""
использование numpy значительно уменьшило используемую память
"""