#Write a program that receives a list of words as input (given), 
# and prints a list of the indices of the words that are either 
# longer than 3 characters or start with the letter 'a' (case-sensitive).
#
#To check if a string starts with some substring use: str.startswith("substring")
lst = ["cat", "apple", "dog", "elephant", "ant", "bird"]

new_lst =[]
for index, ls in enumerate (lst):
    if len(lst[index])> 3 or ls[0] == "a":
        new_lst.append(index)
print (new_lst)

## solcuión coddy
lst = input().split()
new_lst = []
for index, word in enumerate(lst):
    if len(word) > 3 or word.startswith('a'):
        new_lst.append(index)
print(new_lst)