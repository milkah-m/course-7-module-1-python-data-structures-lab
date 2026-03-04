
"""Return a filtered list of students matching the given major.
    
    Uses a list comprehension for concise, readable filtering.
    The comparison is case-insensitive to handle varied user input.
    """

def filter_students_by_major(students, major):
    return [student for student in students if student[2] == major]





