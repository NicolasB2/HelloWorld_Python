#initialize variables
x = 2
name = "John"
age = 23

#logical expressions
print(x == 2)
print(x == 3)
print(x < 3)

#compare
x = [1,2,3]
y = [1,2,3]

print(x == y)
print(x is y)

#AND  OR  NOT
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

if not (False):
    print ("Your name is not Rick")

#operator in
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

#conditional
if x == 2:
    print("x equals two!")
elif x<2:
    print("x is minor than two.")
else:
    print("x is upper than two.")