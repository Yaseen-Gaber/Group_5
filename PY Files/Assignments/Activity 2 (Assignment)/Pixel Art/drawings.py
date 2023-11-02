# Remove the quotes ["""] & ['''] from the top and bottom of a certain code script for execution
# any Code Script(s) that starts and ends with ["""] are the TDD/TESTING scripts
# any Code Script(s) that starts and ends with ['''] are the MAIN Operational scripts
# Comments/Docstrings are mentioned after each code script

"""
import turtle

def draw_pixels(string):
    color_table = {
        '0': 'black',
        '1': 'white',
        '2': 'red',
        '3': 'yellow',
        '4': 'orange',
        '5': 'green',
        '6': 'yellowgreen',
        '7': 'sienna',
        '8': 'tan',
        '9': 'gray',
        'A': 'darkgray',
    }

    turtle.speed(0)
    turtle.penup()
    turtle.goto(-20 * (len(string) // 2), 0)  # Center the drawing at the canvas's origin

    for char in string:
        if char in color_table:
            turtle.pendown()
            turtle.fillcolor(color_table[char])

            # Draw and fill a square
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(20)
                turtle.right(90)
            turtle.end_fill()

            turtle.penup()
            turtle.forward(20)
        else:
            return False

    return True

def main():
    user_input = input("Enter a string of colors (e.g., '01A753421'): ")
    if draw_pixels(user_input):
        print("Drawing complete.")
    else:
        print("Invalid input. Make sure to use valid color characters.")

if __name__ == '__main__':
    main()
    turtle.done()
"""

# Python3 Code Script without LOOP and 'q' for quitting [for testing color code]
# Example VALUE: 01A753421 | Drawing Done Message output/printed

# ---------------------------------------------------------------------------------------------------------------------------------

"""
import turtle

def draw_pixels(string):
    color_table = {
        '0': 'black',
        '1': 'white',
        '2': 'red',
        '3': 'yellow',
        '4': 'orange',
        '5': 'green',
        '6': 'yellowgreen',
        '7': 'sienna',
        '8': 'tan',
        '9': 'gray',
        'A': 'darkgray',
    }

    turtle.speed(0)
    turtle.penup()
    turtle.goto(-20 * (len(string) // 2), turtle.ycor())  # Center the drawing on the same currecnt row

    for char in string:
        if char in color_table:
            turtle.pendown()
            turtle.fillcolor(color_table[char])

            # Draw and fill a square
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(20)
                turtle.right(90)
            turtle.end_fill()

            turtle.penup()
            turtle.forward(20)
        else:
            return False

    return True

def draw_multiple_pixels():
    while True:
        user_input = input("Enter a string of colors (e.g., '01A753421') or 'q' to quit: ")
        if user_input.lower() == 'q':
            break
        if not user_input:
            break  # Stop on empty input
        if not draw_pixels(user_input):
            print("Invalid input. Make sure to use valid color characters or an empty string to quit.")

def main():
    draw_multiple_pixels()
    turtle.done()

if __name__ == '__main__':
    main()
"""

# TDD, Over-writing color code values on the same row, the user can input as many color code(s) as desired
# The user can enter 'q' to quit at any time, any color code values will be OVERWRITTEN
# No invalid color should be inputted therefor outputting an error message
# A Refactored version of the previous Code Script with enhanced features like 'q' and "Invalid color" in a LOOP


# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

"""
import turtle

def draw_grid(size, square_size):
    turtle.speed(0)
    turtle.penup()
    x_start = -size * square_size / 2
    y_start = size * square_size / 2

    for i in range(size + 1):
        y = y_start - i * square_size
        turtle.goto(x_start, y)
        turtle.pendown()
        turtle.forward(size * square_size)
        turtle.penup()

    turtle.setheading(270)  # Turn to face down to draw the grid
    for i in range(size + 1):
        x = x_start + i * square_size
        turtle.goto(x, y_start)
        turtle.pendown()
        turtle.forward(size * square_size)
        turtle.penup()

def draw_pixel(color, size, x, y):
    color_table = {
        '0': 'black',
        '1': 'white',
        '2': 'red',
        '3': 'yellow',
        '4': 'orange',
        '5': 'green',
        '6': 'yellowgreen',
        '7': 'sienna',
        '8': 'tan',
        '9': 'gray',
        'A': 'darkgray',
    }

    turtle.speed(0)
    turtle.penup()

    x_start = -size * 20 / 2 + 20  # Shift the starting x-coordinate to the right by one square
    x += x_start
    y_start = size * 20 / 2        # Shift y-coordinate down by one square so that it aligns with the grid

    turtle.goto(x, y_start - y)  # Adjusting y-coordinate to draw beneath the previous row

    turtle.pendown()
    turtle.fillcolor(color_table[color])

    # Draw and fill a square
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(20)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()

def main():
    size = 10  # Define the size of the grid
    square_size = 20  # Define the size of each square
    draw_grid(size, square_size)
    
    x = 0  # Initialize x position
    y = 0  # Initialize y position
    
    while True:
        user_input = input("Enter a string of colors (e.g., '01A753421' or any other 10-character color code) or 'q' to quit: ")
        if user_input.lower() == 'q':
            break  # Stop on 'q' input from user
        for char in user_input:
            if char.isalnum():
                draw_pixel(char, size, x, y)
                x += 20  # Shift right for the next square while drawing
        y += 20  # Shift down to the next row
        x = 0  # Reset x for the new row

    turtle.done()

if __name__ == '__main__':
    main()
"""

# The program incduces creativity by implementing pixel art on a simple grid, using while loop to promote prudence
# Testing , horizontally drawing the color code values inputted inside a grid, press 'q' after you're done inputting color code values

"""
from turtle import Screen, Turtle

PIXEL_SIZE = 30
CURSOR_SIZE = 20

COLORS = {
    'B': 'blue',
    'K': 'black',
    'O': 'orange',
    'R': 'red',
    'T': 'brown',
    'W': 'white',
    'Y': 'yellow',
}

PIXELS = [
    "WWWRRRRRRWWWW",
    "WWRRRRRRRRRRW",
    "WWTTTOOOKOWWW",
    "WTOTOOOOKOOOW",
    "WTOTTOOOOKOOO",
    "WTTOOOOOKKKKW",
    "WWWOOOOOOOOWW",
    "WWRRBRRRRWWWW",
    "WRRRBRRBRRRWW",
    "RRRRBBBBRRRRW",
    "OORBYBBYBROOW",
    "OOOBBBBBBOOOW",
    "OOBBBBBBBBOOW",
    "WWBBBWWBBBWWW",
    "WTTTWWWWTTTWW",
    "TTTTWWWWTTTTW",
]

WIDTH, HEIGHT = len(PIXELS[0]), len(PIXELS)

screen = Screen()
screen.setup((WIDTH + 3) * PIXEL_SIZE, (HEIGHT + 3) * PIXEL_SIZE)
screen.tracer(False)

turtle = Turtle()
turtle.hideturtle()
turtle.shape('square')
turtle.shapesize(PIXEL_SIZE / CURSOR_SIZE)
turtle.penup()

x0 = -WIDTH/2 * PIXEL_SIZE
y0 = HEIGHT/2 * PIXEL_SIZE

for i, row in enumerate(PIXELS):
    turtle.setposition(x0, y0 - i * PIXEL_SIZE)

    for pixel in row:
        turtle.color(COLORS[pixel])
        turtle.stamp()
        turtle.forward(PIXEL_SIZE)

screen.tracer(True)
screen.exitonclick()
"""

# Actual Working Code (Mairo) from the Internet, particularly stackoverflow.com for demonstration of how the format/structure of the code should be
# The result is executed directly without turtle drawing it & without a grid


#########################################################################################################################

"""
import turtle

def draw_grid(size, square_size):
    turtle.speed(0)
    turtle.penup()
    x_start = -size * square_size / 2
    y_start = size * square_size / 2

    for i in range(size + 1):
        y = y_start - i * square_size
        turtle.goto(x_start, y)
        turtle.pendown()
        turtle.forward(size * square_size)
        turtle.penup()

    for i in range(size + 1):
        x = x_start + i * square_size
        turtle.goto(x, y_start)
        turtle.pendown()
        turtle.setheading(270)
        turtle.forward(size * square_size)
        turtle.penup()

def draw_pixels(pixels, size):
    COLORS = {
        '0': 'black',
        '1': 'white',
        '2': 'red',
        '3': 'yellow',
        '4': 'orange',
        '5': 'green',
        '6': 'yellowgreen',
        '7': 'sienna',
        '8': 'tan',
        '9': 'gray',
        'A': 'darkgray',
    }

    turtle.speed(0)
    turtle.penup()
    x_start = -size * 20 / 2
    y_start = size * 20 / 2 - 20  # Shift one row upwards
    row_height = 20

    for row_index, row in enumerate(pixels):
        y = y_start - (row_index - 1) * row_height
        x = x_start

        for char in row:
            if char in COLORS:
                turtle.penup()
                x += 20  # Move to the next position in the same row
                turtle.goto(x, y)

                turtle.pendown()
                turtle.fillcolor(COLORS[char])

                turtle.begin_fill()
                for _ in range(4):
                    turtle.forward(20)
                    turtle.right(90)
                turtle.end_fill()

    return True

def main():
    size = 20  # Define the size of the grid
    square_size = 20  # Define the size of each square
    draw_grid(size, square_size)
    input_pixels = [
        "00000000000000000000",
        "01111111111111111110",
        "01111111111111111110",
        "01111111100111111110",
        "01111111033011111110",
        "01111110333301111110",
        "01000000333300000010",
        "01033333333333333010",
        "01104333033033340110",
        "01110433033033401110",
        "01111043033034011110",
        "01111043333334011110",
        "01110433333333401110",
        "01110433333333401110",
        "01104334400443340110",
        "01104440011004440110",
        "01044001111110044010",
        "01000111111111100010",
        "01111111111111111110",
        "00000000000000000000"
    ]
    draw_pixels(input_pixels, size)
    turtle.done()

if __name__ == '__main__':
    main()
"""

# Drawing the Star but without any user input (No MANUAL INPUT), best so far
# The Mario smaple from the internet helped a lot in producing this output/result

# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

'''
import turtle

# Function to draw the grid
def draw_grid(rows, columns, square_size):
    turtle.speed(0)
    turtle.penup()
    x_start = -columns * square_size / 2
    y_start = rows * square_size / 2

    for i in range(rows + 1):
        y = y_start - i * square_size
        turtle.goto(x_start, y)
        turtle.pendown()
        turtle.forward(columns * square_size)
        turtle.penup()

    for i in range(columns + 1):
        x = x_start + i * square_size
        turtle.goto(x, y_start)
        turtle.pendown()
        turtle.setheading(270)
        turtle.forward(rows * square_size)
        turtle.penup()

# Function to draw the pixels based on color codes
def draw_pixels(pixels, rows, columns):
    COLORS = {
        '0': 'black',
        '1': 'white',
        '2': 'red',
        '3': 'yellow',
        '4': 'orange',
        '5': 'green',
        '6': 'yellowgreen',
        '7': 'sienna',
        '8': 'tan',
        '9': 'gray',
        'A': 'darkgray',
    }

    turtle.speed(0)
    turtle.penup()
    x_start = -columns * 20 / 2
    y_start = rows * 20 / 2 - 20  # Shift one row upwards
    row_height = 20

    for row_index, row in enumerate(pixels):
        y = y_start - (row_index - 1) * row_height
        x = x_start

        for char in row:
            if char in COLORS:
                turtle.penup()
                x += 20  # Move to the next position in the same row
                turtle.goto(x, y)

                turtle.pendown()
                turtle.fillcolor(COLORS[char])

                turtle.begin_fill()
                for _ in range(4):
                    turtle.forward(20)
                    turtle.right(90)
                turtle.end_fill()

    return True

# Function to draw a 22x25 grid
def draw_22x25_grid():
    rows = 22
    columns = 25
    square_size = 20
    draw_grid(rows, columns, square_size)

    while True:
        input_pixels = []
        for i in range(rows):
            user_input = input(f"Enter row {i + 1} of pixel data: ")
            if user_input.lower() == 'q':
                break
            if not user_input or len(user_input) != columns:
                print("Invalid input. Make sure to enter a valid row of pixel data.")
                continue
            input_pixels.append(user_input)

        if input_pixels:
            if not draw_pixels(input_pixels, rows, columns):
                print("Invalid input. Make sure to use valid color characters.")
        else:
            break  # Stop on empty input

    turtle.done()

# Function to draw a 20x20 grid
def draw_20x20_grid():
    rows = 20
    columns = 20
    square_size = 20
    draw_grid(rows, columns, square_size)

    while True:
        input_pixels = []
        for i in range(rows):
            user_input = input(f"Enter row {i + 1} of pixel data: ")
            if user_input.lower() == 'q':
                break
            if not user_input or len(user_input) != columns:
                print("Invalid input. Make sure to enter a valid row of pixel data.")
                continue
            input_pixels.append(user_input)

        if input_pixels:
            if not draw_pixels(input_pixels, rows, columns):
                print("Invalid input. Make sure to use valid color characters.")
        else:
            break  # Stop on empty input

    turtle.done()

if __name__ == '__main__':
    code_number = input("Enter the code for your drawing, e.g., 01, 02, 03, 04: ")

    if code_number == "02":
        draw_22x25_grid()
    else:
        draw_20x20_grid()
'''

# The user has to spicify the drawings code [drawingXX] first before actually inputting/pasting the values Manually to draw the grid

# Star, Mario & Luigi, Manually + 'q' for quitting the while loop as well as invalid input message
# 20 rows & 20 columns
    
# Baby Yoda, Manually + 'q' for quitting the while loop as well as invalid input message
# 22 rows & 25 columns

# Note: to paste text into MS VS Code, use "CTRL + Shift + V"

'''
import os
import turtle

# Define the folder path where text files are located
folder_path = "D:\Personal\Yaseen\RIT (Rochester Institute of Technology)\Software Developement\PY Files\Assignments\Activity 2 (Assignment)\Pixel Art"  # Replace with the actual folder path

# Function to draw the grid
def draw_grid(rows, columns, square_size):
    turtle.speed(0)
    turtle.penup()
    x_start = -columns * square_size / 2
    y_start = rows * square_size / 2

    for i in range(rows + 1):
        y = y_start - i * square_size
        turtle.goto(x_start, y)
        turtle.pendown()
        turtle.forward(columns * square_size)
        turtle.penup()

    for i in range(columns + 1):
        x = x_start + i * square_size
        turtle.goto(x, y_start)
        turtle.pendown()
        turtle.setheading(270)
        turtle.forward(rows * square_size)
        turtle.penup()

# Function to draw the pixels based on color codes
def draw_pixels(pixels, rows, columns):
    COLORS = {
        '0': 'black',
        '1': 'white',
        '2': 'red',
        '3': 'yellow',
        '4': 'orange',
        '5': 'green',
        '6': 'yellowgreen',
        '7': 'sienna',
        '8': 'tan',
        '9': 'gray',
        'A': 'darkgray',
    }

    turtle.speed(0)
    turtle.penup()
    x_start = -columns * 20 / 2
    y_start = rows * 20 / 2 - 20  # Shift one row upwards
    row_height = 20

    for row_index, row in enumerate(pixels):
        y = y_start - (row_index - 1) * row_height
        x = x_start

        for char in row:
            if char in COLORS:
                turtle.penup()
                x += 20  # Move to the next position in the same row
                turtle.goto(x, y)

                turtle.pendown()
                turtle.fillcolor(COLORS[char])

                turtle.begin_fill()
                for _ in range(4):
                    turtle.forward(20)
                    turtle.right(90)
                turtle.end_fill()

    return True

# Function to process a single text file
def process_single_file(file_name, rows, columns):
    try:
        with open(file_name, 'r') as file:
            input_pixels = [line.strip() for line in file.readlines() if len(line.strip()) == columns]
            if not input_pixels or len(input_pixels) != rows:
                print("Invalid input file. The content must match the grid dimensions.")
                return
            if not draw_pixels(input_pixels, rows, columns):
                print("Invalid input. Make sure to use valid color characters.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")

# Function to process text files in the specified folder
def process_text_files(rows, columns, folder_path):
    file_names = [f for f in os.listdir(folder_path) if f.endswith(".txt")]

    if not file_names:
        print("No text files found in the specified folder.")
        return

    for file_name in file_names:
        process_single_file(file_name, rows, columns)
        turtle.done()

def main():
    code_number = input("Enter the code for your drawing, e.g., 01, 02, 03, 04: ")

    if code_number == "02":
        rows = 22
        columns = 25
    else:
        rows = 20
        columns = 20

    square_size = 20  # Define the size of each square
    draw_grid(rows, columns, square_size)

    folder_path = "D:\Personal\Yaseen\RIT (Rochester Institute of Technology)\Software Developement\PY Files\Assignments\Activity 2 (Assignment)\Pixel Art"

    user_choice = input("Enter the name of the text file you want to process: ")

    if user_choice:
        if not user_choice.endswith(".txt"):
            user_choice += ".txt"
        process_single_file(os.path.join(folder_path, user_choice), rows, columns)
    else:
        print("Invalid input. Please specify a valid text file for processing.")

if __name__ == '__main__':
    main()
'''

# Challenge Done ✅ | NO MULTIPLE FILES PROCESSING  !!! (NOT REQUIRED/NEEDED)
# (which is to reference a certain folder that has the drawings.txt files and spicify file name that you want the program to execute [open, read & draw])
# Without creating the necessary grid first (by specifying the drawings code), the program won't execute properly and may end up malfunctioning/crashing