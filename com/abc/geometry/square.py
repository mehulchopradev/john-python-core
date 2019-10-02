# Developer x of company abc
from .shape import Shape

class Square(Shape):
  def __init__(self, side):
    self.side = side

  # overriden the Shape methods
  def area(self):
    return self.side * self.side

  def perimeter(self):
    return 4 * self.side