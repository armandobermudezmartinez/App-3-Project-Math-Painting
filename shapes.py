class Rectangle:
    def __init__(self, x, y, height, width, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color

    def draw(self, canvas):
        canvas.data[self.y: self.y + self.height, self.x: self.x + self.width] = self.color


class Square(Rectangle):
    def __init__(self, x, y, side, color):
        super().__init__(x, y, side, side, color)
