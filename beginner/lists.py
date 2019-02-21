#first example
my_list = []
my_list.append(1)
my_list.append(2)
my_list.append(3)
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(" ")

#second example
my_list = [4,5,6]
for x in my_list:
    print(x)
print(" ");

#third example
numbers = []
strings = []
names = ["Nicolas", "Daniela", "Sara", "David"]

numbers.append(7)
numbers.append(8)
numbers.append(9)

strings.append("hello")
strings.append("world")

print(numbers)
print(strings)
print(names);

#Added two list
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

#Multiplicated a list
print([1,2,3] * 3)