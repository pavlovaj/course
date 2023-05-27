class Shape:
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def info(self):
        print(f"Эта фигура {self.size} {self.color}.")


class Square(Shape):
    def __init__(self, color, size, length):
        super().__init__(color, size)
        self.length = length

    def info(self):
        print(f"Это {self.size} {self.color} квадрат длиной {self.length} cm.")


class Circle(Shape):
    def __init__(self, color, size, radius):
        super().__init__(color, size)
        self.radius = radius

    def info(self):
        print(f"Это {self.size} {self.color} круг с радиусом {self.radius} cm.")


class Box:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        if isinstance(shape, Shape):
            self.shapes.append(shape)
        else:
            print("Invalid shape.")

    def show_contents(self):
        for shape in self.shapes:
            shape.info()


square1 = Square("желтый", "большой", 15)
circle1 = Circle("зеленый", "средний", 7)
circle2 = Circle("черный", "маленький", 3)
star1 = "invalid shape"

box1 = Box()
box1.add_shape(square1)
box1.add_shape(circle1)
box1.add_shape(circle2)
box1.add_shape(star1)

box1.show_contents()
