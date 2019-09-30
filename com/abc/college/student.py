class Student: # user defined classes must start with capital letter
  count = 0 # class attribute
  # accessed using the class name directly

  def __init__(self, name, gender, roll=None, marks=None, contact_nos=None):
    # constructor
    # creating attribute in an object

    # None - variable that exists in the function scope but does not store any address
    self.name = name
    self.gender = gender
    self.roll = roll
    self.marks = marks

    if contact_nos is not None: # tests whether a variable stores a particular address or no (is)
      if isinstance(contact_nos, list):
        # tests whether the object that the variable stores, is of a particular class type or no
        self.contact_nos = contact_nos
      else:
        # TODO: This will change
        print('Contact nos must be a list')
        self.contact_nos = None
    else:
      self.contact_nos = contact_nos

    Student.count += 1

  # class function
  def get_count():
    return Student.count

  # object function
  def get_details(self):
    part1 = 'Name : ' + self.name + '\nGender : ' + self.gender + '\nRoll : ' + str(self.roll) \
    + '\nMarks : ' + str(self.marks) + '\n'

    if self.contact_nos:
      part2 = 'Contact Nos : '
      for contact_no in self.contact_nos:
        part2 += contact_no + '\n'
    else:
      part2 = 'Contact Nos : NA'
    
    return part1 + part2


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

  def get_name_roll(self):
    return (self.name, self.roll)

# When the program loads, for all the classes (user defined and built in) a single object is created in the memory
# class object. Represents the class area of the memory