class Student: # user defined classes must start with capital letter
  count = 0 # class attribute
  # accessed using the class name directly

  def __init__(self, name, gender, roll=None, marks=None):
    # constructor
    # creating attribute in an object

    # None - variable that exists in the function scope but does not store any address
    self.name = name
    self.gender = gender
    self.roll = roll
    self.marks = marks

    Student.count += 1

  # class function
  def get_count():
    return Student.count

  # object function
  def get_details(self):
    return 'Name : ' + self.name + '\nGender : ' + self.gender + '\nRoll : ' + str(self.roll) \
    + '\nMarks : ' + str(self.marks)

  def get_grade(self):
    marks = self.marks
    if marks > 100 or marks < 0:
      grade = 'I'
    elif marks >= 70:
      grade = 'A'
    elif marks >= 60:
      grade = 'B'
    elif marks >= 40:
      grade = 'C'
    else:
      grade = 'F'
  
    return grade

# When the program loads, for all the classes (user defined and built in) a single object is created in the memory
# class object. Represents the class area of the memory