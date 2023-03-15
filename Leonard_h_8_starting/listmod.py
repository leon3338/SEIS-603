#Andrew Leonard
#  listmod.py -> H8-2
#

# read my_list using eval()
my_list = eval(input("Enter values to create a list: "))
# print id(my_list)
print(id(my_list))
print(my_list)
# insert 47 as first elt of my_list
my_list[0:0] = [47]
# add 47 to end of my_list
my_list.append(47)
# print id(my_list) again
print(id(my_list))

print(my_list)