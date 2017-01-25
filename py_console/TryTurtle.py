import turtle           # allows us to use the turtles library
s = turtle.Screen()     # creates a graphics window
t = turtle.Turtle()     # create a turtle named t
t.forward(150)          # tell t to move forward by 150 units
t.left(90)              # turn by 90 degrees
t.forward(75)           # complete the second side of a rectangle
s.exitonclick()         # wait to close window