'''

1. Dictionaries are used to store data values in key:value pairs.

2. A dictionary is a collection which is ordered*, changeable 
   and do not allow duplicates.

3. Dictionaries are changeable, meaning that we can change, add 
   or remove items after the dictionary has been created.

4. Dictionaries cannot have two items with the same key:

'''

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict["brand"])

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

'''

1. The keys() method will return a list of all the keys in the dictionary.
2. The items() method will return each item in a dictionary, as tuples in a list.

'''


x = thisdict.items()

print(x)
print(thisdict.keys())
print(thisdict.values())

