#
#  inplace.py -> H8-4
#

# read numbers using eval():

numbers = eval(input("Enter a list of integers: "))

# assume numbers after reading is [1, 2, 3, 4, 5]

numbers_orig = numbers

# your code for doubling numbers in place goes here
numbers[0] = numbers[0]*2
numbers[1] = numbers[1]*2
numbers[2] = numbers[2]*2
numbers[3] = numbers[3]*2
numbers[4] = numbers[4]*2
# printing the string result should give output as [2, 4, 6, 8, 10]

# and after doubling, print (numbers_orig is numbers): should print True
print(numbers)
print(numbers_orig is numbers)
