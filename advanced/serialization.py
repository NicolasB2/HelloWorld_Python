# example with json
import json
json_string = json.dumps([1, 2, 3, "a", "b", "c"])
print(json_string)
"""print ("-----")"""
import pickle
pickled_string = pickle.dumps([1, 2, 3, "a", "b", "c"])
print(pickle.loads(pickled_string))