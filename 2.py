import requests
import json
import time
from pprint import pprint
token = 'OibeOusbQhWE'
region = 50
firstname = 'Комарова'
secondname = 'Юлия'
lastname = 'Анатольевна'
birthdate = '12.07.1979'
url = 'https://api-ip.fssp.gov.ru/api/v1.0/'
a = []
def fisical():
    params = {'token': token, 'birthdate': birthdate, 'firstname': firstname,'lastname': lastname, 'region': region,'secondname': secondname}
    response = requests.get(url + 'search/physical', params=params).json()
    task = response['response']['task']
    # time.sleep()
    a.append(task)

def status(task):
    params = {'token': token, 'task': task}
    status = requests.get(url + 'status', params=params).json()
    task = status['response']['status']
    return task
def result(task):
    params = {'token': token, 'task': task}
    result = requests.get(url + 'result', params=params).json()
    pprint(result)

def check_status():
    while status(a) != 0:
        if status(a) == 0:
            print('обработка завершена, можно получить результаты')
            result(a)
        elif status(a) == 1:
            print('обработка начата, можно получить частичные результаты группового запроса')
        elif status(a) == 2:
            print('обработка не начиналась, запрос находится в очереди')
        elif status(a) == 3:
            print('обработка завершена, имели место ошибки, с помощью метода /result можно получить частичные результаты')

# check_status()
fisical()
print(status(*a))
#result(fisical())
print(a)
# time.sleep(5)
# print(status(a))