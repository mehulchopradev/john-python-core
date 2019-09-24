'''
 >= 70 - A
 >= 60 - B
 >= 40 - C
 < 40 - F
 > 100 or < 0 - I
'''

marks = float(input('Enter marks : ')) # module (entire file) - Access the variable (get the value)

def get_grade():
  # if-elif-elif-elif-else
  # marks = 90 # get_grade()

  '''global marks
  marks = 90 # module (entire file)'''
  if marks > 100 or marks < 0: # condition can be python truthy and falsy
    grade = 'I' # enclosing function
  elif marks >= 70: # condition can be python truthy and falsy
    grade = 'A' # enclosing function
  elif marks >= 60:
    grade = 'B' # enclosing function
  elif marks >= 40:
    grade = 'C' # enclosing function
  else:
    grade = 'F' # enclosing function
  
  return grade


print(get_grade())

# no switch statement (cases)