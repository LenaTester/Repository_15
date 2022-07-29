from pythonProject.Repository_3.restapi_lesson.utilities.config import config
import requests


class BaseAPI:

    def __init__(self):
        self.base_url = config['base_url']
        self.user = 'Lena'
        self.headers = None
        self.request = requests

    def get(self, url, body=None, headers=None, params=None):
        print('GET from BaseAPI')
        if headers is None:
            print('BASE HEADERS')
            headers = self.headers
        else:
            print('CUSTOM_HEADERS')
        response = self.request.get(f"{self.base_url}{url}", data=body, headers=headers, params=params)
        print(f'Perform GET request')
        return response

    def post(self, url, json=None, headers=None, params=None):
        print('POST from BaseAPI')
        if headers is None:
            print('BASE HEADERS')
            headers = self.headers
        else:
            print('CUSTOM_HEADERS')
        response = self.request.post(f"{self.base_url}{url}", json, headers=headers, params=params)
        print(f'Perform POST request')
        return response

    def put(self, url, json=None, headers=None, params=None):
        print('PUT from BaseAPI')
        if headers is None:
            print('BASE HEADERS')
            headers = self.headers
        else:
            print('CUSTOM_HEADERS')
        response = self.request.put(f"{self.base_url}{url}", json, headers=headers, params=params)
        print(f'Perform PUT request')
        return response

    def patch(self, url, json=None, headers=None, params=None):
        print('PATCH from BaseAPI')
        if headers is None:
            print('BASE HEADERS')
            headers = self.headers
        else:
            print('CUSTOM_HEADERS')
        response = self.request.put(f"{self.base_url}{url}", json, headers=headers, params=params)
        print(f'Perform PATCH request')
        return response

    def delete(self, url, headers=None, params=None):
        print('DELETE from BaseAPI')
        if headers is None:
            print('BASE HEADERS')
            headers = self.headers
        else:
            print('CUSTOM_HEADERS')
        response = self.request.delete(f"{self.base_url}{url}", headers=headers, params=params)
        print(f'Perform DELETE request')
        return response

