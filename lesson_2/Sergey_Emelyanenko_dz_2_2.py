# Домашнеее задание, урок-2, задание-2

List_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

el1 = int(List_1[1])
el8 = int(List_1[8])

List_1[1] = str(f'"{el1:02}"')
List_1[3] = str(f'"{List_1[3]}"')
List_1[8] = str(f'"+{el8:02}"')

print(' '.join(List_1))