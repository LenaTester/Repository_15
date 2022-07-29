class Color:
    def __init__(self, id, name, year, color, pantone_value):
        self.id = id
        self.name = name
        self.year = year
        self.color = color
        self.pantone_value = pantone_value

    def __eq__(self, other):
        object_1 = self.__dict__
        object_2 = other.__dict__
        return self.__dict__ == other.__dict__