#Create a program that receives a string as input, and it prints how many times the character p (or P) is in the string.
#
#Some chars might be uppercase, use char.lower() to convert it to lowercase.

text = "Happy people play ping pong"
text = text.lower()
print(text)
a=0
for char in text:
    if char == "p":
        a += 1
print (a)


###########################
text = input()
count = 0
for char in text:
    if char.lower() == 'p':
        count += 1
print(count)