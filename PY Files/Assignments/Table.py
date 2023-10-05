"""
This Python3 program uses the Turtle GUI (Graphic User Interface) module to simply draw a scene which includes a candle, a table, a cake, and a decoration
"""

import turtle

#First, we'll have to import the Turtle GUI into Python3 interpreter

turtle.home

#the command "home" positions the turtle to the middle of the canvas so that it's ready for drawing initiation

import turtle

turtle.penup()

def scenary(table_color, table_length):
    turtle.pendown()
    turtle.color(table_color)
    turtle.forward(table_length)
    turtle.right(90)
    turtle.forward(table_length * 0.05)
    turtle.right(90)
    turtle.forward(table_length)
    turtle.right(90)
    turtle.forward(table_length * 0.05)
    turtle.right(90)
    turtle.penup()

    mini_height = 0 - table_length * 0.05

    turtle.goto(0, mini_height)

    lower_part = table_length * 0.8

    turtle.goto(-lower_part/2, mini_height)
    turtle.forward(lower_part)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(lower_part * 0.05)
    rightx = turtle.xcor()
    righty = turtle.ycor()
    turtle.right(90)
    turtle.forward(lower_part)
    leftx = turtle.xcor()
    lefty = turtle.ycor()
    turtle.right(90)
    turtle.forward(lower_part * 0.05)
    turtle.right(90)

    turtle.penup()

    turtle.goto(rightx, righty)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(table_length * 0.4)
    turtle.right(90)
    turtle.forward(table_length * 0.05)
    turtle.right(90)
    turtle.forward(table_length * 0.4)
    turtle.right(90)

    turtle.penup()

    turtle.goto(leftx, lefty)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(table_length * 0.4)
    turtle.left(90)
    turtle.forward(table_length * 0.05)
    turtle.left(90)
    turtle.forward(table_length * 0.4)
    turtle.right(90)

    turtle.penup()

    second_left_c = (lower_part/2) * 2

    turtle.goto(second_left_c, lefty)

def main():
    user_input_color = str(input("Enter the color of the table: "))

    user_input_length = float(input("Enter the length of the table: "))
    user_input_length_divided = user_input_length / 2

    turtle.goto(-user_input_length_divided,0)
    
    scenary(user_input_color, user_input_length)
    turtle.done

if __name__ == "__main__":
    main()

input("Press Enter to exit")