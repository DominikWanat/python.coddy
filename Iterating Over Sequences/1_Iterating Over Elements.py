# Create a program that receives a list as input (given), and prints a new list containing only the words longer than 5 characters

#lst = input().split(",")

lst =  ["penguin","elephant","koala","tiger","dolphin","giraffe","kangaroo","zebra","lion","panda"]
lst2=[]
# Write your code below
for res in lst:
    if len(res)>5:
        lst2.append(res)
print(lst2)

####################

lst = input().split(",")
new_lst = []
for item in lst:
    if len(item) > 5:
        new_lst.append(item)
print(new_lst)