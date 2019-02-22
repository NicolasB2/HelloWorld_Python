# yield save a retorn a generator with all instaneces of n
def contador(max):
    n=0
    while n < max:
            yield n
            n=n+1

mycont = contador(5)
for i in mycont:
    print(i)