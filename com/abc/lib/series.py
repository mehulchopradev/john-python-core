# all lib functions related to generating mathematical series

# module name - series

def get_fibo_series(n):
  result = ''
  a, b = 0, 1
  result += str(a) + '\t' + str(b) # in python only a str can be concatenated with another str

  for v in range(3, n + 1):
    result += str(a + b) + '\t'
    a, b = b, a + b

  return result

def get_even_series(n):
  result = ''
  for v in range(0, n+1, 2):
    result += str(v) + '\t'
  return result

# print(__name__) #implicit variable every module gets
# when directly running this module - __main__
# when imported in an external module and external module runs - package name.module name

if __name__ == '__main__':
  n = int(input('Enter n : '))
  print(get_fibo_series(n))
  print(get_even_series(n))