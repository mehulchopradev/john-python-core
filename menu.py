
# module name - menu
# google.com
# com -> google ->,,,,,,

# import series # just imports the module

# directly import the members of the module (functions)
# from series import get_fibo_series as fibo, get_even_series

from com.abc.lib.series import get_fibo_series as fibo, get_even_series
import com.abc.lib.math
import math

# import math as m

while True:
  print('1. Fibo series', '2. Even series', '3. Even or odd', '4. Factorial', '5. Exit', sep='\n')
  choice = int(input('Enter choice : '))

  if choice == 1 or choice == 2 or choice == 3 or choice == 4:
    n = int(input('Enter n : ')) # module entire file

  if choice == 1:
    # print(series.get_fibo_series(n))
    # print(get_fibo_series(n))
    print(fibo(n))
    # pass # allows to have empty blocks in a program
  elif choice == 2:
    # print(series.get_even_series(n))
    print(get_even_series(n))
  elif choice == 3:
    # print(math.even_odd(n))
    # print(m.even_odd(n))
    print(com.abc.lib.math.even_odd(n))
  elif choice == 4:
    print(math.factorial(n))
  else:
    break
