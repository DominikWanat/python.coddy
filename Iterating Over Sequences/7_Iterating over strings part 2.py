# Create a program that takes two inputs: a string of numbers separated by spaces, and a prefix string.
# The program should split the number string into individual numbers, add the prefix to each number,
# then join these modified numbers back into a single string separated by spaces. Finally, print the resulting string.

numbers = "123 456 789"
prefix = "+1"
# Write your code below

lst = numbers.split()
n_lst = []
for i in range (len(lst)):
    n_lst.append(prefix + lst[i])

n_lst = " ".join(n_lst)
print(n_lst)



