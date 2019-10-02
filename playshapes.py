from com.abc.geometry.square import Square
from com.abc.geometry.rectangle import Rectangle
from com.abc.geomstats.geom_stats import GeomStats

s = Square(side=5)
GeomStats.print_stats(s)

r = Rectangle(length=7, breadth=3)
GeomStats.print_stats(r)

'''print(s.area())
print(s.perimeter())'''