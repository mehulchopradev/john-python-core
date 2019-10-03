print('Program starts...')

n = input('Enter n : ')

try:
  ii = int(n)
except ValueError:
  print('enter integer values only')
else:
  # will execute when there is no error raised in the corresponding try block
  print('Odd') if ii % 2 else print('Even')

print('Program ends...')