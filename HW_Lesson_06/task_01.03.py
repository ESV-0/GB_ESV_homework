from json import loads, dumps
from random import randint
from memory_profiler import memory_usage

def memory_decor(func):
    def wrapper(*args):
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f'Выполнение функции {func.__name__} заняло {mem_diff} Mib')
        return res
    return wrapper

data_storage = {
    "Rambler": 6713661,
    "Wildberries": 3671650226,
    "Oz": 3254165,
    "Yandex": 3541066,
    "Gazprom": 682654,
    "R": 6871466,
    "Marvel": 6574416,
    "Softline": 75169159,
    "HP": 1489905,
    "Rostelecom": 14587125,
    "Kasp": 459665497,
    "Cis": 78945613,
    "Sytronics Group": 123852963,
    "Umbrella": 7418529633,
    "Tegrus": 987456321,
    "Allegro": 369852147,
    "Inv": 4561258,
    "Fl": 32547861,
    "Oil": 45876321,
    "WorldP": 78254122
}
@memory_decor
def winners(data_dict):
    top_3 = {}
    data_copy = data_dict.copy()
    for _ in range(3):
        max_value = 0
        max_key = 0
        for key in data_copy.keys():
            if data_copy[key] > max_value:
                max_value = data_copy[key]
                max_key = key
        top_3[max_key] = max_value
        data_copy.pop(max_key)
    return top_3
"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    71     19.3 MiB     19.3 MiB           1   @profile()
    72                                         def winners(data_dict):
    73     19.3 MiB      0.0 MiB           1       top_3 = {}
    74     19.3 MiB      0.0 MiB           1       data_copy = data_dict.copy()
    75     19.3 MiB      0.0 MiB           4       for _ in range(3):
    76     19.3 MiB      0.0 MiB           3           max_value = 0
    77     19.3 MiB      0.0 MiB           3           max_key = 0
    78     19.3 MiB      0.0 MiB          60           for key in data_copy.keys():
    79     19.3 MiB      0.0 MiB          57               if data_copy[key] > max_value:
    80     19.3 MiB      0.0 MiB          10                   max_value = data_copy[key]
    81     19.3 MiB      0.0 MiB          10                   max_key = key
    82     19.3 MiB      0.0 MiB           3           top_3[max_key] = max_value
    83     19.3 MiB      0.0 MiB           3           data_copy.pop(max_key)
    84     19.3 MiB      0.0 MiB           1       return top_3
{'Umbrella': 7418529633, 'Wildberries': 3671650226, 'Tegrus': 987456321}
"""

@memory_decor
def winners_json(data_json):
    top_3 = {}
    data_dict = loads(data_json)
    for _ in range(3):
        max_value = 0
        max_key = 0
        for key in data_dict.keys():
            if data_dict[key] > max_value:
                max_value = data_dict[key]
                max_key = key
        top_3[max_key] = max_value
        data_dict.pop(max_key)
    del data_dict
    return dumps(top_3)
"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    87     19.3 MiB     19.3 MiB           1   @profile()
    88                                         def winners_json(data_json):
    89     19.3 MiB      0.0 MiB           1       top_3 = {}
    90     19.3 MiB      0.0 MiB           1       data_dict = loads(data_json)
    91     19.3 MiB      0.0 MiB           4       for _ in range(3):
    92     19.3 MiB      0.0 MiB           3           max_value = 0
    93     19.3 MiB      0.0 MiB           3           max_key = 0
    94     19.3 MiB      0.0 MiB          60           for key in data_dict.keys():
    95     19.3 MiB      0.0 MiB          57               if data_dict[key] > max_value:
    96     19.3 MiB      0.0 MiB          10                   max_value = data_dict[key]
    97     19.3 MiB      0.0 MiB          10                   max_key = key
    98     19.3 MiB      0.0 MiB           3           top_3[max_key] = max_value
    99     19.3 MiB      0.0 MiB           3           data_dict.pop(max_key)
   100     19.3 MiB      0.0 MiB           1       del data_dict
   101     19.3 MiB      0.0 MiB           1       return dumps(top_3)
{"Umbrella": 7418529633, "Wildberries": 3671650226, "Tegrus": 987456321}
"""

for i in range(1000000):
    data_storage[i] = randint(10000000, 10000000000)
data_dump = dumps(data_storage)
print(winners(data_storage))
print(winners_json(data_dump))
"""
Оптимизировали использовние памяти с помощью сериализации и удаления ссылки на словарь
"""