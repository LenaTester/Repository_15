import json
from http import HTTPStatus

from requests import get, post

from pythonProject.Repository_3.restapi_lesson.utilities.config import config
from pythonProject.Repository_3.restapi_lesson.api.users_api import UsersApi
from pythonProject.Repository_3.restapi_lesson.class_object.user_data_class import User

def test_get_user_response():
    '''get all users list - 200 - 4'''
    response = get(f"{config['base_url']}/api/users?page=2")
    assert response.reason == 'OK'
    assert response.status_code == HTTPStatus.OK, f'\nStatus code is not as expected\nActual: {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.OK}'

def test_not_found_error():
    '''get all users list -wrong url - 404 - 5'''
    response = get(f"{config['base_url']}/wjhwht")
    assert response.status_code == HTTPStatus.NOT_FOUND, f'\nStatus code is not as expected' \
                                                         f'\nActual: {response.status_code}' \
                                                         f'\nExpected: {HTTPStatus.NOT_FOUND}'

def test_response_json(create_user):
    '''check, if new user equals to fixture user - 6'''
    response = UsersApi().get_user(user_id=8)
    json_user = json.loads(response.text)['data']
    expected_user = create_user
    actual_user = User(json_user['email'], json_user['first_name'], json_user['last_name'])
    assert actual_user == expected_user, f"\nPerson is not as expected"

