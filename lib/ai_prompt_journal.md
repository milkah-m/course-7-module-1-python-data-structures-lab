1. hey claude. what is the python equivalent of .filter in javascript. please include a usage example
   claude's answer: 
numbers = [1, 2, 3, 4, 5, 6]
evens = [x for x in numbers if x % 2 == 0]
print(evens)  # [2, 4, 6]

2. hey claude is this the right way to access third place in a list. i just want to clarify before i print haha: student(2)
    claude's answer: use square brackets even if it is a list

3. hey claude how do i add data to a set. please provide with me a practical example and the logic behind the method.
    claude's answer: use.add() and not .append() because sets have no particular order aaaand also sets handle duplication so i don't even need to use the conditional statements that i was trying to implement. yaaaayyy

4. hey claude how do i differentiate between a set and a dictionary when i want to initiate an empty set? please give me a simple example and the logic behind the method.
    claude's answer: girrrlll you have to use set() because {} had already been claimed by dictionaries by the time set was added.

5. hey claude in my function below. why is my print giving me only mathematics?? my gut feeling is that there's something about set functionality that i have not understood clearly. please explain what that is for me without feeding me the code straightup. After this, I also want you to test my comprehension and understanding of set functionality with an activity.
 students = [
    (101, "Miles", "Mathematics"),
    (102, "Laura", "Mathematics"),
    (103, "Benji", "Physics"),
    (104, "Natalia", "Physics"),
    (105, "Nadia", "Mathematics"),
]
def unique_majors(student_list):
    majors_set = set()
    for student in student_list:
        majors_set.add(student[2])
        return majors_set
       


print(unique_majors(students))
    claude's answer: actual loolllest moment. it was an indentation issue. i had placed my return inside my for loop so it only returned once and wrapped up. but still shouldn't it have returned every single time? and still givem me physics?? ooohh it is because how this return works is that it will exit the function immediately on the first iteration and not wait for the loop to finish.

6. hey claude!! umm so here i am supposed to create a student list generator by major but i think that there is a core functionality of generator expressions that i am missing because tell me why i am getting this when i print: <generator object student_generator.<locals>.<genexpr> at 0x773a49e13220>. here's my function: def student_generator(student_list, major):
    major_generator = (student for student in student_list if student_list[2].lower() == major.lower())
    return major_generator

students = [
    (101, "Alice Johnson", "Computer Science"),
    (102, "Bob Smith", "Mathematics"),
    (103, "Charlie Davis", "Physics"),
    (104, "David Wilson", "Computer Science"),
    (105, "Eve Lewis", "Mathematics"),
]
print(student_generator(students, "computer science"))
so here's what i want you to do. 
 1. explain what specific lines in my code are faulty
 2. teach me what it is that i am not understanding about how generator expresssions work
 3. finally, give me a teeny weeny practice activity to test out my newfound knowledge
    claude's answer: 
    - i input student_list[2] and not student[2]
    - i printed a generator object directly without iterating over it first. this is the core concept about generator expressions that i was missing
    teeny weeny activity: numbers = (x for x in [10, 20, 30, 40, 50])
        for number in numbers:
            print number

            or print numbers

            or print x
            //though i feel like it might not be this straightforward because this is a list within a generator expression...
            but i don't feel like thinking to be honest

7. okay claude what in the actual am i missing here?? i want to return not just to print...

8. hey claude please explain this error to me. i am trying to install dependencies for my lab so that i can run tests. what gives:  pipenv install
Warning: Python 3.10 was not found on your system...
Neither 'pyenv' nor 'asdf' could be found to install Python.
You can specify specific versions of Python with:
$ pipenv --python path/to/python

9. hey claude, here's my code. i want you to compare it to the rubric and let me know what is wanting. i know readme and comments are definitely wanting. please tell me what else and give me your honest assessment of what the score would be if i submitted it as is. finally give me improvements to have it be as close to perfect as possible. 

# In `filter.py`, edit the `filter_students_by_major` function to return a filtered list
# of students given a major using a list comprehension.


# This module contains functions for filtering student data.
"""
    Return a filtered list of students by major using a list comprehension.
    The function should:
    - Check if a student's major matches the given major (case insensitive).
    - Return a new list containing only students that match.
    """
students = [
    (101, "Alice Johnson", "Computer Science"),
    (102, "Bob Smith", "Mathematics"),
    (103, "Charlie Davis", "Physics"),
    (104, "David Wilson", "Computer Science"),
    (105, "Eve Lewis", "Mathematics"),
]

def filter_students_by_major(student_list, major):
    matching_majors = [student for student in student_list if student[2].lower() == major.lower()]
    return matching_majors

print(filter_students_by_major(students, "computer science"))

def format_student_data(student):
    return f"ID: {student[0]} | Name: {student[1]} | Major: {student[2]}"


