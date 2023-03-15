#
#  dict_fun.py -> L11-2
#

# read a dictionary from user:

the_dict = eval(input("Input a dictionary in {...} format: "))

print (the_dict)

# Do each of the following:

# (a)	Iterate over each key in the_dict, printing out one key per line

for k in the_dict.keys():
    print (k)

# (b)	Print out the list containing all keys in the_dict.  (Hint: list(a_dict.keys())

print(list(the_dict.keys()))

# (c)	Iterate over each value in the_dict, printing out one value per line.

for v in the_dict.values():
    print (v)

# (d)	Print out the list containing all values in the_dict

print (list(the_dict.values()))

# (e)	Iterate over each item in a_dict, printing out one item per line.
#       ("Item" is a tuple (key,value)where a_dict[key]==value. )

for (k,v) in the_dict.items():
    print (k,v)
