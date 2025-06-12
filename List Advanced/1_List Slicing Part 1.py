# Create a program that receives a list as input (given) and prints the following sliced list:

# For odd-length lists: take the middle item and one item on each side (3 items total)
# For even-length lists: take the two middle items
# When dividing numbers:

# / gives you a decimal number (5/2 = 2.5)
# // removes the decimal part (5//2 = 2)
# For this challenge, use // because list slicing only works with whole numbers.

lst = [1]
print(len(lst))

new_lst =[]

for i in range (len (lst)):
    if len(lst) == 1:
        new_lst.append(str(lst[0]))
    if len(lst) %2 == 0 :
        if i == len(lst)//2:
            new_lst.append(str(lst[i-1]))
            new_lst.append(str(lst[i]))
    if len(lst) %2 != 0 and len(lst) !=1:
        new_lst.append(str(lst[len(lst)//2-1]))
        new_lst.append(str(lst[len(lst)//2]))
        new_lst.append(str(lst[len(lst)//2+1]))
        break
        
print(new_lst)

####################################################

lst = input().split(",")
if len(lst) % 2 == 0:
    lst_mid = lst[len(lst)//2-1:len(lst)//2+1]
else:
    lst_mid = lst[len(lst)//2-1:len(lst)//2+2]
print(lst_mid)