#
# HTT Ch 13 code example:
#
# Section 13.2.1, example 4: exceptions_4
#
try:
    items = ['a', 'b']
    third = items[2]
    print("This won't print")
except IndexError:
    print("error 1")

print("continuing")

try:
    x = 5
    y = x/0 # this tries to divide by 0, which throws an exception...
    print("This won't print, either") # causing this statement to be skipped!
except IndexError: # not handled here since ZeroDivisionError is not directly related to IndexError
    print("error 2") # not executed: ZDError is rethrown to caller of this (here, Python runtime)

print("continuing again") # never reached: Python runtime ignores code after place where thrown
