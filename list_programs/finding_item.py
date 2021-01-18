# a program to search item in list
# assume this is a list of flowers in flower shop
flowerslist = ['Rose', 'Lotus', 'Dandelion', 'Water Lily',
          'Tulip','Hibiscus','Sunflower,','orchid',
          'chrysanthemum','pansy']

searchterm = input('enter a flower to search: ') 

# we can search in a list for an item using `in` keyword

if searchterm in flowerslist:
    print(f'we have {searchterm} in the shop.')
else:
    print(f'we dont sell {searchterm} here')
