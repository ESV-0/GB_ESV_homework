# Домашнеее задание, урок-1, задание-1

duration = int(input('Введите продолжительность в секундах: '))

dn = duration // 86400
hour = (duration - dn * 86400) // 3600
minute = (duration - dn * 86400 - hour * 3600) // 60
sec = (duration % 3600) % 60

result = ['дней  =', dn, 'часов  =', hour, 'минут  =', minute, 'секунд =', sec]

indx = 1
while indx < len(result):
    if result[indx] != 0:
        print(result[indx - 1], result[indx])
    indx += 2
