#Andrew Leonard
# patterns2.py -> H7-2ab
#
def triangle(N): # H7-2a

  for i in range(N): #rows
      for j in range(i+1):
          print(' ', end='')
      for j in range(i, N): #columns
          print('*', end='')
      print()

#
# ****
#  ***
#   **
#    *
#


def hollow_box(N): # H7-2b

    for i in range(N):#row
        for j in range(N): #column
            if i==0 or j==0 or i==N-1 or j==N-1:
                print('*', end='')
            else:
                print(' ', end='')
        print()
    # finish this: output for N==4 is below
#
# ****
# *  *
# *  *
# ****
#



def main():

    N = int(input("Enter a integer to determine the size of the shapes: "))

    triangle(N)
    print("\n")#adding some space between the two problems
    hollow_box(N)

main()
