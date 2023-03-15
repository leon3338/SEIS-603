#
# eval1.py -> h2-1
#

# an example follows...
# print (44 + 1 - 2 / (3 - 4))
### 44 + 1 - 2 / (3 - 4) => expression to reduce
# temp1 = 3 - 4
### 44 + 1 - 2 / temp1 => reduced by substituting new variable
# temp2 = 2 / temp1
### 44 + 1 - temp2 => reduced again
# temp3 = 44 + 1
### temp3 - temp2 => reduced again
# result = temp3 - temp2
### result is final reduction!
# print (result)

print (2+(3-1)*10/5*(2+3))

temp1 = 3-1

### 2+temp1*10/5*(2+3) => reduced expression

temp2 = 2 + 3

### 2+temp1*10/5*temp2  => reduced expression

# you finish the rest!