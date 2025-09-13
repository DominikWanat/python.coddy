# Create a function named print_employee_details that takes a dictionary
# employee_data as an argument. The function should loop through the dictionary
# and print each key-value pair in the format 'key: value'. If the dictionary
# is empty, the function should print 'No data available'.

employee_data = {}

def print_employee_details(employee_data):
    # Write code here
    if not employee_data:
        print('No data available')
    else:    
        for key, value in employee_data.items():
            print(f'{key}: {value}')

print(print_employee_details(employee_data))