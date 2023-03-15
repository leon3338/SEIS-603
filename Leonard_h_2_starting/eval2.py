#Andrew Leonard
# eval2.py -> h2-2
#

print (1.0 + 2.0 * 2 ** 3 ** 2 % 3 - 6 // 4) # equal to 1.0

### 1.0 + 2.0 * 2 ** 3 ** 2 % 3 - 6 // 4 => original expression

temp1 = 3 ** 2

### 1.0 + 2.0 * 2 ** temp1 % 3 - 6 // 4 => reduced expression

temp2 = 2 ** temp1

### 1.0 + 2.0 * temp2 % 3 - 6 // 4 => reduced expression

temp3 = 2.0 * temp2
### 1.0 + temp3 % 3 - 6 // 4 => reduced expression
temp4 = temp3 % 3
### 1.0 + temp4 - 6 // 4 => reduced expression
temp5 = 6//4
### 1.0 + temp4 - temp5 => reduced expression
temp6 = 1 + temp4

result = temp6 - temp5
print(type(result))

print(result)

# you finish the rest!