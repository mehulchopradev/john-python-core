'''def abc():

  i = 9 # int object (i) - abc
  j = 10 # int object (j) - abc

  def pqr(): # function object (pqr) - abc
    print('pqr')
    print(i) # this will work
    # inner function can access the enclosing function variables (closures)

    j = 3 # int object (j) - pqr
    print(j) # 3
  
  print('abc')
  pqr()

  print(j) # 10

abc()'''


'''def xyz(i): # int object - i - (xyz)
  j = 9 # int object - j - (xyz)

  def ytr(a): # function object - ytr - (xyz)
    return i + j + a

  return ytr # a function can return another function

f = xyz(5) # f <-> ytr
print(f(6)) # 20'''


def wqr(f): # functioon object - wqr - (module)
  i = 9
  return f(i)

def fun(a): # function object - fun - (module)
  return a + 10


print(wqr(fun)) # 19
# callback functions
# passing a function as an argument to another function