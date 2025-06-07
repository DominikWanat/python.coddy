def change_element(lst, index, new_element):
    # Write code here
    lst[index] = new_element
    return lst

lst =["a", "b", "c"]
#lst= input()
index = 1
##index = int(input())
new_element = "d"

print(change_element(lst, index, new_element))