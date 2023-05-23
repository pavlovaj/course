class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def print_info(self):
        print(f'Name: {self.name}, Position: {self.position}, Salary: {self.salary}')

class Accountant(Employee):
    def __init__(self, name, salary):
        super().__init__(name, 'Accountant', salary)


class Engineer(Employee):
    def __init__(self, name, salary, education):
        super().__init__(name, 'Engineer', salary)
        self.education = education

    def print_info(self):
        super().print_info()
        print(f'Education: {self.education}')


class Technologist(Employee):
    def __init__(self, name, salary, experience):
        super().__init__(name, 'Technologist', salary)
        self.experience = experience

    def print_info(self):
            super().print_info()
            print(f'Experience Years: {self.experience}')


accountant = Accountant('Katerine Smith', 50000)
engineer = Engineer('Zac Black', 160000, 'secondary vocational education')
technologist = Technologist('Robert Salmon', 85000, 3)

accountant.print_info()
engineer.print_info()
technologist.print_info()
