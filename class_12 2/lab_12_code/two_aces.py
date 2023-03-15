#
# two_aces.py -> L12-3
#

import deck # this in turns imports card

TRIALS = 100000


def main():
    two_aces_count = 0  # accumulator for no. of times 2 aces are drawn

    for count in range(TRIALS):
        pass
        # complete the following:

        # create a new Deck

        # shuffle the Deck

        # deal card1 from new_deck

        # deal card2 from new_deck

        # if card1 and card2 are both aces,
        #   add 1 to two_aces_count

    print (two_aces_count)
    print (100.0 * two_aces_count / TRIALS)


main()
