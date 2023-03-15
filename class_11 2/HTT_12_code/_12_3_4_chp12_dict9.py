#
# HTT Ch 12 code example:
#
# Section 12.3, example 4: chp12_dict9
#

print()

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print('apples' in inventory)
print('cherries' in inventory)

del inventory['bananas']

if 'bananas' in inventory:
    print(inventory['bananas'])
else:
    print("We have no bananas")

print(inventory)