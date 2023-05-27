class Person:
    def __init__(self, name):
        self.name = name


    def info(self):
        print("This is", self.name)
        self.__position()

    def __position(self):
        print(f"He is a senior manager")


person1 = Person("Bob Miller")
person1.info()