# Write a program that takes two inputs: a text string and a delimiter character.
# The program should split the text by whitespace into words, then join these words using the specified delimited character and print the resulting string.

text = "Hello world python"
delimiter = "-"
# Write your code below
lst = text.split()
text =delimiter.join(lst)

print(text)