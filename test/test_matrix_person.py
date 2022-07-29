from http import HTTPStatus

from pythonProject.Repository_3.restapi_lesson.api.matrix_person_api import MatrixPersonApi

def test_post_matrix_person():
    '''post new matrix person - 7'''
    new_matrix_person = {"name": "Morpheus", "job": "leader"}
    response = MatrixPersonApi().post_user(new_matrix_person)
    assert response.reason == 'Created'
    assert response.status_code == HTTPStatus.CREATED, f'\nStatus code is not as expected\nActual: {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.Created}'

def test_update_through_put_matrix_person():
    '''update matrix person through post - new name - 200 - 8'''
    new_name = {"name": "Neo", "job": "leader"}
    response = MatrixPersonApi().put_user(new_name)
    assert response.reason == 'OK'
    assert response.status_code == HTTPStatus.OK, f'\nStatus code is not as expected\nActual: {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.OK}'

def test_update_through_patch_matrix_person():
    '''update matrix person through patch - new name - 200 - 9'''
    new_name = {"name": "Trinity"}
    response = MatrixPersonApi().patch_user(new_name)
    assert response.reason == 'OK'
    assert response.status_code == HTTPStatus.OK, f'\nStatus code is not as expected\nActual: {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.OK}'

def test_delete_matrix_person():
    '''delete matrix person - 204 - 10'''
    response = MatrixPersonApi().delete_user()
    assert response.reason == 'No Content'
    assert response.status_code == HTTPStatus.NO_CONTENT, f'\nStatus code is not as expected\nActual: {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.NO_CONTENT}'

