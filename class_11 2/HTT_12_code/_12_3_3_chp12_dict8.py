#
# HTT Ch 12 code example:
#
# Section 12.3, example 3: chp12_dict8
#

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 430}

print()
print(list(inventory.values()))
print(list(inventory.items()))

for (k,v) in inventory.items():
    print("Got", k, "that maps to", v)

for k in inventory:
    print("Got", k, "that maps to", inventory[k])

print(inventory)