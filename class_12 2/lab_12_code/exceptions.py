"""

    exceptions.py -> L12-1

    If bad float entered, it will throw a ValueError.

    Finish read_pos_float() so it throws Exception if float <=0.0 is read,
        otherwise return the float

"""


def read_pos_float():
    # Read a string and cast it to float:
    #     (if user enters an invalid float,
    #      what exception is thrown?)
    #
    float_str = float(input("Enter a float > 0.0: "))

    # if > 0.0, return it
    # else throw a new Exception exception

def main():

    while True:
        try:
            returned = read_pos_float()
            print('You entered:', returned)
            break
        except ValueError:  # bad float entered?
            print("not a valid float")
        except Exception:
            print("you must enter a float > 0.0.")

        print ("Please try again...")

    # Note how this indented statement is OUTSIDE and just after the while-loop

    print ("that's all!")

main()
