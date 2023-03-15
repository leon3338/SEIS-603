#Andrew Leonard
# pytypes.py -> h2-4
#

print (type(47)) # int
print (type(47.0)) # float
print (type("47")) # str
print (type(True)) #bool
print (type(None)) #Nonetype
print (type(2 + 3j)) #complex
print (type([1, 7, 99])) #list
print (type(("orange", "blue", "green"))) #tuple
print (type(range(4))) #range
print (type({"name": "Andrew", "age": 28})) #dict
print (type(frozenset({"chocolate", "cookies", "icecream"}))) #frozenset
print (type(b"example")) #bytes
print (type(bytearray(4))) #bytearray
print (type(memoryview(bytes(3)))) #memoryview
