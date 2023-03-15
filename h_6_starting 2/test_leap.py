#
# testleap.py -> H6-4
#

# algorithm for leap year:
'''
(a) if year evenly divisible by 400 (year%400==0), return True
(b) if not by 400 but by 100, return False
(c) if neither of the above but evenly divisible by 4, return True
(d) if none of the above, return False

if (a):
    return True
elif (b):  note you only need to check if year%100==0 since (a) is False
    return False
elif (c):
    return True
else: (d)
    return False
'''

def is_leap(year):
    pass
    # finish this

def test_leap_2020():
    assert is_leap(2020) == True

# add 9 more PyTest test functions below