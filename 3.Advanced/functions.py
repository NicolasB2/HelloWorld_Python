from datetime import date
from functools import partial

#Partials
def multiply(x,y):#Multiply function
        return x * y

dbl = partial(multiply,2)# create a new function that multiplies by 2
print(dbl(5))

dbl = partial(multiply,3)# create a new function that multiplies by 3
print(dbl(5))

dbl = partial(multiply,5)# create a new function that multiplies by 5
print(dbl(5))

def func(u,v,w,x):#Funtion
    return u*4 + v*3 + w*2 + x

p = partial(func,5,6,7)#Remplace function
print(p(8))

print


#Closures
def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)
    data_transmitter()
transmit_to_space("Start mition")


def transmit_to_space(message):
  "This is the enclosing function"
  def data_transmitter():
      "The nested function"
      print(message)
  return data_transmitter

fun2 = transmit_to_space("Burn the Sun!")
#"Satart transmition like method"
fun2()


def multiplier_of(n):
    def multiplier(number):
        return number*n
    return multiplier

#Create multiplier_of with 5
multiply= multiplier_of(5)
#Start method multiplier with nine
print(multiply(9))
