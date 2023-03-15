#
# HTT Ch 13 code example:
#
# Section 13.2.1, example 3: exceptions_3
#
try:
    items = ['a', 'b']
    third = items[2]
    print("This won't print")
except Exception:
    print("got an error")

print("continuing")
