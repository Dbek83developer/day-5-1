# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sum_height = 0
number_stud = 0
for height in student_heights:
  sum_height += height
  number_stud += 1
average = round(sum_height / number_stud)
# print(number_stud)
print(average)


