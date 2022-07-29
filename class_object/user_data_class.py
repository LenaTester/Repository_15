class User:
    def __init__(self, email, first_name, last_name):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def __eq__(self, other):
        object_1 = self.__dict__
        object_2 = other.__dict__
        return self.__dict__ == other.__dict__
