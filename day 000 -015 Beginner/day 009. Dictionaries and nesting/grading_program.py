#! /usr/bin/env python3

# grading_program.py

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
student_grades = {}



for student in student_scores:  # Student is our key
    score = student_scores[student]
    if 91 <= score <= 100:
        student_grades[student] = "Outstanding"
    elif 81 <= score <= 90:
        student_grades[student] = "Exceeds Expectations"
    elif 71 <= score <= 80:
        student_grades[student] = "Acceptable"
    elif score < 70:
        student_grades[student] = "Fail"


print (student_grades)