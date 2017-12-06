
import turtle

myTurtle = turtle.Turtle()
myTurtle.shape("turtle")
#mySecondTurtle = turtle.Turtle()

myList = [1, 2, 3, 5, 8, 13, 21]

print(myList)
print(myList[0])
print(myList[4])
#print(myList[5])

#defining the function
def printMyList():
    print("In the function")
    for i in range(0, len(myList)):
        print(myList[i])

#calling the function
printMyList()

def addMyList():
    sumOfList = 0
    print("Summing up my list of numbers")
    for i in range(0, len(myList)):
        sumOfList = sumOfList + myList[i]

    print("The sum of myList is ", sumOfList)

addMyList()

def usingTurtleWithLists():
    for i in range(0, len(myList)):
        myTurtle.forward(myList[i]*10)
        myTurtle.right(90)

usingTurtleWithLists()
turtle.done()
