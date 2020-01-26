#Firstly, import pickle

import pickle
"""SERIALIZATION"""
#Dumping a python object to a file in binary format using pickle
friend1 = {"Raunaq": [24, "India"]}
friend2 = {"Milony": [25, "United States"]}
friends = (friend1, friend2)

with open('friends.dat','wb') as file:
    pickle.dump(friends, file)

"""DESERIALIZATION"""
#Reconstucting the python object from the binary file

with open('friends.dat','rb') as file:
    content = pickle.load(file)

print (content)

