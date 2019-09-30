from com.abc.college.student import Student

'''l = [
  Student('mehul', 'm', 10),
  Student('john', 'm', 5),
  Student('jane', 'f', 23),
  Student('jill', 'f', 20)
]'''

student_dict = {
  10: Student('mehul', 'm', 10),
  5: Student('john', 'm', 5),
  23: Student('jane', 'f', 23)
}


roll = int(input('Enter roll to search : '))

'''for student in l:
  if student.roll == roll:
    print(student.get_details())
    break
else:
  # it will execute when the corresponding for block has been completely exhausted (no break encountered)
  print('Not found')'''

if roll in student_dict:
  print(student_dict[roll].get_details())
else:
  print('Not found')
