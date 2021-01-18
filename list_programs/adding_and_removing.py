# tell me name of some books
fav_books =[] # empty
unfav_books =[] # empty

# adding item to list
fav_books.append('to kill mocking bird')
fav_books.append('Legion')
fav_books.append('Steelheart')
unfav_books.append('The Hunger games')
unfav_books.append('Julius ceaser')
unfav_books.append('Percy Jackson')
fav_books.append('The final empire')

# removing a item in the list
unfav_books.remove('Percy Jackson') # case sensitive
unfav_books.remove('The Hunger games')

# counting values in list
print('i like', len(fav_books),'books')
for book in fav_books:
    print('+',book)
print('i dont like', len(unfav_books),'books')
for book in unfav_books:
    print('-',book)