# Домашнеее задание, урок-1, задание-3

numbs = [11,12,13,14]
for vol in range(100):
    vol += 1
    if vol in numbs:
        print(vol, 'процентов')
    elif vol % 10 == 1:
        print(vol, 'процент')
    elif vol % 10 > 1 and vol % 10 < 5:
        print(vol, 'процента')
    else:
        print(vol, 'процентов')

