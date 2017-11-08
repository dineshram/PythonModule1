
birthYear = int(input("Enter your birth year"))

if(birthYear <= 1900):
    print("Thats too old !")
    exit(0)

currentYear = int(input("What year are we in now?"))

if(birthYear > currentYear):
    print("You are not yet born !")
    exit(0)

yearIEntered = int(input("Enter a year"))

if(yearIEntered < birthYear):
    print("I cannot calculate your age in the past !")
    exit(0)

print("My age in ", yearIEntered, " will be:", yearIEntered-birthYear)


#Tasks for homework
# 1) What if its a new born baby? Greet him/her :)
# 2) What if someone's age comes up as 100 ! Congratulate him/her
# 3) What if someone's age is between 13 and 19? Say hello to the teenager
# 4) If the person is 10, 20, 30, 40.... invite them to a new decade
# 5) If the person's age is a prime number, tell them about it
# 6) Add up the digits in their birth year
