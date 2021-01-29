mobiles = {}

for i in range(5):
    name = input('enter mobile name: ')
    price = int(input('enter mobile price $$: '))

    mobiles[name] = price
    print('added')

print('Your data is')
for k, v in mobiles.items():
    if v > 25000:
        print(k,v,'is costly')
    else:
        print(k,v,'is in budget')