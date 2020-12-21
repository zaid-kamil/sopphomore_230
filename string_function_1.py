# string builtin functions
# chr() - convert integer to string char
# ord() - convert a char to integer
# len() - returns length of string
# str() - converts items to string

x = chr(65)
print(x)
x = chr(2365)
print(x)
x = chr(12365)
print(x)

y = ord('A')
print(y)
y = ord('a')
print(y)
y = ord('{')
print(y)

print(len("amazing"))
print(len("world"))
print(len("bringer"))

x = 49.3
x = str(x) # converted float to str
print(x, type(x))
x = True
x = str(x) # converted bool to str
print(x, type(x))
x = [1,2,3,4]
x = str(x)
print(x, type(x))