msg = input('enter a message')

# remove vowels
for v in "aeiouAIEUO":
    msg = msg.replace(v,'')
print('vowels removed:',msg)

# get 3 char index from it
print("every 3 char of string:",msg[::3])