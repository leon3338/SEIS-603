#
# count_blanks.py -> h9-2
#

# read the filename from the user
infile = input("please enter a file name: ")
# open the file for reading
myfile = open(infile, "r")
# read in contents of file as single string
astr = myfile.read()
# count number of ' ' in your string
print(astr.count(' '))
# print the result
