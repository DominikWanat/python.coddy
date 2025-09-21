# Step 1: Create the Grades Dictionary
grades = {"Alice": 85, "Bob": 90, "Charlie": 78
    # Add initial student grades here
}

# Step 2: Access All Keys and Values
# Print all students and grades
keys = grades.keys()
values = grades.values()
#print(f"Students: {keys}")
#print(f"Grades: {values}")

# Step 3: Add a New Student
# Add Diana with a grade of 92
grades["Diana"] =  92

# Step 4: Retrieve a Student's Grade
# Get Bob's grade using get() method
bobs_grade = grades.get("Bob")
#print(f"Bob´s grade: {bobs_grade}")

# Step 5: Remove a Student
# Remove Charlie using pop() method
# Print the updated dictionary
grades.pop("Charlie")

print(f"Update grades: {grades}")

################################################################

# Step 1: Create the Grades Dictionary
grades = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}

# Step 2: Access All Keys and Values
print("Students:", grades.keys())
print("Grades:", grades.values())

# Step 3: Add a New Student
grades["Diana"] = 92

# Step 4: Retrieve a Student's Grade
bobs_grade = grades.get("Bob")
print("Bob's grade:", bobs_grade)

# Step 5: Remove a Student
grades.pop("Charlie")
print("Updated grades:", grades)