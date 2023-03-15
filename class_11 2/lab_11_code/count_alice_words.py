#
# count_alice_words.py -> L10-6
#

# we'll complete the #### section below,
#   using a dictionary to count the frequency of each word

FILENAME = 'alice.txt'

fvar = open(FILENAME, 'r')  # open file for reading

allwords = []  # accumulate the words in this list

for aline in fvar:
    # print (aline,end='')
    pass
    # lower case each line
    mod_line = aline.lower().strip()

    # print (mod_line,end='')
    # here we replace each punctuation symbol with '' -- except for single quotes '

    mod_line = mod_line.replace('.',' ')
    mod_line = mod_line.replace('!',' ')
    mod_line = mod_line.replace('?',' ')
    mod_line = mod_line.replace('--',' ')
    mod_line = mod_line.replace('"',' ')
    mod_line = mod_line.replace(',',' ')
    mod_line = mod_line.replace(':',' ')
    mod_line = mod_line.replace('(',' ')
    mod_line = mod_line.replace(')',' ')
    mod_line = mod_line.replace('[',' ')
    mod_line = mod_line.replace(']',' ')
    mod_line = mod_line.replace(';',' ')
    mod_line = mod_line.replace('/',' ')
    mod_line = mod_line.replace('_', ' ')

    # split the line on whitespace (blanks, '\n', '\t') to obtain list words
    #   of words in the current line

    words = mod_line.split()

    # print (words)
    #    print(words)  # just to see the words flying across the screen...

    # add each string in words to allwords: several ways of doing this

    # for each_word in words:
    #     allwords.append(each_word)
    #
    # allwords.append(words)  #wrong: why?
    # (but allwords.extend(words) is a shortcut equivalent

    allwords.extend(words)

# print (allwords)
print (f'The number words is {len(allwords)}')

filtered_allwords = []

for aword in allwords:
    if "'" not in aword:
        filtered_allwords.append(aword)
    elif aword == "'":
        pass # do nothing
    else:
        if aword=="'tis":
            filtered_allwords.append(aword)
            continue # start next loop iteration

        if aword[0]=="'":
            aword = aword[1:] # remove the leading ' from aword

        if aword == "'tis":
            filtered_allwords.append(aword)
            continue  # start next loop iteration

        if aword[-1]=="'":
            aword = aword[:-1]

        filtered_allwords.append(aword)

    # finish with other handling: words with embedded '

filtered_allwords.sort()

for word in filtered_allwords:
    print (word) # one per line
  
print (f"Total word count is {len(filtered_allwords)}")

input(">>>")

####
# now we use a dictionary to keep a count of each word
# in filtered_allwords

word_count = {} # accumulate counts: word is key, # is value

for each_word in filtered_allwords:
    pass
    # check if each_word already a key and add 1 to its value if so
    # else set dictionary[key] to 1

    if each_word in word_count:
        word_count[each_word] = word_count[each_word] + 1
    else:
        word_count[each_word] = 1

# get the keys and turn into a list

word_keys = list(word_count.keys())

# sort the list of keys (words)

word_keys.sort()

# iterate through the list, printing out the word + its count,
#   one per line:  f"{key} - {value}"

for each_key in word_keys:
    print (f"{each_key} - {word_count[each_key]}")

fvar.close()
