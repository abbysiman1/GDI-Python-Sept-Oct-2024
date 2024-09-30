# Step 1: Start with a dictionary of student grades
student_grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

# Step 2: Access and print Bob's grade
print(student_grades["Bob"])

# Step 3: Update Charlie's grade to 82
student_grades["Charlie"]=92
print("Updated Charlie's grade:", student_grades)

# Step 4: Add a new student (David) with a grade of 90
student_grades["David"]=90
print("Added David's grade:", student_grades)

# Step 5: Add two more students to the dictionary and print the updated dictionary
student_grades["Zoe"]=100
student_grades["Naomi"]=95
print("Updated student grades:", student_grades)