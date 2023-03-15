import random

SIZE = 100

# generate a list to_search of length SIZE, such that
#  each element has random int in range(2*SIZE)

to_search = []
for index in range(SIZE):
    to_search.append(random.randrange(2 * SIZE))

# randomize it!

random.shuffle(to_search)

# build dictionary dict_search with
#    dict_search[i] = to_search[i]
# for i in range(SIZE)

dict_search = {}

for index, elt in enumerate(to_search):
    dict_search[index] = elt

to_find = random.randrange(2 * SIZE)
print (f'searching for {to_find}')

# print(to_find)
#### search using linear search

foundit = False
for index,elt in enumerate(to_search):
    if elt==to_find:
        print (f'found it at {index}')
        foundit = True
        break
if not foundit:
    print ("not found.")

#### search using binary search

# sort into ascending order
to_search.sort()
# to_find = 75

foundit = False
upper = SIZE - 1
lower = 0
while upper >= lower:
    guess = (upper + lower) // 2  # middle elt between upper, lower bounds
    if to_search[guess] == to_find:
        print(f"found it @ to_search[{guess}]")
        foundit = True
        break
    elif to_search[guess] < to_find:
        lower = guess + 1
    else:
        upper = guess - 1

if not foundit:
    print("not found.")