# Домашнеее задание, урок-8, задание-1
import re
def email_parse() :
    email = input('Введите арес почты: ')
    #email = 'emp.logika@bk.ru'
    parn = r'^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$'
    if re.match(parn, email) is not None:
        print('Адрес email корректный')
    else:
        print('ValueError')

    username = re.search('^[\w]+', email)
    domain = re.search('@[\w.]+', email)

    print({'username': username.group(), 'domain': domain.group()})
email_parse()