import numpy as np
from PIL import Image


class Canvas:
    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color

        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.data[:] = self.color

    def make(self, image_path):
        img = Image.fromarray(self.data, 'RGB')
        img.save(image_path)


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


canvas = Canvas(20, 30, (255, 255, 255))

rectangle1 = Rectangle(0, 6, 7, 10, (100, 200, 125))
rectangle1.draw(canvas)
square1 = Square(1, 3, 3, (0, 100, 222))
square1.draw(canvas)
canvas.make('canvas.png')





