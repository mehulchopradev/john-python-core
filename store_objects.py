from com.abc.college.book import Book
from pickle import dump, load

with open('/Users/mehul.chopra/Documents/books.pkl', mode='rb') as fp:
  books = load(fp)

while True:
  print('1. Enter book', '2. View books', '3. Exit', sep='\n')
  choice = int(input('Enter Choice : '))

  if choice == 1:
    title = input('Title : ')
    price = float(input('Price : '))
    pages = int(input('Pages : '))

    books.append(Book(title, price, pages))
  elif choice == 2:
    for book in books:
      print(book)
  else:
    with open('/Users/mehul.chopra/Documents/books.pkl', mode='wb') as fp:
      dump(books, fp)
    break

