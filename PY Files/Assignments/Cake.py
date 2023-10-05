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



x = int(input("Enter the value of x to contiinue.."))
y = int(input("Enter the value of y to contiinue.."))

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