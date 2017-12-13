


myNumber = int(input("Enter a number"))

def addDigits(number):
    sumOfDigits = 0
    while number > 0:
        sumOfDigits = sumOfDigits + number % 10
        number = number // 10

    print("The sum of digits is ", sumOfDigits)

addDigits(myNumber)
