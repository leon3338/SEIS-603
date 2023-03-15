# Andrew Leonard
# whilesum.py -> H7-1
#
total = 0
moreInts = True
while moreInts:
    num = int(input('Enter an integer(0 when you are done): '))
    if num > 0:
        total = total + num
    else:
        print('The sum of these integers is: ', total)
        break
