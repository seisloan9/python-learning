def gpa(score):
    gradepoint = 0
    if score >= 90:
            gradepoint = 4
    elif 80 >= score >= 89:
            gradepoint = 3
    elif 70 >= score >= 79:
            gradepoint = 2
    elif 60 >= score >= 69:
            gradepoint = 1
    else:
            gradepoint = 0
    return gradepoint
