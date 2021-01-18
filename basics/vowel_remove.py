msg = input('enter a message =>')
vowels = 'aeiou'
for v in vowels:
    msg = msg.replace(v,'')
print(msg)