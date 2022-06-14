# Домашнеее задание, урок-8, задание-4
from functools import wraps

def val_checker(decorator_check_func):
    def val_checker_temp(func_calc_cube):
        @wraps(func_calc_cube)
        def wrapped(x):
            if decorator_check_func(x):
                return func_calc_cube(x)
            else:
                raise ValueError(x)

        return wrapped
    return val_checker_temp

@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

x = calc_cube(5)
print(x)
print(calc_cube.__name__)
