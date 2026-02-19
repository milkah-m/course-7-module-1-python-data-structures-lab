# filter.py
# This module contains functions for filtering and grouping student data.

"""1. Return a formatted string for a single student record.
    Converts the student tuple into a dictionary first so that each
    field is explicitly named, making the f-string easier to read and maintain.
    """
"""2. Loop through all students and print each one's formatted details."""

def format_student_data(student):
    student_dict = {
        "id": student[0],
        "name": student[1],
        "major": student[2]
    }
    return f"ID: {student_dict['id']} | Name: {student_dict['name']} | Major: {student_dict['major']}"
    

def display_students(student_list):
    for student in student_list:
        print(format_student_data(student))

    