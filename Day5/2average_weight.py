# Input a Python list of student heights

student_heights = [156, 178, 165, 171, 187]
total_height = 0
for height in student_heights:
    total_height += height

print(f"total height = {total_height}")
print(f"number of students = {len(student_heights)}")
print(f"average height = {round(total_height / len(student_heights))}")

