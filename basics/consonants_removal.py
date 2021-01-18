msg = input("apna msg likhe : ")
for char in msg:
    if char not in 'aeiouAIOEU':
        msg = msg.replace(char,'')
print(msg)