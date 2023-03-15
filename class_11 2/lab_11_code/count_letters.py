#
#  count_letters.py -> L11-3
#

# read a string from user:

to_count = input("Input a string: ")

print (to_count)

# initialize counting dictionary

counting_dict = {}

# iterate over each char in to_count, updating counts in counting_dict

for ch in to_count:
    if ch in counting_dict:
        counting_dict[ch] = counting_dict[ch] + 1
    else:
        counting_dict[ch] = 1

for (k,v) in counting_dict.items():
    print (f"'{k}' - {v}")

# get keys from dict, turn into list, and sort

all_keys = list(counting_dict.keys())

all_keys.sort()

# for each key in sorted dict, print out line: f"'{key}' - {value}"

for k in all_keys:
    print (f"'{k}' - {counting_dict[k]}")

print (counting_dict)
