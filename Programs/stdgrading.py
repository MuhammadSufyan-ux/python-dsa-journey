





# updated version 

# Student Result System

name = input("Enter student's name: ")

subjects = []

# Taking marks of 7 subjects
for i in range(1, 8):
    marks = int(input(f"Enter marks for subject {i}: "))
    subjects.append(marks)

# Total marks
total_marks = int(input("Enter total marks: "))

# Calculations
obtained_marks = sum(subjects)
percentage = (obtained_marks / total_marks) * 100
average = obtained_marks / len(subjects)

# Highest and lowest marks
highest = max(subjects)
lowest = min(subjects)

# Grade
if percentage >= 85:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 65:
    grade = "B+"
elif percentage >= 55:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "Fail"

# Result
print("\n========== STUDENT RESULT ==========")
print("Student Name:", name)
print("Total Marks:", total_marks)
print("Obtained Marks:", obtained_marks)
print("Percentage:", percentage)
print("Average Marks:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Grade:", grade)
print("====================================")