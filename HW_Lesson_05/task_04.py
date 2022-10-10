"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
from timeit import timeit

some_dict = {i: i ** 2 for i in range(10000)}
some_ordered = OrderedDict({i: i ** 2 for i in range(10000)})

def change_dict(some_dict_orderdict):
    for i in range(10000):
        some_dict_orderdict[i] = i
    return some_dict_orderdict

def pop_dict(some_dict_orderdict):
    for i in range(10000):
        some_dict_orderdict.pop(i)
    return some_dict_orderdict

print('Замер dict: ', timeit('pop_dict(some_dict.copy())', globals=globals(), number=100))
print('Замер Ordereddict: ', timeit('pop_dict(some_ordered.copy())', globals=globals(), number=100))

print('Удаление dict: ', timeit('pop_dict(some_dict.copy())', globals=globals(), number=100))
print('Удаление Ordereddict: ', timeit('pop_dict(some_ordered.copy())', globals=globals(), number=100))

"""
Замер dict:  0.06992719997651875
Замер Ordereddict:  0.19359069992788136
Удаление dict:  0.07151339994743466
Удаление Ordereddict:  0.18688789999578148

Выполнение операций с dict происходит быстрее чем с Ordereddict. Нет необходимости
использовать OrderedDict в Python 3.6 и более поздних версиях.
"""