#Multiple arguments
def arguments(first, second, third):
    print(first)
    print(second)
    print(third)
arguments("hello","whats","new")
print

#Rest of Arguments
def foo(first, second, third, *therest):
    print("First: %s" %(first))
    print("Second: %s" %(second))
    print("Third: %s" %(third))
    print("And all the rest... %s" %(list(therest)))
foo(1,2,3,4,5)
print
