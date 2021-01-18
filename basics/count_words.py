msg = 'this was great this was awesome this was not boring'
words = msg.split()       # break string into words
for item in set(words):   # set makes all the words unique   
    print(item,'=>', words.count(item))  # count each word