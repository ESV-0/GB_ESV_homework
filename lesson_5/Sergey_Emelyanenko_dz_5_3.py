# Домашнеее задание, урок-5, задание-3

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

dict_sum = { tut: kla for tut, kla in zip(tutors, klasses) if len(tutors) <= len(klasses)}
print(dict_sum)