class Table:
    def __init__(self, l, w, h):
        self.long = l
        self.width = w
        self.height = h

    def outing(self):
        print(self.long, self.width, self.height)


class Kitchen(Table):
    def howplaces(self, n):
        if n < 2:
            print("It is not kitchen table")
        else:
            self.places = n
    def outplases(self):
        print(self.places)


class Dressing(Table):
    def is_convenient_for_makeup(self):
        if 85 >= self.height >= 75:
            print("This is a convenient height")
        else:
            print("This is an unconvenient height")

    def is_very_convenient_for_makeup(self):
        if 60 <= self.width >= 30:
            print("This is a convenient width")
        else:
            print("This is an unconvenient width")