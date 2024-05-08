import turtle as t
import math

PI = math.pi

def setPos(x, y):
    t.pu()
    t.goto(x, y)
    t.pd()

def circles(radius, depth):
    circumference = 2 * PI * radius
    if depth == 0:
        return 0
    elif depth == 1:
        t.circle(radius, 360, None)
        t.pu()
        return circumference
    elif depth == 2:
        for _ in range(4):
            t.pd()
            circles(radius / 0.99, depth - 1)
            t.rt(90)
    elif depth == 3:
        t.pd()
        for _ in range(4):
            circles(radius / 1.98, t.circle(50.5050505050501, 180))
            circles(radius / 1.98, depth - 1)
            circles(radius / 1.98, t.circle(50.5050505050501, 180))
            t.rt(90)
    elif depth == 4:
        circles(radius / 1.98, t.circle(50.5050505050501, 180))
        for _ in range(4):
            t.pd()
            circles(radius / 3.96, t.circle(25.25252525252525, 180))
            circles(radius / 3.96, depth - 2)
            circles(radius / 3.96, t.circle(25.25252525252525, 180))
            t.rt(90)
        circles(radius / 1.98, t.circle(50.5050505050501, 180))
        
        t.rt(90)
        circles(radius / 3.96, t.circle(25.25252525252525, 180))
        circles(radius / 3.96, depth - 2)
        circles(radius / 3.96, t.circle(-25.25252525252525, 180))
        t.lt(90)

        circles(radius / 1.98, t.circle(50.5050505050501, 180))
        
        for _ in range(2):
            circles(radius / 3.96, t.circle(25.25252525252525, 180))
            circles(radius / 3.96, depth - 2)
            circles(radius / 3.96, t.circle(-25.25252525252525, 180))

        circles(radius / 1.98, t.circle(-50.5050505050501, 180))
        t.rt(90)

        circles(radius / 3.96, t.circle(25.25252525252525, 180))
        circles(radius / 3.96, depth - 2)
        circles(radius / 3.96, t.circle(-25.25252525252525, 180))

        circles(radius / 0.99, t.circle(-radius, 180))
        t.rt(90)

        circles(radius / 3.96, t.circle(-25.25252525252525, 180))
        circles(radius / 3.96, depth - 2)
        circles(radius / 3.96, t.circle(25.25252525252525, 180))
        t.lt(90)

        circles(radius / 3.96, t.circle(-25.25252525252525, 180))
        circles(radius / 3.96, depth - 2)
        circles(radius / 3.96, t.circle(25.25252525252525, 180))

        circles(radius / 1.98, t.circle(50.5050505050501, 180))
        t.rt(90)

        circles(radius / 3.96, t.circle(25.25252525252525, 180))
        circles(radius / 3.96, depth - 2)
        circles(radius / 3.96, t.circle(-25.25252525252525, 180))

        circles(radius / 1.98, t.circle(-50.5050505050501, 180))
        t.rt(90)
        
        circles(radius / 3.96, t.circle(-25.25252525252525, 180))
        circles(radius / 3.96, depth - 2)
        circles(radius / 3.96, t.circle(25.25252525252525, 180))

        circles(radius / 0.99, t.circle(radius, 270)) # 
        t.rt(90)

        circles(radius / 3.96, t.circle(25.25252525252525, 180))
        circles(radius / 3.96, depth - 2)
        circles(radius / 3.96, t.circle(-25.25252525252525, 180))
        t.lt(90)

        circles(radius / 3.96, t.circle(-25.25252525252525, 180))
        circles(radius / 3.96, depth - 2)
        circles(radius / 3.96, t.circle(25.25252525252525, 180))

        circles(radius / 1.98, t.circle(50.5050505050501, 180))

        circles(radius / 3.96, t.circle(25.25252525252525, 180))
        circles(radius / 3.96, depth - 2)
        circles(radius / 3.96, t.circle(-25.25252525252525, 180))

        circles(radius / 1.98, t.circle(-50.5050505050501, 180))
        t.rt(180)
        
        circles(radius / 3.96, t.circle(-25.25252525252525, 180))
        circles(radius / 3.96, depth - 2)
        circles(radius / 3.96, t.circle(25.25252525252525, 180))

        circles(radius / 1.98, t.circle(50.5050505050501, 180))
        t.rt(90)

        circles(radius / 3.96, t.circle(25.25252525252525, 180))
        circles(radius / 3.96, depth - 2)
        circles(radius / 3.96, t.circle(-25.25252525252525, 180))
    # elif depth == 5:
        pass


def main():
    screen = t.Screen()
    screen.setup(width=1.0, height=1.0)
    screen.title("Turtle Recursion")
    t.speed(0)
    t.pencolor('red')
    t.pensize(2)
    setPos(0, -150)
    circumference = circles(200, 1)
    print(f"The circumference of the circle is {circumference}")
    setPos(0, 50)
    circles(100, 2)
    circles(100, 3)
    circles(100, 4)
    # circles(100, 5)
    t.done()

main()