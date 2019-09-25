from com.abc.college.student import Student

# print(Student.count)
print(Student.get_count())
# Internally
# Student.get_count()

# s1 = Student()
# Internally
# 1. Reserves area in memory for this Student object - 2001
# 2. Student.__init__(2001)

s1 = Student('mehul', 'm', 10, 90.45)
# Internally
# 1. Reserves area in memory for this Student object - 2006
# 2. Student.__init__(2006, 'mehul', 'm', 10, 90.45)

# created attributes in an object
'''s1.name = 'mehul'
s1.gender = 'm'
s1.roll = 10
s1.marks = 90.45'''



'''s2 = Student()
#Internally
# 1. Reserves area in memory for this Student object - 2004
# 2. Student.__init__(2004)'''

'''s2.student_name = 'jane'
s2.gen = 'f'
s2.r = 11
s2.marks = 45'''

s2 = Student('jane', 'f', 11, 45)
s2.dummy = 90 # works

print(Student.count)

# print(s1)
# print(s2)

# access the attributes from an object
'''print(s1.name)
print(s1.roll)

print(s2.name)
print(s2.roll)'''

print(s1.get_details())
# Python internally
# Student.get_details(s1)


print(s2.get_details())
# Python internally
# Student.get_details(s2)

print(s1.get_grade())
# Student.get_grade(s1)

print(s2.get_grade())
# Student.get_grade(s2)

s3 = Student('jill', 'f')
# Student.__init__(3004, 'jill', 'f')

print(Student.count)
