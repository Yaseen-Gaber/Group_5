# Remove the quotes ["""] & ['''] from the top and bottom of a certain code script for execution
# any Code Script(s) that starts and ends with ["""] are the TDD/TESTING scripts
# any Code Script(s) that starts and ends with ['''] are the MAIN Operational scripts
# Comments/Docstrings are mentioned after each code script

"""
import turtle
import unittest
import pixart
def draw_square(x, y, size, color):
  turtle.penup()
  turtle.goto(x, y)
  turtle.pendown()
  turtle.begin_fill()
  for _ in range(4):
    turtle.forward(size)
    turtle.left(90)
  turtle.end_fill()
class TestPixart(unittest.TestCase):
    def test_draw_square(self):
        turtle.speed(0)
        turtle.penup()
        turtle.goto(-100, -100)
        turtle.pendown()
        pixart.draw_square(x * 20, y * 20, 20, "white")
        self.assertEqual(turtle.position(), (20, 0))
        self.assertEqual(turtle.heading(), 0)
        self.assertEqual(turtle.pencolor(), "white")
if __name__ == "__main__":
    unittest.main()
"""


# TDD, "test_draw_square" function has an Attribute error ---> " module 'pixart' has no attribute 'draw_square' ""
# TDD, both "x" and "y" are not defined in the function because it's the first prototype (failing code script)


# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


"""
import turtle

def draw_checkerboard(size):
    # Create a turtle screen and turtle object
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)  # Adjust the drawing speed to maximum (fastest)

    # Set up the initial position
    t.penup()
    t.goto(-size // 2, size // 2)
    t.pendown()

    colors = ["black", "white"]  # Define the alternating colors for the checkerboard

    for i in range(size):
        for j in range(size):
            color_index = (i + j) % 2
            t.fillcolor(colors[color_index])
            t.begin_fill()

            # Draw a square of the current color
            for _ in range(4):
                t.forward(20)  # Adjust the size of each square
                t.right(90)

            t.end_fill()

            # Move to the next square position
            t.forward(20)

        # Return to the left side of the row and move down
        t.penup()
        t.goto(-size // 2, t.ycor() - 20)
        t.pendown()

    # Close the turtle graphics window when clicked
    screen.exitonclick()

def main():
    print("Welcome to the Pixel Art Checkerboard Generator!")
    size = 20  # for adjusting the size

    draw_checkerboard(size)

if __name__ == '__main__':
    main()
"""

# The turtle starts drawing the 'CHESS' checkboard from the origin and not the top left
# Second Prototype for testing the Turtle, better improvements but still needs REFACTORING
# User input (for specifying color-code strings) is the ONLY MISSING FUNCTOIN   !!!


# ----------------------------------------------------------------------------------------------------------------------------------------


"""
import turtle

def draw_checkerboard(size, square_size, checkerboard_color):
    # Create a turtle screen and turtle object
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)  # Adjust the drawing speed to maximum (fastest)

    # Calculation of the starting position to center the checkerboard
    start_x = -size * square_size / 2
    start_y = size * square_size / 2

    # Setting up the initial position at the center
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()

    colors = [checkerboard_color, "white" if checkerboard_color == "black" else "black"]

    for i in range(size):
        for j in range(size):
            color_index = (i + j) % 2
            t.fillcolor(colors[color_index])
            t.begin_fill()

            # Draw a square of the inputted/specified color
            for _ in range(4):
                t.forward(square_size)
                t.right(90)

            t.end_fill()

            # Move to the next square position
            t.forward(square_size)

        # Return to the left side of the row and move down
        t.penup()
        t.goto(start_x, t.ycor() - square_size)
        t.pendown()

    # Close the turtle graphics window when clicked
    screen.exitonclick()

def main():
    print("Welcome to the Pixel Art Checkerboard Generator!")
    size = int(input("Enter the size of the checkerboard: "))
    square_size = int(input("Enter the size of each square: "))
    checkerboard_color = input("Enter the color of the checkerboard (e.g., 'black' or 'red'): ")

    draw_checkerboard(size, square_size, checkerboard_color)

if __name__ == '__main__':
    main()
"""


# Values: size_of_checkboard = 20, size_of_square = 20, color = black | CHESS (3rd Operational Prototype)
# Still needs Refactoring   !!!


#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

'''
import turtle

def draw_pixel(color):
    turtle.penup()
    turtle.pendown()
    turtle.pencolor(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(10)
        turtle.left(90)
    turtle.end_fill()

def draw_black_pixel():
    draw_pixel('black')

def draw_white_pixel():
    draw_pixel('white')

def draw_red_pixel():
    draw_pixel('red')

def draw_yellow_pixel():
    draw_pixel('yellow')

def draw_orange_pixel():
    draw_pixel('orange')

def draw_green_pixel():
    draw_pixel('green')

def draw_yellowgreen_pixel():
    draw_pixel('yellowgreen')

def draw_sienna_pixel():
    draw_pixel('sienna')

def draw_tan_pixel():
    draw_pixel('tan')

def draw_gray_pixel():
    draw_pixel('gray')

def draw_darkgray_pixel():
    draw_pixel('darkgray')

def draw_checkerboard(size, square_size, checkerboard_color):
    # Create a turtle screen and turtle object
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)  # Adjust the drawing speed as needed

    # Calculate the starting position to center the checkerboard at the origin
    start_x = -size * square_size / 2
    start_y = size * square_size / 2

    # Set up the initial position at the center
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()

    colors = [checkerboard_color, "white" if checkerboard_color == "black" else "black"]

    for i in range(size):
        for j in range(size):
            color_index = (i + j) % 2
            t.fillcolor(colors[color_index])
            t.begin_fill()

            # Draw a square of the inputted/specified color
            for _ in range(4):
                t.forward(square_size)
                t.right(90)

            t.end_fill()

            # Move to the next square position
            t.forward(square_size)

        # Return to the left side of the row and move down
        t.penup()
        t.goto(start_x, t.ycor() - square_size)
        t.pendown()

    # Close the turtle graphics window when clicked
    screen.exitonclick()

def main():
    print("Welcome to the Pixel Art Checkerboard Generator!")
    size = int(input("Enter the size of the checkerboard: "))
    square_size = int(input("Enter the size of each square: "))
    checkerboard_color = input("Enter the color of the checkerboard (e.g., 'black', 'red', 'white', 'yellow', 'yellowgreen', 'orange', 'green', 'sienna', 'tan', 'grey', 'darkgrey'): ")

    draw_checkerboard(size, square_size, checkerboard_color)

if __name__ == '__main__':
    main()
'''

# Values: size_of_checkboard = 20, size_of_square = 20, color = red
# All Done ✅, Code Script Refactored