# Andrew Leonard
#  count_alice2.py -> H8-5 EXTRA CREDIT
#

# copy your L9-8 code into here,
#   then follow instructions in H8-5

FILENAME = 'alice.txt'

fvar = open(FILENAME, 'r')  # open file for reading

allwords = []  # accumulate the words in this list

for aline in fvar:

    # lower case each line

    aline = aline.lower()

    # remove punctuation (except single quotes '): replace each by ' ' (single blank)
    aline = aline.replace("--", " ").replace(".", " ").replace(",", " ").replace("(", " " ).replace(")", " ")
    aline = aline.replace(":", " ").replace(";", " ").replace("?", " ").replace("!", " ").replace("@", " ")
    aline = aline.replace("%", " ").replace("^", " ").replace("&", " ").replace("*", " ").replace("-", " ")
    aline = aline.replace("-", " ").replace("_", " ").replace("+", " ").replace("=", " ").replace("/", " ")
    aline = aline.replace("<", " ").replace(">", " ").replace("~", " ").replace("\"", " ").replace("[", " ")
    aline = aline.replace("]", " ")
    # split the line on whitespace (blanks, '\n', '\t') to obtain aline_list
    #   of words in the current line
    aline_list = aline.split()
    #print(aline_list)
    # add each string st in aline_list to allwords

    allwords = allwords + aline_list
    # for st in aline_list:

    # several ways of doing this:
    # 1. append st to allwords
    # 2. concatenate [st] to allwords
    # 3. use the list method extend()

print (allwords)
print (f'The number of words is {len(allwords)}')

# Extra:
#
#  the following is one approach to handling single quotes:
#   iterate through allwords, filtering them by modifying
#   each by removing ' if there, but only if not part of
#   contraction within word (eg it's)

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

print (f"Total filtered word count is {len(filtered_allwords)}")

fvar.close()
