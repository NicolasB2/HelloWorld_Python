# yield save a retorn a generator with all instaneces of n
def contador(max):
    n=0
    while n < max:
            yield n
            n=n+1

mycont = contador(5)
for i in mycont:
    print(i)


# example of lotery with yield generator and random
import random
def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield int(random.uniform(1,40))

    # returns a 7th number between 1 and 15
    yield int(random.uniform(1, 15))

for j in lottery():
       print(j)