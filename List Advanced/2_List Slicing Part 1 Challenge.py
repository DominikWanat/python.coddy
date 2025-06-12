# Create a program that takes a list and prints:

# For lists with 5 or more items: the first two and last two items
# For lists with less than 5 items: the first and last item only

input_list = [1, 2, 3, 4]
output_list= []
if len(input_list)  >= 5:
    output_list = input_list[:2] + input_list [-2:]
if len(input_list)  < 5:
    output_list.append(input_list[0])
    output_list.append(input_list[-1])
print(output_list)

###########################################################
input_list = input().split(', ')
# Write your code below
if len(input_list) >= 5:
    print(input_list[:2] + input_list[-2:])
else:
    print([input_list[0], input_list[-1]])