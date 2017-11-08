theYearIEntered = int(input("Please enter a year in the future"))
theYearIWasBornIn = int(input("Please enter the year in which you were born"))

print(type(theYearIEntered))
print(type(theYearIWasBornIn))


print("My age in", theYearIEntered, " will be", theYearIEntered-theYearIWasBornIn)

#Tests
# 1) Entered a string - breaks
# 2) Enter a decimal - breaks
# 3) Empty string - breaks
# 4) a space - breaks
