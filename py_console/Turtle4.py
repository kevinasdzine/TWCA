import turtle

s = turtle.Screen()
t = turtle.Turtle()

s.colormode(255)
# t.width(4)
t.speed(0)

f = 200  # forward amount
a = 90  # angle to turn
for i in range(255):
    t.pencolor((i, 0, 255 - i))
    for j in range(4):
        t.forward(f)
        t.left(a)
    t.left(360.0 / 255.0)

s.exitonclick()
