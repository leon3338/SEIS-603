#
# traceme.py -> h4-1
#

#
# Run the following in the PyCharm debugger:
#   set breakpoints on each print, and examine value of a,b, and sum
#

import random
random.seed(47)

sum = 0

for b in range(5):
    a = random.randint(1,6)
    sum = sum + a

    print ("set a breakpoint on this line...") # LOCATION 1

print ("set another breakpoint on this line...") # LOCATION 2:

# list values of a, b, and sum at LOCATION 1
#    for each time the loop body is executed

# also list final values of a, b, and sum at LOCATION 2

# put your values within the following triple-quoted string

'''

LOCATION 1:
a = __, b=__, sum=__
<repeat these values for a total of 5 sets of values>

LOCATION 2
a = __, b=__, sum=__

'''


