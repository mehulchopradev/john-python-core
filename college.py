from com.abc.college.student import Student
from com.abc.college.professor import Professor

s = Student('mehul', 'm', 10, 90, ['34534534'])
p = Professor('jane', 'f', [], ['Physics'])
i = 10

# print(s)
# Internally
# print(s.__str__())
# print(Student.__str__(s))

# print(p)
# Internally
# print(p.__str__())
# print(Professor.__str__(p))

# print(i)
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

s2 = Student('jane', 'f', 23, 89, [])
s3 = Student('john', 'm', 20, 96, [])

d1 = Student('johnnn', 'M', 20, None, [])

avg = (s + s2) / 2 # Student.__add__(s, s2)
print(avg)

print(s2 > s3) # Student.__gt__(s2, s3)

print(s3 == d1) # Student.__eq__(s3, d1)

s2 << '7987986787' << '978768768' # Student.__lshift__(s2, '7987986787')

print(s2.get_details())