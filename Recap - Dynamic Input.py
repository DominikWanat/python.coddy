#Write a program that gets a dynamic number of input values.
#The first input is a number that represents the number of the input values following it. The next input values are whole numbers.
#In the end, print the sum of all the input numbers (not including the first input).


##############################################################################
## ChatGPT:
# Get the first input: number of values to be summed
count = int(input("Enter the number of values: "))

# Initialize a variable to store the sum
total = 0

# Loop to get each number and add to the total
for i in range(count):
    num = int(input(f"Enter number {i+1}: "))
    total += num

# Print the result
print("Sum of the numbers:", total)

##############################################################################

## Sencilla para coddy

inp = int(input())
total = 0

for i in range (inp):
    num = int(input())
    total += num

print(total)
