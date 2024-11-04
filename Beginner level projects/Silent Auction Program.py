student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermon': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

# Iterate over the student_scores dictionary and assign grades
for student, score in student_scores.items():
    if score >= 91:
        student_grades[student] = "Outstanding"
    elif score >= 81:
        student_grades[student] = "Exceeds Expectations"
    elif score >= 71:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)  