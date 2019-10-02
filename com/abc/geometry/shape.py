# enforce protocol on its sub classes
# 1. It should mark itself as an Abstract class
# 2. Along with that, mark the methods that need to be followed as part of the protocol, as abstract methods

from abc import ABC, abstractmethod

class Shape(ABC):

  @abstractmethod
  def area(self):
    pass

  @abstractmethod
  def perimeter(self):
    pass