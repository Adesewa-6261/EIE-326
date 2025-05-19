# GPA calculator 

courses = ['GEC 320', 'EIE 323', 'EIE 327', 'GEC 324', 'GEC 325', 'TMC 321']
grade_points = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'F': 0}

total_score = 0
total_units = 0
course_unit = 3  # All courses are 3 units

for course in courses:
    grade = input("Enter your grade for " + course + ": ")
    grade = grade.upper()

    if grade == 'A':
        point = 5
    elif grade == 'B':
        point = 4
    elif grade == 'C':
        point = 3
    elif grade == 'D':
        point = 2
    elif grade == 'F':
        point = 0
    else:
        print("Invalid grade entered. Use A, B, C, D, or F.")
        break

    total_score = total_score + (point * course_unit)
    total_units = total_units + course_unit

gpa = total_score / total_units
print("Your GPA is:", gpa)
