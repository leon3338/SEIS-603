#
#  anagrams.py -> L10-4
#

'''
Find and print all words in the largest set of words that are all anagrams of each other
    == "anagram lists"

Starting code follows...

You will find the following operations useful:

    charlist = list(string) => create a list of single chars in string
    word = ''.join(charlist) => join charlist back into a word

'''


def make_sorted(word):
    '''
    Build and return a new string with each of word's chars
      in sorted order, using list() and list's join method
    '''

    # turn word into a list of individual chars

    char_list = list(word)

    # sort the list (in place)

    char_list.sort()

    # join the now-sorted letters back into a single string to_return

    to_return = ''.join(char_list)

    # return to_return

    return to_return


# open .txt file for reading (the 'dictionary of words')

word_file = open("words.txt", "r")

# Initialize anagrams as empty dict

anagrams = {}

for word in word_file:  # for each word (== a line from external .txt dictionary)...

    # Strip trailing newline from word (word.rstrip() also works here)

    word = word[:-1]

    # Create alpha_sort: string with sorted chars in stripped word

    alpha_sort = make_sorted(word)

    # print (alpha_sort)
    # complete the following:

    # if string alpha_sort already in anagrams dictionary as key:

    if alpha_sort in anagrams:
        anagrams[alpha_sort].append(word)
    else:
        anagrams[alpha_sort] = [ word ]

    #   Append stripped word to anagrams[alpha_sort]
    #     (add word to list of all words having same chars)

    # else:
    #   Set anagrams[alpha_sort] to new list containing
    #     single stripped word ([word])

    # shortcut for previous if-else:
    # anagrams[alpha_sort] = anagrams.get(alpha_sort,[]).append(word)

print(anagrams)

input("Press ENTER to continue:") # pause to allow browsing of output

word_file.close()

# Here, the dictionary anagrams has all "anagram lists" for dictionary:
# Now build tuple w/ first int elt as length of value list,
#   2nd as value list: (len(value_list), value_list)

anagram_freq = []

# for each value in dictionary's values:
#      append ((len(v),v)) to anagram_freq

for value_list in anagrams.values():
    anagram_freq.append((len(value_list), value_list))

# sort anagram_freq in reverse order, ordering by length of list v

anagram_freq.sort(reverse=True)

# print first 20 values (longest anagram lists first) of anagram_freq (slices!)

for elt in anagram_freq[:20]:
    print(elt)


