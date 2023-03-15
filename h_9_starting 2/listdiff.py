#
# listdiff.py -> h9-1
#

def diff (list1,list2):
    to_return = [] # accumulate elements to return

    # iterate over list1

    for elt1 in list1:
        pass


    for elt2 in list2:
        pass

    return to_return

    # Return list containing all
    # TOP-LEVEL ELEMENTS of either
    # list1 or list2 that do NOT
    # appear as a top-level element
    # in the OTHER list

    # Hint: iterate over each elt of list1,
    #   accumulating in the list to_return those
    #   list1 elts that DON'T occur in list2 (and what else)?
    #   Then iterate over list2, doing the same.
    #

print (diff([1,4,2,1,3,2],[1,4,5]))

# Should print [2,3,5]:
#   Note we must remove the duplicate 2 found in list1