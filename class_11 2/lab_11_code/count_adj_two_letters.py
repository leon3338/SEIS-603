#
#  count_adj_two_letters.py -> L10-5
#

"""
Demo: count_adj_two_letters.py:

Find and print the two-letter pairs that occur most and least frequently
    in all dictionary words, with top and bottom 10 pairs both listed

Starting code follows...

"""

# open words.txt file for reading (the 'dictionary of words')

word_file = open("words.txt", "r")

# Initialize two empty dicts:
#
#   adjacent_2_counts has strings of two letters as keys, and counts of their
#       occurrence in word_file as values
#
#   words_w_adj_2_counts also has strings of two letters as keys, but each value
#       is a list of all word_file words that contain the two-letter key

adjacent_2_counts = {}
words_w_adj_2_counts = {}

for word in word_file:  # for each word (== a line from words.txt)...

    # trim newline from end of word
    
    word = word[:-1]
    # word = word.rstrip()

    if len(word) < 2:  # words should contain at least 2 chars
        continue  # skip to next loop iteration

    # start with char in word at index start_char, then
    #   extract via slices the pair of letters at word[start_char:start_char+2]

    for start_char in range(len(word) - 1):  # only advance start_char until next-to-last char

        # extract next pair using slice
        pair = word[start_char:start_char+2] # "aa"  # fix this - hint: word[start_char:start_char+2]

        # update the count of pair occurrences in adjacent_2_counts dict by 1
        # adjacent_2_counts[pair] = 0  # fix this
        # if pair in adjacent_2_counts:
        #     adjacent_2_counts[pair] = adjacent_2_counts[pair] + 1
        # else:
        #     adjacent_2_counts[pair] = 1

        adjacent_2_counts[pair] = adjacent_2_counts.get(pair,0) + 1

        # now append this word to words_w_adj_2_counts[pair], thus capturing
        #   all words which contain this pair:

        if pair not in words_w_adj_2_counts:
            # if we haven't seen this pair before, initialize the value
            #   of words_w_adj_2_counts[pair] to a list containing just the word
            words_w_adj_2_counts[pair] = [word]  # fix this:
        else:
            # append word to end of existing list in words_w_adj_2_counts[pair]
            # finish this...
            words_w_adj_2_counts[pair].append(word)



# get all items == (key,value) pairs from adjacent_2_counts dict and listify

items = list(adjacent_2_counts.items())
print(items)

input("ENTER to continue:")  # a way of pausing before doing final calculations

# sort this list into descending order (reverse=True) by 2nd element (count) of each item
#   key= gives an anonymous function that returns the element to sort on (here, count)

items.sort(key=lambda x: x[1], reverse=True) # we'll explain lambda functions in class

# now list the top 10 two-letter combos along with the first 10 words in the list

print('Top 20:\n')
for letter_pair,count in items[:20]:  # first 20 items, sorted by # of occurrences
    print(f'"{letter_pair}" occurs {count} times, with first 10 as follows:')  #
    for word in words_w_adj_2_counts[letter_pair][:10]:
        print('  ', word)

print('Bottom 20:\n')

for item in items[-20:]:  # bottom 20 items, sorted by # of occurrences
    print('"{}" occurs {} times, with first 10 as follows:'.format(item[0], item[1]))
    for word in words_w_adj_2_counts[item[0]][:10]:
        print('   ', word)

word_file.close()
