# Write a function named reverse which gets a list of numbers as argument and returns the reversed list.
#
# For example, for [1, 2, 3], the expected output is [3, 2, 1].

lst = [3, 5, 7, 1, -4, 98]

def reverse(lst):
    # Write code here
    rev = []
    for i in range (len(lst)-1,-1,-1):
        rev.append(lst[i])
    return rev

print(reverse(lst))


#####################################################

def reverse(lst):
    res = []
    for i in range(len(lst)):
        res.append(lst[len(lst) - i - 1])
    return res