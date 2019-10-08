from com.abc.college.book import Book

b1 = Book('Book 1', 1000, 900)

b1.pages = 950 # @pages.setter

print(b1.pages) # @property

# b1.__price = -450
# b1.set_price(300)
# b1.set_price(-400)

print(b1)

print(b1.get_price())