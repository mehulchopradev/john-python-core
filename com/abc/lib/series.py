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