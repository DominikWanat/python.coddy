## Write a function named prod which gets a list of numbers as argument and returns the product of all the numbers in the list.
## 
## Reminder, product is the multiplication of all the numbers, for [1, 2, 3], return 6 = 1 * 2 * 3.

lst = [12, 23, 56, 2, -18, 98]

def prod(lst):
    a = 1
    for i in range (len(lst)):
        a *= lst[i]
        
    return a

print(prod(lst))