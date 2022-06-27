# Домашнеее задание, урок-8, задание-3
from functools import wraps

def type_logger(func):
    @wraps(func)
    def wrapper(arg):
        print(f'{func.__name__}({arg}: {type(arg)})')
    return wrapper
@type_logger
def calc_cube(x):
   return x ** 3

print(calc_cube(5))

