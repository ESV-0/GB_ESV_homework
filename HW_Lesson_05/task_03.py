"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list
Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее
2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее
3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее
Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""
from collections import deque
from timeit import timeit

def sep():
    print("_" * 20)

lst = [i for i in range(1000)]
deq_lst = deque(lst)
"""
1) Сравнение операций append, pop, extend списка и дека
"""
def append_lst(lst):
    for i in range(100):
        lst.append(i)
    return lst

def append_deq_lst(deq_lst):
    for i in range(100):
        deq_lst.append(i)
    return deq_lst

def pop_lst(lst):
    for i in range(10000):
        lst.pop(i)
    return lst

def pop_deq_lst(deq_lst):
    for i in range(10000):
        deq_lst.pop()
    return deq_lst

def extand_lst(lst, lst_2):
    for i in range(100):
        lst.extand(lst_2)
    return lst

def extand_deq_lst(deq_lst, deq_lst_2=deque()):
    for i in range(100):
        deq_lst.extand(deq_lst_2)
    return deq_lst

print(timeit("append_lst", globals=globals()))
print(timeit("append_deq_lst", globals=globals()))
print(timeit("pop_lst", globals=globals()))
print(timeit("pop_deq_lst", globals=globals()))
print(timeit("extand_lst", globals=globals()))
print(timeit("extand_deq_lst", globals=globals()))
"""
Вывод: функции append, pop, extend по времени работают однаково у дек и списка.
"""
sep()
"""
2) Сравнение операций appendleft, popleft, extendleft дека и соответствующих им операций списка
"""

def insert_lst(lst):
    for i in range(1000):
        lst.insert(0, i)
    return lst

def appendleft_deq_lst(deq_lst):
    for i in range(1000):
        deq_lst.appendleft(0, i)
    return deq_lst

def popleft_lst(lst):
    for i in range(1000):
        lst.pop(i)
    return lst

def popleft_deq_lst(deq_lst):
    for i in range(1000):
        deq_lst.popleft()
    return deq_lst

def extendleft_lst(lst, lst_2):
    for i in range(1000):
        for i in lst_2:
            lst.insert(0, i)
        return lst_2

def extendleft_deq_lst(deq_lst):
    for i in range(1000):
        deq_lst.extendleft(i)
    return deq_lst

print(timeit("insert_lst", globals=globals()))
print(timeit("appendleft_deq_lst", globals=globals()))
print(timeit("popleft_lst", globals=globals()))
print(timeit("popleft_deq_lst", globals=globals()))
print(timeit("extendleft_lst", globals=globals()))
print(timeit("extendleft_deq_lst", globals=globals()))
"""
Вывод: исполнение операции дека popleft, extendleft производится
быстрей, чем соответствующие операций списка. У операция appendleft наоборот
список быстрее.
"""
sep()
"""
3) Сравнение операций получения элемента списка и дека
"""

def el_from_lst(x):
    for i in range(len(lst)):
        lst[i] = x
    return x

def el_from_deq_lst(x):
    for i in range(len(deq_lst)):
        deq_lst[i] = x
    return x

print(timeit("el_from_lst", globals=globals()))
print(timeit("el_from_deq_lst", globals=globals()))
"""
Вывод: извлечение элемента быстрей происходит из списка, чем из дека.
"""
"""
0.01796600001398474
0.018002500059083104
0.021395399933680892
0.017797400010749698
0.018692099954932928
0.01869309996254742
____________________
0.017913300078362226
0.018770200083963573
0.017920600017532706
0.017642199993133545
0.01872129994444549
0.021233399980701506
____________________
0.018211100017651916
0.01721909991465509
"""