def area_rectangle(length, breadth):
  a = length * breadth
  return a

def perimeter_rectangle(length, breadth):
  p = 2 * (length + breadth)
  return p

l = float(input('Enter length : '))
b = float(input('Enter breadth : '))

area = area_rectangle(length=l, breadth=b)
peri = perimeter_rectangle(length=l, breadth=b)

print(area)
print(peri)