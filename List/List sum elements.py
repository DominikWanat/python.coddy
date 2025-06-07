#Create a function named sum_elements that receives a list as an argument and prints the sum of all the elements in the list
lst = [1, 2, 3, 4, 5]

def sum_elements(lst):
    # Write code here
    a = 0    
    for i in range (len(lst)):
        a += lst[i]
    print(a)

sum_elements(lst)