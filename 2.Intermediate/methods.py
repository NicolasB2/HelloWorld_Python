# Define a function
def my_function():
    print("Hello From My Function!")
my_function()


# Define a function with args
def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))
my_function_with_args("nicolas", "a great year!")


# Define a function whit returns
def sum_two_numbers(a, b):
    return (a + b)
print (sum_two_numbers(1,2))


# Define a function whit a lot parameters
def foo(first, second, third, *therest):
    print("First: %s" %(first))
    print("Second: %s" %(second))
    print("Third: %s" %(third))
    print("And all the rest... %s" %(list(therest)))

foo(1,2,3,4,5)


# Send functions arguments by keyword
def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" %(first + second + third))

    if options.get("number") == "first":
        return first

result = bar(1, 2, 3, action = "sum", number = "first")
print("Result: %d" %(result))