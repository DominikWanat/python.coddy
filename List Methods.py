lst1= [1,1,1]
lst2=[4,3,2]


# Write code here
def merge(lst1, lst2):
    # Write code here
    for i in range (len(lst1)):
        a= lst1[i]
        lst2.append(a)
    lst2.sort()
    return (lst2)

print(merge(lst1,lst2))


#####################################################

def merge(lst1, lst2):
    res = []
    for i in range(len(lst2)):
        res.append(lst2[i])
    for i in range(len(lst1)):
        res.append(lst1[i])
    res.sort()
    return res