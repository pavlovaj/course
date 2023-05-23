class Figure:
    def __init__(self):
        self.color = "white"

    def change_color(self, new_color):
        self.color = new_color

    def print_info(self):
        print('')


class Oval(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.color = color

    def print_info(self):
        print(f'Oval, color: {self.color}, width: {self.width}, height: {self.height}')


class Square(Figure):
    def __init__(self, length):
        self.length = length

    def print_info(self):
        print(f'Square, color: {self.color}, side length: {self.length}')


oval = Oval(5, 10)
square = Square(5)

oval.print_info()
square.print_info()

oval.change_color('green')
square.change_color('red')

oval.print_info()
square.print_info()