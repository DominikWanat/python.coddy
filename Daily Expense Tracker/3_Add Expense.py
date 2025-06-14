# Handle the option where the user adds an expense (1).

# Initialize in the start of the program an empty expenses list
# When the user selects 1 as a choice, get another input from the user, a float, and add its value to the expenses list.
# After adding, output:
# Expense added successfully!


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
    if choice == "1":
        print("Expense added successfully!")
    elif choice == "5":
        # Exit the program
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break