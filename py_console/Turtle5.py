import turtle

s = turtle.Screen()
t = turtle.Turtle()

s.colormode(255)
# t.width(4)
t.speed(0)

f = 400  # forward amount
a = 90  # angle to turn
for i in range(64):
    t.pencolor((i * 4, 0, 255 - i * 4))
    t.penup()
    t.forward(f / 2)
    t.pendown()
    t.left(a)
    t.forward(f / 2)
    for j in range(3):
        t.left(a)
        t.forward(f)
    t.left(a)
    t.forward(f / 2)
    t.penup()
    t.left(a)
    t.forward(f / 2)
    t.left(360.0 / 255.0)

s.exitonclick()
