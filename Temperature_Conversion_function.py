

#defining a function
def celciusToFahrenheit():
    myInput = int(input("Enter a temperature in Celcius : "))
    tempInFahrenheit = (myInput*9 + 160) / 5
    print("The temp of " , myInput , "in celcius is " ,
          tempInFahrenheit , "in Fahreiheit")


def fahrenheitToCelcius():
    myInput = int(input("Enter a temperature in Fahrenheit : "))
    tempInCelcius = ((myInput - 32)/9)*5
    print("The temp of " , myInput , "in fahrenheit is" ,
          tempInCelcius , "in Celcius")

optionSelected = input("Enter 'c' for output in celcius and"
                       "Enter 'f' for output in fahrenheit")
#calling a function
if(optionSelected == 'c'):
    fahrenheitToCelcius()
elif(optionSelected == 'f'):
    celciusToFahrenheit()
else:
    print("You selected an invalid option")

