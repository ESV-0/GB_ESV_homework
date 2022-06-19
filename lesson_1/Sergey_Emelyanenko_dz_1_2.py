# Домашнеее задание, урок-1, задание-2.a

list_1_2 = []
for el in range(1,1000):
    if el % 2 != 0:
        list_1_2.append(el**3)
sum = 0
for el in list_1_2:
    temporary_list = list(str(el))
    sum_1 = 0
    for el_str in temporary_list:
        sum_1 += int(el_str)
    if sum_1 % 7 == 0:
        sum += el
print(sum)


# Домашнеее задание, урок-1, задание-2.b

list_1_2 = []
for el in range(1,1000):
    if el % 2 != 0:
        list_1_2.append(el**3 + 17)
sum = 0
for el in list_1_2:
    temporary_list = list(str(el))
    sum_1 = 0
    for el_str in temporary_list:
       sum_1 += int(el_str)
    if sum_1 % 7 == 0:
        sum += el
print(sum)
