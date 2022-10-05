"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет
есть ли в кэше соответствующая страница или нет
Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}
Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш
Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""
from uuid import uuid4
import hashlib
salt = uuid4().hex
# salt = "my_salt"
cache = {}

def my_cache(url):
    my_hash = hashlib.sha512(salt.encode() + url.encode()).hexdigest()
    if cache.get(url):
        print('хеш url-а: ', my_hash)
    else:
        cache[url] = my_hash

my_cache('https://gb.ru/')
my_cache('https://gb.ru/')
my_cache('https://www.yandex.ru/')
my_cache('https://www.yandex.ru/')
print(cache)
