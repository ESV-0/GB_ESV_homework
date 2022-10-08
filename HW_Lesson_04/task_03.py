"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через timeit
Обязательно предложите еще свой вариант решения!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!

def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)

def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num

def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num """

from timeit import timeit
from random import randint

def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)

def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num

def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

def revers_4(enter_num):
    enter_num = str(enter_num)
    revers_num = reversed(enter_num)
    return revers_num

enter_num = randint(100000000, 1000000000)

print('Обратное число при рекурсивной функции: ', timeit(f'revers({enter_num})', globals=globals()))
print('Обратное число при использовании цикла: ', timeit(f'revers_2({enter_num})', globals=globals()))
print('Обратное число через срез строки:       ', timeit(f'revers_3({enter_num})', globals=globals()))
print('Обратное число через реверс строки:     ', timeit(f'revers_4({enter_num})', globals=globals()))

'''
Итоговые замеры:
ООбратное число при рекурсивной функции:  1.6652788000064902
Обратное число при использовании цикла:  1.062066699960269
Обратное число через срез строки:        0.2374518999713473
Обратное число через реверс строки:      0.21502579998923466

Вызов рекурсивной функции и использование цикла занимает больше времени,
чем использование среза или реверса строки.Оптимальный метод - использование реверса строки поскольку
его асимптотическаяя сложность - О(n), а у присвоения среза - О(k+n)
'''
