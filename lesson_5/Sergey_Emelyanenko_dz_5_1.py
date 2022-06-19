# Домашнеее задание, урок-5, задание-1

def nums_generator(n):
    for num in range(1, n + 1, 2):
        yield num

num_gen = nums_generator(33)
for i in num_gen:
    print(i)