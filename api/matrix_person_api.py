from pythonProject.Repository_3.restapi_lesson.api.base_api import BaseAPI
from pythonProject.Repository_3.restapi_lesson.utilities.decorators import auto_steps

@auto_steps
class MatrixPersonApi(BaseAPI):

    def __init__(self):
        super().__init__()
        self.user_url = "/api/users/"

    def post_user(self, new_matrix_person):
        print('POST USER')
        return self.post(url=f"{self.user_url}", json=new_matrix_person)

    def put_user(self, new_name):
        print('PUT USER')
        return self.put(url=f"{self.user_url}{2}", json=new_name)

    def patch_user(self, new_name):
        print('PATCH USER')
        return self.patch(url=f"{self.user_url}{2}", json=new_name)

    def delete_user(self):
        print('DELETE USER')
        return self.delete(url=f"{self.user_url}{2}")