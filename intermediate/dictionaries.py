# first option to add elements
phonebook = {}
phonebook["Nico"] = 19
phonebook["Sara"] = 22
phonebook["Dani"] = 19
phonebook["Deib"] = 20
print(phonebook)


# second option to add elements
phonebook = {
    "Nico" : 19,
    "Sara" : 22,
    "Dani" : 19,
    "Deib" : 20
}
print(phonebook)


#remove and pool
del phonebook["Dani"]
phonebook.pop("Sara")
print(phonebook)


# print with for
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))