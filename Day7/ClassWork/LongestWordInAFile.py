def longest_word(filename):
    with open(filename, 'r') as infile:
        words = infile.read().split()
        print(words, type(words))
        #max_len = len(max(words, key=len))
    #return [word for word in words if len(word) == max_len]

print(longest_word('shopping.txt'))


def listMax(myList):
    max = 0
    for i in range(0,len(myList)):
        if myList[i] > max:
            max = myList[i]

    return max

maxOfList = listMax([1, 5, 2, 4, 8, 9, 0, 15, 7])
print("Max number in the given list is :", maxOfList)



