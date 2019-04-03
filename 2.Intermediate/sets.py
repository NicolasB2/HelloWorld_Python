# add elements in a set
a = set()
b = set ()
a.add("Sara")
a.add("Nicolas")
a.add("David")
b.add("Daniela")
b.add("Wilmer")
print(a)
print(b)


# inicialize a set
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])
print(a)
print(b)


# intersection between set a and b
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])
print(a.intersection(b))
print(b.intersection(a))


# Union between set a and b
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])
print(a.union(b))
print(b.union(a))


# element that differentiates the set from another
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])
print(a.difference(b))
print(b.difference(a))


# diferents elements of sets
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))