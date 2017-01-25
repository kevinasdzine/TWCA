import turtle

s = turtle.Screen()
t = turtle.Turtle()

s.colormode(255)
t.width(4)

f = 10 # forward amount
a = 45 # angle to turn
for i in range(255):
    t.pencolor((i,0,255-i))
    t.forward(f)
    t.left(a)
    f = f + 1
    
s.exitonclick()
