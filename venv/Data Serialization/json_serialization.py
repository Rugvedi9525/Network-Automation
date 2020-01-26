#Import the json library

import json
'''
Two important json methods for json.dump and json.dumps
json.dump ==> to dump a python object into a text file in json format
json.dumps ==> to convert a python object into string representation of the json format. 
'''
friend1 = {"Raunaq": [24, "India"]}
friend2 = {"Milony": [25, "United States"]}
friends = (friend1, friend2)

'''SERIALIZATION'''

with open('friends.json', 'w') as file:
    json.dump(friends, file, indent=4)

print (json.dumps(friends, indent = 4))

'''DESERIALIZATION'''

'''
Two important methods used for deserialization are
json.load and json.loads
json.load ==> is used to take convert the json format to a python object
json.loads ==> is used to just converted the string representation json to the python object.
JSON doesn't support all of the python data types
Doesnt support set at all, and converts a list or tuple to an array. Dictionary becomes a json object. True to true, False to false, None to null, etc.
'''

with open('friends.json') as file:
    content = json.load(file)

print (content)

content_string = """
[
    {
        "Raunaq": [
            24,
            "India"
        ]
    },
    {
        "Milony": [
            25,
            "United States"
        ]
    }
]
"""

print (json.loads(content_string))

#DISCLAIMER: MAKE SURE YOU NOTICE THAT THE TUPLE HAS BEEN CONVERTED TO AN ARRAY BY JSON





