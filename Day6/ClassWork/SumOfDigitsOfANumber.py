
myNumber = int(input("Enter a number"))
print(type(myNumber))

sumOfDigits = 0

while myNumber > 0:
    sumOfDigits = sumOfDigits + myNumber % 10
    myNumber = int(myNumber / 10)
    print("sumOfDigits =", sumOfDigits, " myNumber = ", myNumber)

print("Sum of Digits is", sumOfDigits)
