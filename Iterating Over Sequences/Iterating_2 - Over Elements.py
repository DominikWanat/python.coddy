# Create a program that receives a list of numbers as input (given), and prints the sum of all even numbers in the list.

numbers = [1,2,3,4,5,6]
sum = 0
for num in numbers:
    if int(num) %2 == 0:
       sum += int(num)
print(sum) 


#####################################
numbers = input().split(',')
even_sum = 0
for num in numbers:
    if int(num) % 2 == 0:
        even_sum += int(num)
print(even_sum)