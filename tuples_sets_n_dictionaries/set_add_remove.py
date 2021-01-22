x = {1,2,3}

x.add(4)
x.add(3)
x.add(5)
x.add(10)
print(x)
x.remove(3)
x.remove(5)
x.discard(10) # same as remove but better
print(x)

y = {10,11,12}
x.update(y) # add a set to existing set
print(x)