n = int(input('Enter n : '))

'''i = 0 # loop variable

# while loop

while i <= n: # condition which can be python truthy or falsy
  if not i % 2:
    print(i)
  i += 1'''


# for loop (preferred)
'''
  for var in <<sequence of elements>>:
    I1
    I2
    I3
'''
# sequence of elements - (0 to n)
# n = 8 - (0, 1, 2, 3, 4, 5, 6, 7, 8)
# n = 2 (0, 1, 2)

'''for v in range(0, n + 1):
  if not v % 2:
    print(v)'''

for v in range(0, n + 1, 2): # step size as third argument to the range
  print(v)