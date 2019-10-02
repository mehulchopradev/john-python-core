from com.abc.college.student import Student
from com.abc.college.professor import Professor

s = Student('mehul', 'm', 10, 90, ['34534534'])
p = Professor('jane', 'f', [], ['Physics'])
i = 10

print(s)
# Internally
# print(s.__str__())
# print(Student.__str__(s))

print(p)
# Internally
# print(p.__str__())
# print(Professor.__str__(p))

print(i)
# Internally
# print(i.__str__())
# print(int.__str__(i))

'''print(s.name)
print(s.gender)

print(p.name)
print(p.gender)
print(p.subjects)'''

# print(s.get_details())
# print(p.get_details())