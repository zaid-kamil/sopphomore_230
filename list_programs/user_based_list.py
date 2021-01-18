fruits = []
number = int(input('how many fruits will you enter:'))

for i in range(number):
    name = input('enter fruit name: ')
    fruits.append(name)

print('you have entered ->',fruits)
