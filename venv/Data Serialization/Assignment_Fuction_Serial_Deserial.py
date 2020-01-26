import pickle
import json

def serialize(pythonObj, fileName, serializeType):
    if serializeType == 'pickle':
        with open(f'{fileName}.dat','wb') as file:
            pickle.dump(pythonObj, file)

    elif serializeType == 'json':
        with open(f'{fileName}.json', 'w') as file:
            json.dump(pythonObj, file, indent=4)
    else:
        print ("ERROR")


#Testing
friend = {"Raunaq": [24, "India"]}
fileName = "serialize"
serializeType1 = "pickle"
serializeType2 = "json"


#Serializing the python object
serialize(friend, fileName, serializeType1)
serialize(friend, fileName, serializeType2)




def deserialize(fileName, serializeType):
    if serializeType == 'pickle':
        with open(f'{fileName}.dat','rb') as file:
            content = pickle.load(file)
        print(content)
    elif serializeType == 'json':
        with open(f'{fileName}.json', 'r') as file:
            content = json.load(file)
        print(content)
    else:
        print ("ERROR")


#Testing
fileName = "serialize"
serializeType1 = "pickle"
serializeType2 = "json"
deserialize(fileName, serializeType1)
deserialize(fileName, serializeType2)