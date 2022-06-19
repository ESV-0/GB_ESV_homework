# Домашнеее задание, урок-6, задание-1

import requests
import json
nginx_logs = str(requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs').text)
with open('C:/Users/emplo/Desktop/GB_ESV_homework/lesson_6/nginx_logs.txt', 'w+', encoding='utf-8') as file:
    file.writelines(nginx_logs)
file.close()
with open('C:/Users/emplo/Desktop/GB_ESV_homework/lesson_6/nginx_logs.txt', encoding='utf-8') as file:
    lfile = list(file)
file.close()

for i in range(len(lfile)):
    remote_addr = []
    request_type = []
    requested_resource = []
    lfile_str = list(lfile[i])
    i = 0
    while lfile_str[i] != ' ':
       remote_addr.append(lfile_str[i])
       i += 1
    remote_addr = "".join(remote_addr)

    for i in range(i + 35, i + 39):
        request_type.append(lfile_str[i])
    request_type = "".join(request_type)

    for i in range(i + 2, i + 22):
        requested_resource.append(lfile_str[i])
    requested_resource = "".join(requested_resource)

    print(remote_addr, ' ', request_type, ' ', requested_resource)