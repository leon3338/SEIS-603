#
# HTT Ch 12 code example:
#
# Section 12.3, example 5: chp12_dict10
#
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

print(inventory.get("apples"))
print(inventory.get("cherries"))
print(inventory.get("cherries", 0))

print(inventory)