import string                       # loading a library

message = 'i will { } walk " on &^* the)(*) surface%@%%!@#{} of moon'

for spchar in string.punctuation:   # for every sp char in punctations
    print(spchar,'--', message.count(spchar))


