import turtle as t

screen = t.Screen()
screen.bgcolor("white")

pen = t.Turtle()
pen.speed(1)  # Set the drawing speed

def draw_eye(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.begin_fill()
    pen.color("black")
    pen.circle(20)
    pen.end_fill()

def draw_nose(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.begin_fill()
    pen.color("orange")
    pen.circle(10)
    pen.end_fill()

def draw_mouth(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.width(2)
    pen.setheading(270)
    pen.circle(30, 180)  # Adjusted the circle angle to 180

def draw_face_outline():
    pen.penup()
    pen.goto(-20, -100)  # Adjusted the starting position
    pen.pendown()
    pen.width(2)
    pen.color("black")
    pen.circle(100)

draw_face_outline()
draw_eye(-50, 30)  # Adjusted the eye positions
draw_eye(10, 30)   # Adjusted the eye positions
draw_nose(-20, 0)  # Adjusted the nose position
draw_mouth(-45, -20)  # Shifted the mouth just a little further to the left

screen.exitonclick()
