"""
Задание 3
Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

"""
# вариант O(n Log n)
def sorted_1(company):
    list_from_dict = list(company.items())
    list_from_dict.sort(key = lambda i: i[1], revers = True)
    for i range(2):
        print(f"{list_from_dict[i][0]}: {list_from_dict[i][1]})

# вариант O(n)
def sorted_2(company):
    input_max = {}
    list_d = dict(company)
    for i range(2):
        maximum = max(list_d.items(), key = lamda k_v: k_v[1])
        del list_d[maximum[0]]
        input_max[maximum[0]] = maximum[1]
    print(input_max)

sorted_1(company)
sorted_2(company) # Лучший вариант
    
