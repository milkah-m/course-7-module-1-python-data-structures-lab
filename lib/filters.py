
"""Return a filtered list of students matching the given major.
    
    Uses a list comprehension for concise, readable filtering.
    The comparison is case-insensitive to handle varied user input.
    """

def group_students_by_major(student_list):
    return {
        major: [s for s in student_list if s[2] == major]
        for major in {s[2] for s in student_list}
    }






