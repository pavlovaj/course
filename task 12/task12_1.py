class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age
        self.__position = "manager"

    def get_position(self):
        return self.__position

    def set_position(self, new_position):
        self.__position = new_position

person = Person("Bob", 35)
print(person.name)
print(person._age)

print(person.__position)

print(person.get_position())

person.set_position("senior manager")
print(person.get_position())

print(person._Person__position)