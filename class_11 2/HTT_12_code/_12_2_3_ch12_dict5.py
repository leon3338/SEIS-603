#
# HTT Ch 12 code example:
#
# Section 12.2, example 3: ch12_dict5 (CodeLens)
#

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
inventory['bananas'] = inventory['bananas'] + 200

numItems = len(inventory)

print('\n', numItems,sep='')
print(inventory)