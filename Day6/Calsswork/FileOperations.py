
#reading a file

def readMyDataFile(dataFileName):
    with open(dataFileName, mode='r') as myDataFile:
        print(type(myDataFile))
        items = myDataFile.read().splitlines()
        return items

#readMyDataFile()

def writeDataToMyFile(shoppingList):
    with open("shopping.txt", 'w') as myDataFile:
        for item in shoppingList:
            myDataFile.write(item+'\n')


shoppingList = ['Apple', 'Soap', 'Tacos']
writeDataToMyFile(shoppingList)

def seeIfItemExists(myItem):
    myShoppingList = readMyDataFile('shopping.txt')
    for item in myShoppingList:
        if item == myItem:
            print(myItem, "Exists in my shopping list")
            return

    print(myItem, " Does not exist in my shopping list")


seeIfItemExists("Orange")

def checkPassword(userName):
    data = readMyDataFile("userCredentials.txt")
    print(data)
    for user in data:
        userCred = user.split(';')
        print(userCred)
        if(userCred[0] == userName):
            print("Type password for", userName)
            userPass = input()
            if(userPass == userCred[1]):
                print("The Password is correct")
            else:
                print("The password for" , userName, " is incorrect")

checkPassword("Dinesh")
