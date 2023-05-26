class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, new_name):
        self.__name = new_name

    def set_age(self, new_age):
        if new_age in range(1, 150):
            self.__age = new_age
        else:
            print("This is incorrect age.")