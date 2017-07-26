# This program works for input numbers with even number of digits


import cs50
import math
def multiply(x, y, n):
    if(n == 1):
        return x*y
    len = n / 2
    a = int(x / (10 ** len))
    b = int(x - (a *(10 ** len)))
    c = int(y / (10 ** len))
    d = int(y - (c *(10 ** len)))
    ac = multiply(a, c, len)
    ad = multiply(a, d, len)
    bc = multiply(b, c, len)
    bd = multiply(b, d, len)
    return int(ac*(10**n)) + ((10 ** len)*(ad + bc)) + bd
print(multiply(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627, 64))


