# Домашнеее задание, урок-3, задание-5

import random

nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
adjectives = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']

def get_jokes(n):
    """Функция get_jokes(), возвращает n шуток, сформированных из трех случайных слов,
       взятых из трёх списков (по одному из каждого)"""
    for i in range(n):
        Ri_0 = random.choice(nouns)
        Ri_1 = random.choice(adverbs)
        Ri_2 = random.choice(adjectives)
        joke = (Ri_0, Ri_1, Ri_2)
        print(joke)
get_jokes(2)
