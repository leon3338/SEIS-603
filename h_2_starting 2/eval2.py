#
# eval2.py -> h2-2
#

print (1.0 + 2.0 * 2 ** 3 ** 2 % 3 - 6 // 4)

### 1.0 + 2.0 * 2 ** 3 ** 2 % 3 - 6 // 4 => original expression

temp1 = 3 ** 2

### 1.0 + 2.0 * 2 ** temp1 % 3 - 6 // 4 => reduced expression

temp2 = 2 ** temp1

### 1.0 + 2.0 * temp2 % 3 - 6 // 4 => reduced expression

# you finish the rest!