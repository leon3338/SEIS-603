#
#  inplace.py -> H8-4
#

def squeeze(alist,elt):
    while elt in alist:
        alist.remove(elt)

def main():
    alist = eval(input("Enter a list: "))
    print("Your list is", alist)

    # read a list and an element to remove using eval()
    elt = eval(input("Enter an element to remove: "))
    print("The element you are going to remove is ", elt)

    # call squeeze(alist,elt) and print returned result
    squeeze(alist,elt)

    print("your new list", alist)
main()