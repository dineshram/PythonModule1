import turtle

myTurtle = turtle.Turtle()
counter = 0

while counter in range(0, 4):
    myTurtle.forward(50)
    myTurtle.right(90)
    counter = counter + 1

turtle.done()
