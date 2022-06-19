# Домашнеее задание, урок-6, задание-6.1

bakery = input('Введите значение суммы продаж: ')
with open('C:/Users/emplo/Desktop/GB_ESV_homework/lesson_6/bakery.csv', 'a+', encoding='utf-8') as f:
    print(bakery, file=f)
f.close()


