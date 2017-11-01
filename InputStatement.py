#here we want to take an input from the user

print("Please enter the radius of the circle :")
radius = float(input())
print("You have entered a radius of", radius)

if(radius < 0):
    print("The radius of a circle cannot be a negative number")


myConstPi = 3.14

print("The circumference of the circle is :", 2*myConstPi*radius)
