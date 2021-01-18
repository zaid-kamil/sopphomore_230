message = input('enter your message :')
special_chars = '~!@#$%^&*()_+{,.}:"<>?/'
for spc in special_chars:
    message = message.replace(spc, "_") # replace and update
    print(message)
