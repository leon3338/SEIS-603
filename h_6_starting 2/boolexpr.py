#
# boolexpr.py -> H6-1
#

# Spring 2022 semester started 2/1, ends 5/13

def is_in_semester(month,day):
    # finish this

    return True

def main():

    # read month, day as ints
    month = 9
    day = 8

    # if is_in_semester(month,day) returns True,
    #   print 'month/day is in Fall Semester'
    # if it returns False,
    #   print 'month/day is NOT in Fall Semester'

    if is_in_semester(month,day):
        # print something
        pass
    else:
        # print something else...
        pass

    # here's how to print the result using an f-string:

    print (f"{month}/{day} is in Spring Semester")

main()