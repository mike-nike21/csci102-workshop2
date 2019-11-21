# fibonacci.py

a = 0 
b = 1

print(b)
for i in range(99):
    c = a + b
    a = b
    b = c
    print(c)
