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

#split and count characters
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]
print(words)
print(word_lengths)

#select only the numbers wich to carry out the conditional
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [int(x) for x in numbers if x > 0]
print(newlist)