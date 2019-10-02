# super class / parent class / base class
# CollegUser -> object (single inheritance)
class CollegeUser(object):
  # every class in python implicitly inherits from the class object
  def __init__(self, name, gender, contact_nos):
    # self - Student object / Professor object / any sub class(child class) object

    # common set of attributes in the respective sub classs object
    self.name = name
    self.gender = gender
    self.contact_nos = contact_nos

  def get_details(self):
    # self - Student object / Professor object / any sub class(child class) object
    part1 = 'Name: {0}\nGender: {1}\n'.format(self.name, self.gender)

    if self.contact_nos:
      part2 = 'Contact Nos : '
      for contact_no in self.contact_nos:
        part2 += contact_no + '\n'
    else:
      part2 = 'Contact Nos : NA'

    return part1 + part2

  def __str__(self):
    return 'Name: {0}\nGender: {1}'.format(self.name, self.gender)