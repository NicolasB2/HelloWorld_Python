# example about class with methods
from signal import default_int_handler


class MyClass:
    variable = "blah"

    def function(self,by):
        print("This is a message inside the class \nThis class was developed by %s"%(by))

x = MyClass()
y = MyClass()

y.variable = "yackity"

print(x.variable)
print(y.variable)
x.function("nicolas")

# example about a class whit args
class car:

    def __init__(self,marca,nombre,precio):
        self.marca = marca
        self.nombre = nombre
        self.precio = precio

    def funtion(self):
        print ("El carro de la marca %s %s cuesta: %s"%(self.marca,self.nombre,self.precio))


mycar = car("lamborghini","veneno","12345")
mycar.funtion()