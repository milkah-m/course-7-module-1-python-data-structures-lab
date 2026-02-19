"""ReturnING a generator expression that yields students matching the given major.
    
    A generator is used instead of a list for memory efficiency — it produces
    one student at a time on demand rather than loading all matches into memory
    at once. This is particularly beneficial when working with large datasets.
    The comparison is case-insensitive to handle varied user input.
    """

def student_generator(student_list, major):
     # Returns a generator expression for lazy evaluation — 
    # avoids loading all students into memory at once
    major_generator = (student for student in student_list if student[2].lower() == major.lower())
    return major_generator

