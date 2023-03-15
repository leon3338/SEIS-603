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
    if year%400==0:
        return True
    elif year%100==0:
        return False
    elif year%4==0:
        return True
    else:
        return False

#pytests
def test_leap_2020():
    assert is_leap(2020) == True
def test_leap_1800():
    assert is_leap(1800) == False
def test_leap_1904():
    assert is_leap(1904) == True
def test_leap_1999():
    assert is_leap(1999) == False
def test_leap_1799():
    assert is_leap(1799) == False
def test_leap_2996():
    assert is_leap(2996) == True
def test_leap_3200():
    assert is_leap(3200) == True
def test_leap_1993():
    assert is_leap(1993) == False
def test_leap_1582():
    assert is_leap(1584) == True
def test_leap_2624():
    assert is_leap(2624) == True
