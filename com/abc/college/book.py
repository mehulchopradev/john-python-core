class Book:

  def __init__(self, title, price, pages):
    self.title = title
    # self.__price = price # private attribute (two underscores prefixed)
    self.set_price(price)
    self.pages = pages # @pages.setter

  def __str__(self):
    return 'Title: {0}\nPrice: {1}\nPages: {2}'.format(self.title, self.__price, self.pages) # @property

  # public mutator function for private attribute price
  # Encapsulation
  def set_price(self, price):
    if price < 0:
      raise ValueError('Price cannot be negative')

    # if all is fine
    self.__price = price

  # public accessor function for private attribute price
  def get_price(self):
    return self.__price

  # pages now becomes an object property (property is different from an object attribute)
  @property
  def pages(self): # emaulate the getter kind of function
    return self.__pages

  @pages.setter
  def pages(self, pages): # emulate the setter kind of functions
    if pages < 10:
      raise ValueError('Pages should be more than 10')

    self.__pages = pages
