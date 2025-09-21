## Create a function named check_inventory that takes two parameters: inventory (a dictionary where keys are item names and values are quantities) ##and item (a string representing the item to check). The function should:

## Check if the item is in the inventory.
## If the item is in stock, return the string: "<item> is in stock. Quantity: <quantity>".
## If the item is not in stock, return the string: "<item> is not in stock."


inventory = {"book":7,"magazine":12,"notepad":0}
item = "notepad"

def check_inventory(inventory, item):
    # Write code here
    if item in inventory:
        if inventory[item] > 0:
            print(f"{item} is in stock. Quantity: {inventory[item]}")
        if inventory[item] == 0:
            print(f"{item} is in stock. Quantity: {inventory[item]}")
    else:
        print(f"{item} is not in stock.")

print(check_inventory(inventory, item))