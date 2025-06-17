def print_pattern_2(rows, cols):
    # Outer loop for rows
    for i in range(rows):
        # Inner loop for columns
        row_string = ""
        for j in range(cols):
            row_string += '*'
        # Move to the next line after printing a row
        print(row_string)

# Get input for rows and columns
rows = int(input())
cols = int(input())

# Call the function
print_pattern_2(rows, cols)