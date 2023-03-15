#Andrew Leonard
# errors.py -> h1-2
#

#this is a syntax error, in order to resolve the error you need to either use only double quotes or only single quotes
#for your string
print ("python is a cool language to learn')

#the following code would be a semantic error if your intent was to find what 3 to the power of 2 is.
#while it will give you a result, the function you were looking to perform was incorrect
#the result will not be what you were looking for, instead it should be print(3**2)
print(3*2)

#Infinite loops are an instance of a runtime error where you create a set of conditions that can never be met
while True:
    print("I am an example infinite loop, a type of runtime error")