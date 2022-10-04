""""
Задание 1.	Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна
запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""

def arithmetic_operations():
    operation = input('Введите (+, -, *, / или 0 для выхода): ')
    if operation not in ['+', '-', '*', '/', '0']:
        print('Неправильное значение!')
        return arithmetic_operations()
    if operation == '0':
        return 0
    first_number = input('Введите первое число: ')
    if first_number.isdigit():
        first_number = int(first_number)
    else:
        print('Введено не число. Необходимо исправить')
        return arithmetic_operations()
    second_number = input('Введите второе число: ')
    if second_number.isdigit():
        second_number = int(second_number)
    else:
        print('Введено не число. Необходимо исправить')
        return arithmetic_operations()
    if operation == '/' and second_number == 0:
        print('Деление на ноль!')
        return arithmetic_operations()
    if operation == '+':
        result = first_number + second_number
        print(f'Результат: {result}')
        return arithmetic_operations()
    if operation == '-':
        result = first_number - second_number
        print(f'Результат: {result}')
        return arithmetic_operations()
    if operation == '*':
        result = first_number * second_number
        print(f'Результат: {result}')
        return arithmetic_operations()
    if operation == '/':
        result = first_number / second_number
        print(f'Результат: {result}')
        return arithmetic_operations()

if __name__ == '__main__':
    print(arithmetic_operations())