"""
Values: x = 180, y = 150, a = 180, b = 100, d = 180, z = 75 | Table Color: Brown, length: 300.
"""

import turtle as t

t.bgcolor("lightblue")

def plate():
    t.pencolor("white")
    t.fillcolor("white")
    t.begin_fill()
    t.forward(200)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(400)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(200)
    t.end_fill()




x = int(input("Enter the value of x to continue.."))
y = int(input("Enter the value of y to continue.."))




def layer1(x,y):
    t.penup()
    t.goto(0,10)
    t.pendown()
    t.pencolor("pink")
    t.fillcolor("pink")
    t.begin_fill()
    for i in range(1):
        t.forward(x)
        t.left(90)
        t.forward(y)
        t.left(90)
        t.forward(x*2)
        t.left(90)
        t.forward(y)
        t.left(90)
        t.forward(x)
        t.end_fill()
        



a = int(input("Enter the value of a to continue.."))
b = int(input("Enter the value of b to continue.."))

def layer2(a,b):
    t.pencolor("yellow")
    t.fillcolor("yellow")
    t.begin_fill()
    for i in range(1):
        t.forward(a)
        t.left(90)
        t.forward(b)
        t.left(90)
        t.forward(a*2)
        t.left(90)
        t.forward(b)
        t.left(90)
        t.end_fill()
        



d = int(input("Enter the value of d to continue.."))
z = int(input("Enter the value of z to continue.."))

def layer3(d,z):
    t.pencolor("green")
    t.fillcolor("green")
    t.begin_fill()
    t.penup()
    t.goto(0,10)
    t.pendown()
    for i in range(1):
        t.forward(d)
        t.left(90)
        t.forward(z)
        t.left(90)
        t.forward(d*2)
        t.left(90)
        t.forward(z)
        t.left(90)
        t.forward(d)
        t.end_fill()
        t.done


      

plate()
layer1(x,y)
layer2(a,b)
layer3(d,z)




def draw_decoration(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pencolor("blue")
    t.fillcolor("blue")
    t.begin_fill()
    t.circle(10)
    t.end_fill()




draw_decoration(5, y + 10)  




def draw_candle(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    t.pencolor("brown")
    t.fillcolor("brown")
    t.begin_fill()
    t.goto(x - 5, y)
    t.goto(x - 5, y + 30)
    t.goto(x + 5, y + 30)
    t.goto(x + 5, y)
    t.end_fill()

    t.penup()
    t.goto(x, y + 30)
    t.pendown()
    t.pencolor("yellow")
    t.fillcolor("yellow")
    t.begin_fill()
    t.goto(x - 5, y + 40)
    t.goto(x, y + 45)
    t.goto(x + 5, y + 40)
    t.goto(x, y + 30)
    t.end_fill()




draw_candle(55, 160)  



def draw_decoration(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pencolor("blue")
    t.fillcolor("blue")
    t.begin_fill()
    t.circle(10)
    t.end_fill()




draw_decoration(5, y + 10)  




def draw_candle(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    t.pencolor("brown")
    t.fillcolor("brown")
    t.begin_fill()
    t.goto(x - 5, y)
    t.goto(x - 5, y + 30)
    t.goto(x + 5, y + 30)
    t.goto(x + 5, y)
    t.end_fill()

    t.penup()
    t.goto(x, y + 30)
    t.pendown()
    t.pencolor("yellow")
    t.fillcolor("yellow")
    t.begin_fill()
    t.goto(x - 5, y + 40)
    t.goto(x, y + 45)
    t.goto(x + 5, y + 40)
    t.goto(x, y + 30)
    t.end_fill()




draw_candle(-55, 160)  



def draw_icing(x, y, width):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pencolor("White") 
    t.fillcolor("White")  
    t.begin_fill()
    t.forward(200 + width * -0.6)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(385 + width * -0.6)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(200 + width * -0.6)
    t.end_fill()

icing_x = 0
icing_y = 149.8
icing_width = 25


draw_icing(icing_x, icing_y, icing_width)




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