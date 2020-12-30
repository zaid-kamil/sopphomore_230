for c, i in enumerate(range(1, 15,2)):
    if c % 2 != 0:
        print((i*'O').center(15))
    else:
        print((i*'*').center(15))