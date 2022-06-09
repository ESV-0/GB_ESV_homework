# Домашнеее задание, урок-6, задание-6.1
def add(x, y):
    with open('C:/Users/emplo/Desktop/GB_ESV_homework/lesson_6/bakery.csv', encoding='utf-8') as f:
        lf = list(f)
        for i in range(x, len(lf)):
            print(lf[i])
    f.close()
add(1, 3)


