#
# doublespace.py -> h9-3
#

# Hint: modify copyfile.py from Lab 9

fname = input("Enter a file that you want to copy: ")

infile = open(fname, "r")

outfile = open("double_"+fname, "w")

for line in infile:
    outfile.write(line + "\n")


infile.close()
outfile.close()
