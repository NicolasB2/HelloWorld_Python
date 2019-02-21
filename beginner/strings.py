#concatenate strings
hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)
print("")

#multiplicated strings
hellos = "hello" * 10
print(hellos)
print("")

#formate like this: "Hello, John!"
name = "John"
print("Hello, %s!" % name)
print("")

# formate like this: "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old." % (name, age))
print("")

#formate like this: "A list: [1, 2, 3]"
mylist = [1,2,3]
print("A list: %s" % mylist)
print("")

#formate like this: "Hello John doe. Your current balance is 53.44."
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."
print(format_string % data)
print("")

#count characters
astring = "Hello world!"
print(len(astring))

#get a index of first char
print(astring.index("o"))

#count especific character
print(astring.count("l"))

#get a sub string
print(astring[3:7])

#reverse de string
print(astring[::-1])

#Uppercase and lowercase
print(astring.upper())
print(astring.lower())

#starts and end with
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))

#