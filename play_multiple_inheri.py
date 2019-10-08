class Abc: # vendor 1

  def fun(self):
    print('Fun')

  def hello(self):
    print('hello of Abc')

class Xyz: # vendor 2

  def hello(self):
    print('hello')

class Mno(Xyz, Abc): # multiple inheritances
  # MRO (Method resolution order)
  pass


m = Mno()
m.fun()
m.hello()