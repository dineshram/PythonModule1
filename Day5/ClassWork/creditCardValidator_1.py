


myCreditCardNumber = input("Enter a credit card number")

if(len(myCreditCardNumber) != 16):
    print("The number should be 16 digits long")

doubleOfDigits = []

def doubleAlternateDigits(number):
    for i in range(0, len(number)):
        if(i % 2 == 0):
            doubleOfDigits.append(int(number[i])*2)

doubleAlternateDigits(myCreditCardNumber)

print("Double of Alternate Digits is ", doubleOfDigits)

def addDigits(number):
    sumOfDigits = 0
    while number > 0:
        sumOfDigits = sumOfDigits + number % 10
        number = number // 10

    return sumOfDigits
    #print("The sum of digits is ", sumOfDigits)

normalizedAlternateNumbers = []

def validationStep2():
    for i in range(0, len(doubleOfDigits)):
        if(doubleOfDigits[i] >= 10):
            result = addDigits(doubleOfDigits[i])
            normalizedAlternateNumbers.append(result)
        else:
            normalizedAlternateNumbers.append(doubleOfDigits[i])

validationStep2()
print("Normalized alternate numbers are ", normalizedAlternateNumbers)

def validationStep3():
    sumOfAllDigits = 0
    for i in range(0, len(normalizedAlternateNumbers)):
        sumOfAllDigits += normalizedAlternateNumbers[i]
    return sumOfAllDigits

sumOfAllDigits = validationStep3()
print("The sum of all normalized digits is ", sumOfAllDigits)

if(sumOfAllDigits % 10 == 0):
    print("The credit card number is valid")
else:
    print("The credit card number is not valid")
