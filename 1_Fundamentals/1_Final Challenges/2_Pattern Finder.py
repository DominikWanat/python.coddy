# Create a function named find_occurrences that:

# Takes two string arguments: text and pattern
# Counts how many times pattern appears in text, including overlapping occurrences
# Returns a tuple containing:
# A boolean indicating if the pattern was found (True/False)
# The number of occurrences of the pattern
# A list of starting positions where the pattern was found
# For example, if text is "abababab" and pattern is "aba", your function should return (True, 3, [0, 2, 4]), since "aba" appears at positions 0, 2, and 4.

# If the pattern is not found, return (False, 0, []).
def find_occurrences(text, pattern):
    positions = []
    index = 0

    while index <= len(text) - len(pattern):
        if text[index:index + len(pattern)] == pattern:
            positions.append(index)
        index += 1  # Move forward by one to allow overlapping matches

    found = len(positions) > 0
    count = len(positions)
    return (found, count, positions)

# Read input
text = input()
pattern = input()

# Call your function and print the result
result = find_occurrences(text, pattern)
print(result)

#####################################################################
def find_occurrences(text, pattern):
    count = 0
    positions = []
    
    # Get the length of both strings
    text_length = len(text)
    pattern_length = len(pattern)
    
    # Check each possible starting position in text
    for i in range(text_length - pattern_length + 1):
        # Check if pattern matches at current position
        if text[i:i+pattern_length] == pattern:
            count += 1
            positions.append(i)
    
    # Return tuple with results
    if count > 0:
        return (True, count, positions)
    else:
        return (False, 0, [])

# Read input
text = input()
pattern = input()

# Call your function and print the result
result = find_occurrences(text, pattern)
print(result)