#Andrew Leonard
#   dict2list.py -> h10-1
#

#  finish this...


inputdict = eval(input("enter a dictionary to create: "))

for key, value in inputdict.items():
    print(key, value)

print(list(inputdict.items()))


