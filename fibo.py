n = int(input('Enter n : '))

# n = 8 - (0, 1, 1, 2, 3, 5, 8, 13)

a, b = 0, 1

print(a)
print(b)


# sequence
# (3-n)
# (3, 4, 5, 6, 7, 8)

for v in range(3, n + 1):
  print(a + b)
  a, b = b, a + b
