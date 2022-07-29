from pythonProject.Repository_3.restapi_lesson.api.base_api import BaseAPI
from pythonProject.Repository_3.restapi_lesson.utilities.decorators import auto_steps

@auto_steps
class UsersApi(BaseAPI):

    def __init__(self):
        super().__init__()
        self.user_url = "/api/users/"

    def get_user(self, user_id, headers=None):
        print('GET PEOPLE')
        return self.get(url=f"{self.user_url}{user_id}", headers=headers)


