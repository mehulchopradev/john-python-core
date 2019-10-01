nos = [4, 5, 10, 3, 5, 10, 1, 6, 8]

# get a new list of only the pointers greater than 5 from the nos list (filtering)
'''def greater_than_5(element):
  return element > 5

iterable = filter(greater_than_5, nos)
print(list(iterable))'''

iterable = filter(lambda element: element > 5, nos)
print(list(iterable))

# get a new list of only the even pointers greater than 3 from nos list(filtering)
'''def even_pointers(element):
  return not element % 2 and element > 3

evens_iterable = filter(even_pointers, nos)
print(list(evens_iterable))'''

evens_iterable = filter(lambda element: not element % 2 and element > 3, nos)
print(list(evens_iterable))


# get a new list of squares of even pointers and cubes of odd pointers from the nos list (mapping)
'''def map_even_odd(element):
  return element ** 3 if element % 2 else element ** 2
even_odd_iterable = map(map_even_odd, nos)
print(list(even_odd_iterable))'''

even_odd_iterable = map(lambda element: element ** 3 if element % 2 else element ** 2, nos)
print(list(even_odd_iterable))

'''def map(func, iterable):
  l = []
  for item in iterable:
    l.append(func(item))

  return l'''

'''def filter(func, iterable):
  filtered_list = []
  for item in iterable:
    if func(item):
      filtered_list.append(item)
  
  return filtered_list'''
