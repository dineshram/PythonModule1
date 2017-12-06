

import turtle

def setupTurtle():
    myTurtleInsideFunction = turtle.Turtle()
    myTurtleInsideFunction.penup()
    myTurtleInsideFunction.setpos(-300, 0)
    myTurtleInsideFunction.pendown()
    myTurtleInsideFunction.color('red')
    myTurtleInsideFunction.pensize(2.5)
    myTurtleInsideFunction.speed(100)

    return myTurtleInsideFunction

#call the setupTurtle function and store the result in a variable
#called myTurtle
myTurtle = setupTurtle()

#define the temperature list
averageTemperatureList = [3, 4,	6, 9, 14, 17, 18, 17, 14, 11, 7, 4]
numberOfRainyDays = [22, 19, 19, 18, 17, 18, 19, 19, 20, 21, 21, 20]

def pulse(height, width):
    myTurtle.left(90)
    myTurtle.forward(height*10)
    myTurtle.right(90)
    myTurtle.forward(width)
    myTurtle.right(90)
    myTurtle.forward(height*10)
    myTurtle.left(90)
    myTurtle.forward(width)

#for i in range(0, len(averageTemperatureList)):
#    pulse()

for temp in averageTemperatureList:
    print("temp now is ", temp)
    myTurtle.write("hello")
    pulse(temp, 25)

turtle.done()
