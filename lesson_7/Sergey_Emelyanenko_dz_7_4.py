# Домашнеее задание, урок-7, задание-4
import os
os.chdir("C:\\Users\\emplo\\Desktop\\GB_ESV_homework\\lesson_7")

directory = r'some_data'
groups = [100, 1000, 10000, 100000]  # размеры, на какие группы разбивать
groups += [float('inf')]             # последняя группа для меньше бесконечности
result = dict.fromkeys(groups, 0)

for p, s, f in os.walk(directory):  # обходим всё
    for file in f:
        path = os.path.join(p, file)
        size = os.path.getsize(path)

        to_group = min(filter(lambda x: size < x, groups)) # вычисляем ближайшее большее число из groups, куда и посчитаем файл
        result[to_group] += 1

p_size = 0
for size in groups:
    print(f'Размер (байт) от {p_size:10} до {size:10} : {result[size]}')
    p_size = size
