list1 = [1, 2, 3]
index = 1
list2 = [5, 6, 7]

def change_element(list1, index, list2):
    # Write your code below
    #ch = 0
    ch = list2[0] 
    list1[index] = ch
    print(list1)

change_element(list1, index, list2)

###################################

def change_element_coddy(list1, index, list2):
    list1[index] = list2[0]
    return list1