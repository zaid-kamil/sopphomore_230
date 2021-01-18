# a program to find item by index 
# assume you are a 5 star hotel ,u have a list of foods and food prices
# user will select a food , you have to print the price

food = ['maggi','chill-chicken','roasted chicken','chaat']
food_prices = [50, 250, 500, 500]

name = input('Yes sir, what would u like to have today:')

if name in food:
    print('yes sir its available,')
    pos = food.index(name) # give us the pos of item
    price = food_prices[pos] # will get the price of item
    print(f'the {name} will be of {price}')
else:
    print(f'sorry sir, we dont serve {name}')