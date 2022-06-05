# Домашнеее задание, урок-6, задание-1
# -*- coding: utf-8 -*-

with open('C:/Users/emplo/Desktop/GB_ESV_homework/lesson_6/users.csv', encoding='utf-8') as users:
    lusers = list(users)
users.close()
with open('C:/Users/emplo/Desktop/GB_ESV_homework/lesson_6/hobby.csv', encoding='utf-8') as hobby:
    lhobby = list(hobby)
hobby.close()

users_and_hobby = {}
for i in range(0, len(lusers)):
    users_and_hobby[lusers[i]] = lhobby[i]

with open('C:/Users/emplo/Desktop/GB_ESV_homework/lesson_6/users_and_hobby.csv', 'w', encoding='utf-8') as savedict:
    savedict.writelines(str(users_and_hobby))
savedict.close()


