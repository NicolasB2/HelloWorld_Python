import json
import pickle

#JSON is human-readable
json_string = json.dumps([1, 2, 3])
g = open("../sources/json.txt","w")
g.write(json_string)
g.close()

x = json.loads(json_string)
x.append(4)
x.append(5)
x.append(6)
print x

#PICKLED is human-unredable
pickle_string = pickle.dumps(["a", "b", "c"])
f = open("../sources/pickle.txt","w")
f.write(pickle_string)
f.close()

y = pickle.loads(pickle_string)
y.append('d')
y.append('e')
y.append('f')
print y
