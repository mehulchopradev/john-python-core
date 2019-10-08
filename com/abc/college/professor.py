from .college_user import CollegeUser
from ..emailer.email import Email

# child class
class Professor(CollegeUser, Email):
  def __init__(self, name, gender, contact_nos, subjects, email=None):
    # create name, gender, contact_nos, subjects attributes in the current object (self)
    super().__init__(name, gender, contact_nos)
    # Internally
    # CollegeUser.__init__(self, name, gender, contact_nos)

    self.subjects = subjects
    self.email = email

  # can have its own set of functions