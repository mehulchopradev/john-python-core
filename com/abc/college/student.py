from .college_user import CollegeUser

# sub class / child class / concrete class
# Student -> CollegeUser -> object (multi level inheritance)
class Student(CollegeUser):
  def __init__(self, name, gender, roll, marks, contact_nos):
    # create name, gender, roll, marks, contact_nos attributes in the current object (self)
    super().__init__(name, gender, contact_nos)
    # Internally
    # CollegeUser.__init__(self, name, gender, contact_nos)

    self.roll = roll
    self.marks = marks

  def get_details(self): # method overriding
    # signature of the overriden method and inherited method must be the same

    part1 = super().get_details() # calling the super class version of the overriden method from the override method
    # Internally
    # CollegeUser.get_details(self)

    return '{0}Roll: {1}\n'.format(part1, self.roll)

  # can have its own set of functions