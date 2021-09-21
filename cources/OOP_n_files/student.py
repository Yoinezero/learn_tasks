class Student:

    def __init__(self, name: str, surname: str):
        self.__name = name
        self.__surname = surname

    def __str__(self):
        return f"{self.name}"

    @property
    def name(self):
        return f"{self.__name} {self.__surname}"
