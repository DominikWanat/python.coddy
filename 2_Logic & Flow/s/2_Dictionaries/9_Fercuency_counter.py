# Create a function named frequency_counter that takes a
# list data_list as an argument. The function should count
# the frequency of each item in the list and return
# a dictionary where the keys are the unique items
# from the list and the values are the counts of how
# many times each item appears.

# For example, if the input list is [1, 2, 2, 3, 3, 3, 4, 4, 4, 4],
# the function should return a dictionary like this:
# {1: 1, 2: 2, 3: 3, 4: 4}

data_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

def frequency_counter(data_list):
    # Write code here
    data_list_uniq =list(set(data_list))
    for i in data_list_uniq(i):
        data_list_uniq_cout = data_list.count(i)
        data_list_dic = {i:data_list_uniq_cout}

print(frequency_counter(data_list))