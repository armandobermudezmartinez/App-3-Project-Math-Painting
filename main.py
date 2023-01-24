from canvas import Canvas
from shapes import Rectangle, Square

# Get canvas width and height from the user
canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height: "))

# Make a dictionary of color codes and prompt for color
colors = {"white": (255, 255, 255), "black": (0, 0, 0)}
canvas_color = input("Enter canvas color (white or black): ")

# Create a canvas with the user data
canvas = Canvas(canvas_height, canvas_width, color=colors[canvas_color])

while True:
    shape_type = input("What would you like to draw? Enter quit to quit: ")
    # Ask for rectangle data and create rectangle if user entered rectangle
    if shape_type.lower() == 'rectangle':
        x = int(input("Enter x of the rectangle: "))
        y = int(input("Enter y of the rectangle: "))
        width = int(input("Enter width of the rectangle: "))
        height = int(input("Enter height of the rectangle: "))
        red = int(input("How much red should the rectangle have: "))
        green = int(input("How much green should the rectangle have: "))
        blue = int(input("How much blue should the rectangle have: "))
        rectangle = Rectangle(x, y, height, width, (red, green, blue))
        rectangle.draw(canvas)

    if shape_type.lower() == 'square':
        x = int(input("Enter x of the square: "))
        y = int(input("Enter y of the square: "))
        side = int(input("Enter width of the square: "))
        red = int(input("How much red should the square have: "))
        green = int(input("How much green should the square have: "))
        blue = int(input("How much blue should the square have: "))
        square = Square(x, y, side, (red, green, blue))
        square.draw(canvas)

    if shape_type == "quit":
        break

canvas.make('canvas.png')
