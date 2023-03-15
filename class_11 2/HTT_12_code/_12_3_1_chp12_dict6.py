#
# HTT Ch 12 code example:
#
# Section 12.3, example 1: chp12_dict6
#

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

for akey in inventory.keys():     # the order in which we get the keys is not defined
   print("Got key", akey, "which maps to value", inventory[akey])

ks = list(inventory.keys())
print(ks)

print(inventory)