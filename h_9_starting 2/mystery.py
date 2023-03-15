#
# mystery.py -> h9-4
#

file_ref = open ("myname.txt","r")
aline = file_ref.readline()
bline = file_ref.readline()
cline = file_ref.readline()

print (aline.replace('-','\n')+bline+cline)
file_ref.close()
