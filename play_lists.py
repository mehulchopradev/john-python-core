nos = [5, 6, 10, 10, 1, 3, 2, 9]

# get a new list having even nos from the nos list (filtering)
'''evens = []
for n in nos:
  if not n % 2:
    evens.append(n)'''

# for comprehensions (requirement shud be for a new list)
evens = [n for n in nos if not n % 2]
print('*******evens********')
print(evens)

# get a new list of all the odds greater than 3 from the nos list (filtering)
print('*********Odds*********')
odds = [n for n in nos if n % 2 and n > 3]
print(odds)


# get a new list having squares of elements from the nos list (mapping)
print('********Squares***********')
squares = [n ** 2 for n in nos]
print(squares)

# get a new list of cubes of even elements greater than 2 from the nos list (mapping + filtering)
l = [n ** 3 for n in nos if not n % 2 and n > 2]
print(l)

'''
[
  [4,5],
  [3,1]
]
'''