import requests
import json
import time
from pprint import pprint

token = 'OibeOusbQhWE'
region = 50
firstname = 'Епихин'
secondname = 'Андрей'
lastname = 'Владимирович'
birthdate = '13.12.1997'
url = 'https://api-ip.fssp.gov.ru/api/v1.0/'
task_list = []

def fisical(): # Проверка ФЛ
        params = {'token': token, 'birthdate': birthdate, 'firstname': firstname,'lastname': lastname,
                  'region': region,'secondname': secondname}
        response = requests.get(url + 'search/physical', params=params).json()
        task = response['response']['task']
        # time.sleep()
        task_list.append(task)

def status(task): # Запрос статуса
    params = {'token': token, 'task': task}
    status = requests.get(url + 'status', params=params).json()
    task = status['response']['status']
    return task

def result(task): # Запрос результата
    params = {'token': token, 'task': task}
    result = requests.get(url + 'result', params=params).json()
    pprint(result)

def check_status(task): # Проверка статуса
    if status(task) == 0:
        print('обработка завершена, можно получить результаты')
        result(task)
    elif status(task) == 1:
        print('обработка начата, можно получить частичные результаты группового запроса')
    elif status(task) == 2:
        print('обработка не начиналась, запрос находится в очереди')
    elif status(task) == 3:
        print('обработка завершена, имели место ошибки, с помощью метода /result можно получить частичные результаты')

def group_all_region(): # Групповой запрос
    data_list = all_region()
    task_list = []
    a = data_list[:49]
    b = data_list[49:]
    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
    data = {"token": token, "request": a}
    data_1 = {"token": token, "request": b}
    response = requests.post('https://api-ip.fssp.gov.ru/api/v1.0/search/group', headers=headers, data=data)
    time.sleep(5)
    response_1 = requests.post('https://api-ip.fssp.gov.ru/api/v1.0/search/group', headers=headers, data=data_1)
    task_list.append(response)
    task_list.append(response_1)
    return task_list


def all_region(): # Создание списка для группового запроса
    group_list = []
    reg = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
         31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58,
         59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 82, 86, 89, 92]
    for region_number in reg:
        group_data = {"type": 1, "params": {"firstname": firstname, "lastname": lastname, "secondname": secondname,
                                            'region': region_number, "birthdate": birthdate}}
        group_list.append(group_data)
    return group_list


# group_all_region()
# print(all_region())


# all_city()
# check_status()
# fisical()
# print(check_status("bab6863a-6974-4f86-b019-0e51fc79b7ae"))
# #result(fisical())
# print(task_list)
# time.sleep(5)
# print(status(a))
# group()
