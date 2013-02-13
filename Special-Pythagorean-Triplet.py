# a + b + c = 1000
import math

a = 1
b = 2
c = 3

def tripletCheck(a, b, c):
    if(a + b + c == 1000):
        return True
    else:
        return False

while True:
    while True:
        c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
        if tripletCheck(a, b, c):
            break
        b += 1
        if b > 1000:
            break
    if tripletCheck(a, b, c):
        break
    a += 1
    b = 0
print a, b, c
print a * b * c
