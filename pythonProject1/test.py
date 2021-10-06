# find out the average
grades = [55, 64, 75, 80, 95]


def find_average_grades(grades):
    sum_of_grades = sum(grades)
    total_subjects = len(grades)
    average_grades = sum_of_grades / total_subjects
    return average_grades


# calculate grades and returns it
def compute_grade(average_grades):
    if average_grades >= 90:
        grade = "A"
    elif average_grades >= 80:
        grade = "B"
    elif average_grades >= 70:
        grade = "C"
    else:
        grade = "D"
    return grade


average_grades = find_average_grades(grades)
print("Your averages grades are:", average_grades)

grade = compute_grade(average_grades)
print(f"Your grade is: {grade}")
