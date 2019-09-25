from student_ops import get_grade, get_details

name = input('Enter name : ')
gender = input('Enter gender : ')
roll = int(input('Enter roll : '))
marks = float(input('Enter marks : '))

print(get_details(name, gender, roll, marks))
print(get_grade(marks))

