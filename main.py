a = int(input())
b = int(input())
c = int(input())
if b > a:
    a, b = b, a
if c > b:
    c, b = b, c
if b > a:
    a, b = b, a
print(a)
print(b)
print(c)