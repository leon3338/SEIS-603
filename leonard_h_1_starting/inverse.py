#Andrew Leonard
# inverse.py -> h1-3
#
prompt = input("enter an integer:")
i = int(prompt)

#when using the input option, items are taken in as a string
print("Here's your input as a string: ", prompt)
print(type(prompt))

#it you want to utilize an input as something like an integer, you need to conver it to that type
print("Here's your input as an integer:", i)
print(type(i))

#while both print statements will let you know that your input is whatever you enter, the type gets transformed
#in the second set of statements.
