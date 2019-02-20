print ("Write the letter corresponding to the operation you want")
print ("plus -> p")
print ("minus -> m")
print ("divide -> d")
print ("multiply -> x")

while 1<2:
    request = raw_input();

    if request == "p":
        print ("Enter the first number")
        x = input()
        print ("Enter the second number")
        y = input()
        print (x+y)

    if request == "m":
        print ("Enter the first number")
        x = input()
        print ("Enter the second number")
        y = input()
        print (x-y)

    if request == "d":
        print ("Enter the first number")
        x = input()
        print ("Enter the second number")
        y = input()
        print (x/y)

    if request == "x":
        print ("Enter the first number")
        x = input()
        print ("Enter the second number")
        y = input()
        print (x*y)