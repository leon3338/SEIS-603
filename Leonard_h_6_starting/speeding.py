#
# speeding.py -> H6-2
#

# fine is:
# $50 plus $5 for each mph over the limit,
# plus a penalty of $200 for any speed over 90 mph.
# Assume that the limit is less than 90 mph.
# Speed limit will be 60
# finish this!

def speeding_fine(speed,limit):

    fine = 0
    if speed > limit:
        fine = (speed - limit) * 5 + 50

        if speed > 90:
            fine = (speed - limit) * 5 + 50 +200
            return fine
    else:
        print("Speed is legal")

def main():
    n = input("enter a speed a s a float: ")
    speed = float(n)
    print("your fine is: $", speeding_fine(speed, 60))


main()
# def test_speed_60_limit_60():
#     assert speeding_fine(60,60) == 0
# def test_speed_87_limit_60():
#     assert speeding_fine(87,60) == (87-60)*5 +50
# def test_speed_90_limit_60():
#     assert speeding_fine(90,60) == (90-60)*5 +50
# def test_speed_91_limit_60():
#     assert speeding_fine(91,60) == 50+(91-60)*5 + 200