# Домашнеее задание, урок-4, задание-2

def currency_rates(*args):
    import requests
    import re

    my_st = str(requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text)
    my_st = re.split("<|>|/", my_st)

    valute = str(input('Введите наименование валюты (например, USD, EUR, GBP, ...): '))
    index = my_st.index(valute)
    index_name = index + 10
    index_value = index + 15
    print(f'Курс {valute} ({my_st[index_name]}) равен {my_st[index_value]} Руб.')

currency_rates()