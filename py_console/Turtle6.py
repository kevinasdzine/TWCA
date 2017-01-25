import math
import turtle

s = turtle.Screen()
t = turtle.Turtle()

s.colormode(255)
# t.width(4)
t.speed(0)

f = 400  # forward amount
a = 120  # angle to turn
h = math.sqrt(f ** 2 - ((f / 2) ** 2)) / 3 * 2
t.left(90)
for i in range(255/3):
    t.pencolor((i*3, 0, 255 - i*3))
    t.penup()
    t.forward(h)
    t.pendown()
    t.left(30)
    for j in range(3):
        t.left(a)
        t.forward(f)
    t.penup()
    t.left(150)
    t.forward(h)
    t.left(180)
    t.left(360.0 / 255.0)

s.exitonclick()
