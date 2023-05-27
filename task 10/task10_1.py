class Person:
    def __init__(self, name, plan):
        self.name = name
        self.plan = plan

    def info(self):
        print(f"{self.name}  собирается {self.plan} этим вечером")

class Friend:
    def __init__(self, name, plan):
        self.name = name
        self.plan = plan

    def change_person(self, person):
        print(f"{self.name} поговорил(а) с {person.name} о планах на вечер и убедила {self.plan}")

    def convince_person(self, person):
        person.plan = self.plan

person1 = Person("Юля", "спать")
friend1 = Friend("Аня", "пойти гулять")

person1.info()
friend1.change_person(person1)
friend1.convince_person(person1)
person1.info()