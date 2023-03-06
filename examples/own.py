import json

import pytest
import requests
import logging
from assertpy import assert_that

logger = logging.getLogger('Our_logger')


url = 'https://jsonplaceholder.typicode.com/posts/1'

response = requests.get(url).json()               # отправили запрос на указанній url

print(response)

# logger.warning(f'{response}')

# login = 'admin'
# pwd = 'admin123'
#
# @pytest.fixture(autouse=True, scope='module')
# def change_data():
#     return {}
#
#
# def test_get(change_data):
#     response = requests.get(url)
#     assert response.text == '{"users":"https://www.aqa.science/users/",' \
#                             '"groups":"https://www.aqa.science/groups/"}'
#
#     data = response.json()
#     logger.info(f'json converted to internal {type(data)}')
#     assert_that(data).contains_key('users', 'groups')
#     change_data.update(data)
#
#     # users_link = data['users']                 # we have got link for users
#     # groups_link = data['groups']                # we have got link for groups
#     # change_data['user_link'] = users_link
#     # print(users_link, groups_link)
#
# def test_get_users(change_data):
#     user_link = change_data['users']
#     response = requests.get(user_link, auth=(login, pwd))
#
#     # проверяем что в нашем респонсе json содержаться ключи:'count', 'next', 'previous', 'result'
#     assert_that(response).contains_key('count', 'next', 'previous', 'result')
#     print(response)
#
#
# def test_get_users_2(change_data):           # проверяем есть ли 2 страница next_url
#     next_url = 'https://www.aqa.science/users/?page=2'
#     expected_keys = ['count', 'next', 'previous', 'result']
#     response = requests.get(next_url, auth=(login, pwd))
#     assert_that(response).contains_key(*expected_keys)
#
#     with open('result.json', 'w+') as f:           # проверяем что в файле result.json находятся все пользователи на второй странице, ищем нашего
#         json.dump(response, f)
#
#
# def test_post_users(change_data):           # создаем пользователя
#     post_data = {
#             "username": "new_test_user",
#             "email": "tester.com",
#             "groups": []
#     }
#     user_link = change_data["users"]
#     response = requests.post(user_link, post_data, auth=(login, pwd)).json()  # ответ который пришел при создании юзера
#     created_user_url = response['url']    # создаем переменную которая равна url созданноого юзера в post запросе
#     change_data['created_user_url'] = created_user_url           # передаем url
#
#     with open("result.json", "w+") as f:
#         json.dump(response, f)
#
#
# def test_delete_users(change_data):  # удаляем пользователя
#     post_data = {
#         "username": "new_test_user",
#         "email": "tester.com",
#         "groups": []
#     }
#     user_link = change_data['created_user_url']
#     response = requests.delete(user_link,  auth=(login, pwd))
#
#     print(response.text)