#! /usr/bin/env python3

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
#student_heights = [156, 178, 165, 171, 187]  # For testing
# Work out how many students there is without using len()
# Work out the total amount of height without using sum()
num_of_students = 0
tot_student_height = 0
for student in student_heights:
    num_of_students += 1
    tot_student_height += student

average_height = (round(tot_student_height / num_of_students))
print(average_height)

# Test area
#print (f"average_height: {average_height}" )
#print(f"number of students: {num_of_students}")
#print(f"total student height: {tot_student_height}")


