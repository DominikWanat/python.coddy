def create_student_dict(name, age, major):
    # Write code here
    student_dict = {
        "name": name,
        "age": age,
        "major": major
    }
    return(student_dict)

##############################################

def create_student_dict(name, age, major):
    # Create an empty dictionary
    student_dict = {}

    # Add key-value pairs to the dictionary
    student_dict["name"] = name
    student_dict["age"] = age
    student_dict["major"] = major

    # Return the dictionary
    return student_dict