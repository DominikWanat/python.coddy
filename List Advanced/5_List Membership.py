# Create a function called not_mutual_friends that takes two lists of names representing two people's friend lists. The function should return a list of names that are friends with only one person (not mutual friends).

# Let's say we have:

# Person A's friends: ["John", "Emma", "Mike", "Sarah"]
# Person B's friends: ["Emma", "Tom", "Sarah", "Peter"]
# When we call not_mutual_friends with these two lists, it should return: ["John", "Mike", "Tom", "Peter"]

# Explanation:

# "John" and "Mike" are only friends with Person A
# "Tom" and "Peter" are only friends with Person B
# "Emma" and "Sarah" are mutual friends (friends with both people), so they are not included in the result

list1 =["John", "Emma", "Mike", "Sarah"]
list2 = ["Emma", "Tom", "Sarah", "Peter"]

def not_mutual_friends(list1, list2):
    # Write your code below
    result = []
    for friend in list1:
        if friend not in list2:
            result.append(friend)
    for fiend in list2:
        if fiend not in list1:
            result.append(fiend)
    return result