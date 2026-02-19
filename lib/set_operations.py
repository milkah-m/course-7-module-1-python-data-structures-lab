"""ReturnS a set of unique majors from the student list.
    
    Uses a set comprehension to extract the major field from each student tuple.
    Duplicates are automatically discarded since sets only store unique values.
    """
def unique_majors(student_list):
    majors_set = set()
    for student in student_list:
        majors_set.add(student[2])
    return majors_set
       


