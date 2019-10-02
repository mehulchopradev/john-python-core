from .college_user import CollegeUser

# child class
class Professor(CollegeUser):
  def __init__(self, name, gender, contact_nos, subjects):
    # create name, gender, contact_nos, subjects attributes in the current object (self)
    super().__init__(name, gender, contact_nos)
    # Internally
    # CollegeUser.__init__(self, name, gender, contact_nos)

    self.subjects = subjects

  # can have its own set of functions