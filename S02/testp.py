import math
def bestAverageGrade(scores):
    grades = {}
    for student, grade in scores:
        grade = float(grade)
        current = grades.get(student)
        if current is None:
            grades[student] = grade, 1
        else:
            num, denom = current
            grades[student] = num + grade, denom + 1
    return math.floor(max(num/denom for num, denom in grades.values()))