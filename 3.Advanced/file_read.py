#open file for reading : f = open("file.txt", "r")

#'Hel'
f = open('../sources/read.txt')
dato1 = f.read(3)
print(dato1)
f.close()

#'Hello\n'
g = open('../sources/read.txt')
dato2 = g.readline()
print(dato2)
g.close()

#'Hello\nWord\n'
h = open('../sources/read.txt')
dato3 = h.read()
print (dato3)
h.close()
