#
# boolexpr.py -> H6-1
#

# Spring 2022 semester started 2/1, ends 5/13

def is_in_semester(month,day):
    if month < 2 or month > 4:
        return False
    #check for all-spring months
    if month == 2 or month == 3 or month == 4:
        return True
    if month == 5:
        if day >= 13:
            return True
        else:
            return False



def main():

    # read month, day as ints

    n = input("Enter a month: ")
    j = input("Enter a day: ")
    month = int(n)
    day = int(j)
    # if is_in_semester(month,day) returns True,
    #   print 'month/day is in Fall Semester'
    # if it returns False,
    #   print 'month/day is NOT in Fall Semester'

    if is_in_semester(month,day):
        print (f"{month}/{day} is in Spring Semester")
    else:
        print (f"{month}/{day} is not Spring Semester")

    # here's how to print the result using an f-string:



main()