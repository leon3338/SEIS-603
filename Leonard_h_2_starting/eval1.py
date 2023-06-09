#Andrew Leonard
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

temp3 = temp1*10
### 2+temp3/5*temp2 => reduced expression

temp4 = temp3/5
### 2+temp4*temp2 => reduced expression
temp5 = temp4 * temp2
### 2+temp5 => reduced expression
result = 2 + temp5

print(result)

