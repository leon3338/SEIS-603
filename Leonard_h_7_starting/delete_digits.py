#Andrew Leonard
# delete_digits.py -> H7-3
#

def del_digits(str1):
    digitsremoved = ''.join(i for i in str1 if not i.isdigit())
    #iteration through string adding non-ints to result
    #checks if char is a base 10 digit and excludes from new string
    return digitsremoved

def main():


    # prompt and read a str
    st = input("Enter a string(any digits included will be removed): ")

    # call del_digits(str1), passing entered str
    print(del_digits(st))
    # print out result

main()