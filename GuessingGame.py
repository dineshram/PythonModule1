import random

minimum = int(input("Enter the lower range"))
maximum = int(input("Enter a higher range"))
maxTries = 5

myRandomNumber = random.randint(minimum, maximum)
theNumberGuessed = int(input("Guess a number between 1 and 6"))
#print(type(theNumberGuessed))
tries = 0

while(tries < maxTries):
    if(theNumberGuessed != myRandomNumber):
        print("Incorrect : try again !")
        tries = tries + 1
        theNumberGuessed = int(input("Guess again ! :"))
        if(theNumberGuessed == myRandomNumber):
            print("Woohooo !!")
            exit(0)


print("Unfortunately all the guesses were wrong !")


#What if we enter numbers outside the range
#Make a way to continue playing the game
