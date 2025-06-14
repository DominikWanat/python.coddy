# Now let's create the actual program!

# Create an infinite while loop (refer the hint if not sure how to do so)
# In each iteration of the loop, get input from the user, this will be the choice (1 - 5 from the menu)
# Handle the first case, if the choice is equal to 5, exit the program (loop) and output:


while True:
    choice = int(input())
    if choice ==5:
        print("Welcome to the Daily Expense Tracker!")
        print ("")
        print("Menu:")
        print("1. Add a new expense")
        print("2. View all expenses")
        print("3. Calculate total and average expense")
        print("4. Clear all expenses")
        print("5. Exit")
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break

################################################################
print("Welcome to the Daily Expense Tracker!")

# Display menu once
print("\nMenu:")
print("1. Add a new expense")
print("2. View all expenses")
print("3. Calculate total and average expense")
print("4. Clear all expenses")
print("5. Exit")

while True:
    # Get user choice
    choice = input()

    if choice == "5":
        # Exit the program
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break