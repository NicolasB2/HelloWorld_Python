# Define a function
def my_function():
    print("Hello From My Function!")
my_function()


# Define a function with args
def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))
my_function_with_args("nicolas", "a great year!")


# Define a function whit returns
def sum_two_numbers(a, b , c):
    return (a + b)**c
print (sum_two_numbers(1,2,3))