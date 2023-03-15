#
# blackjack.py -> L12-4
#

import deck

TRIALS = 100000


def main():

    blackjack_count = 0 # accumulator of # of blackjack hands

    for count in range(TRIALS):

        new_deck = deck.Deck()
        new_deck.shuffle()

        # finish this...

        hand1 = []
        hand2 = []

        # deal from new_deck and add to hand1
        # deal again from new_deck and add to hand2
        # deal third card and add to hand1
        # deal fourth card and add to hand2

        # if hand1's cards form a Blackjack (one Ace plus
        #   one face/10 card at the same time,
        #   hand2's cards are also Blackjack,
        #       so add 1 to blackjack_count

    print (blackjack_count)

    print ("Percentage of blackjacks:", 100.0*blackjack_count/TRIALS)


main()