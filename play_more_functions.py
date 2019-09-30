# variable number of arguments 0 to n
def myadd(*args):
  # print(args) # tuple
  sum = 0
  for arg in args:
    sum += arg
  return sum


# positional arguments packing.
# the positional arguments get packed into a tuple
print(myadd())
print(myadd(4))
print(myadd(5, 3, 2))
print(myadd(5, 6, 10, 4, 5, 6, 8))


def perimeter(length, breadth):
  return 2 * (length + breadth)

stats = (5, 3) # can be a list too
print(perimeter(stats[0], stats[1]))
print(perimeter(*stats)) # positional arguments unpacking

def area(**rec_stats):
  # print(rec_stats) # dict
  return rec_stats['length'] * rec_stats['breadth']

# print(area(5.1, 4.9)) # positional arguments
# keyword arguments packing
print(area(length=5.1, breadth=4.9)) # keyword arguments
print(area(breadth=4.9, length=5.1))
# print(area(b=4.9, l=5.1)) # not going to work

stats_map = {'breadth': 4, 'length': 10}
print(perimeter(stats_map['length'], stats_map['breadth']))
print(perimeter(**stats_map)) # keyworkd argument unpacking