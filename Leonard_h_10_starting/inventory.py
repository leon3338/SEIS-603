#Andrew Leonard
#   inventory.py -> h10-2
#
#   Complete this to implement a simple inventory tracking program
#     using dictionaries.
#

def get_command():
    command = input("Enter command: ")
    return command


def add_to_inventory(dict):
    invname = input("Enter name of item to add to inventory: ")
    qty = int(input("Enter quantity of item to add: "))

    # finish this: add qty to dict[invname] value
    #   (if not there, set dict[invname] to qty)

    if invname in dict.keys():
        dict[invname] = dict[invname] + qty
    else:
        dict[invname] = qty

def view_inventory(dict):
    print(f"{'Item':9} -- {'Qty':9}")
    for (k, v) in dict.items():
        print(f"{k:<9} -- {v:<9}")

def remove_inventory(dict):
    invname = input("Enter an item in the inventory you would like to remove from: ")
    qty = int(input("Enter the quantity you would like to remove: "))

    if invname not in dict:
        print("\nthis is not a valid item in the inventory\n")
    elif invname in dict and dict[invname] >= qty:
        dict[invname] = dict[invname] - qty
        if invname in dict and dict[invname] == 0:
            dict[invname] = dict[invname] - qty
            del dict[invname]
    elif invname in dict and dict[invname] < qty:
        print("\nInventory has less than the quantity to be removed\n")
    else:
        return False

    # Finish this...

    # Prompt user for name of item to delete,
    #   followed by amount to remove from inventory.

    # Be sure to check both item name and amount to remove
    #   are valid (item already in inventory and amount of this item
    #   doesn't exceed existing inventory amounts), printing msg
    #   if either condition fails.

    # If all of an item's quantity is removed, also remove the item from the dictionary.


def main():
    print("Welcome to StuffMaster, v.0.47")

    inventory = {}  # empty dictionary

    while True:  # get command, process command; quit when selected below

        print("Commands are: ")
        print("'A' => Add to inventory")
        print("'V' => View existing inventory")
        print("'R' => Remove from inventory")
        print("'Q' => Quit after showing final inventory")

        # Get the command

        cmd = get_command().upper()[0]

        # Call the appropriate function based on command

        if cmd == 'A':
            add_to_inventory(inventory)
        elif cmd == 'V':
            view_inventory(inventory)
        elif cmd == 'R':
            remove_inventory(inventory)
        elif cmd == 'Q':
            break
        else:
            print(f"Unknown command: '{cmd}' => try again.")

        # If unknown command, complain and prompt for reentry

    # here, we're quitting

    print("Quitting. Final version of inventory is:")

    # print out final version of inventory

    view_inventory(inventory)

    print("Exiting...")


main()
