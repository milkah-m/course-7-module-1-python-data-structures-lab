# student_data.py
# This module initialises the student records used across the system.

# Each student is stored as a tuple (ID, Name, Major).
# Tuples are used here because student records are fixed and should not be modified.
# The full collection is stored in a list since the roster may grow over time.

students = [
    (101, "Alice Johnson", "Computer Science"),
    (102, "Bob Smith", "Mathematics"),
    (103, "Charlie Davis", "Physics"),
    (104, "David Wilson", "Computer Science"),
    (105, "Eve Lewis", "Mathematics"),
]