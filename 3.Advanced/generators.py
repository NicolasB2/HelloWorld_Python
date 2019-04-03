# yield save a return a generator with all instances of n
def meter(max):
    n=0
    while n < max:
            yield n
            n=n+1

mycont = meter(5)
for i in mycont:
    print(i)
print ("---------")


# example of lottery with yield generator and random
import random
def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield int(random.uniform(1,40))

    # returns a 7th number between 1 and 15
    yield int(random.uniform(1, 15))

for j in lottery():
       print(j)
print ("---------")


# method of fibonacci with yield generator
def fib(num):
    a, b = 1, 1
    x = 0
    while x<num:
        yield a
        a, b = b, a + b
        x+=1

for n in fib(7):
    print (n)
print ("---------")
