l = [1, 2, [1, 2, 5]]

for i in range (0, len(l)):
    print(type(l[i]))
    if(isinstance(l[i], list)):
        print(l[i])
