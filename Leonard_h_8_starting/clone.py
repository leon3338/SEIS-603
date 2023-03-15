#Andrew Leonard
#  inplace.py -> H8-1
#

# try cloning a list w/ [:]
# compare list with its clone using is
sample_list = ['andrew', 'robert',  'leonard']
elt = sample_list[:]
print(sample_list is elt)
# try cloning a string w/ [:]
# compare string with its attempted clone using is
sample_string = 'this is an example of a string'
elt = sample_string
print(sample_string is elt)

# try cloning a tuple w/ [:]
# compare tuple with its attempted clone using is
tuple_list = (8,13,93)

elt = tuple_list

print(tuple_list is elt)