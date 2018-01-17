
#reading a file

def readMyDataFile(dataFileName):
    with open(dataFileName, mode='r') as myDataFile:
        print(type(myDataFile))
        items = myDataFile.read().splitlines()
        print(items)
        return items

items = readMyDataFile("shopping.txt")

def findLongestShoppingItem(myList):
   longestItemSize = 0
   longestItem = ""

   for i in range(0, len(myList)):
       if longestItemSize < len(myList[i]):
           longestItemSize = len(myList[i])
           longestItem = myList[i]
           print("MaxNumber now is :", longestItemSize)

   return longestItem

print(findLongestShoppingItem(items))

#Write a function to count the
#number of occurances of a word in a file


def writeDataToMyFile(shoppingList):
    with open("shopping.txt", 'w') as myDataFile:
        for item in shoppingList:
            myDataFile.write(item+'\n')


shoppingList = ['Apple', 'Soap', 'Tacos']
#writeDataToMyFile(shoppingList)

def seeIfItemExists(myItem):
    myShoppingList = readMyDataFile('shopping.txt')
    for item in myShoppingList:
        if item == myItem:
            print(myItem, "Exists in my shopping list")
            return

    print(myItem, " Does not exist in my shopping list")


#seeIfItemExists("Orange")

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

#checkPassword("Dinesh")
