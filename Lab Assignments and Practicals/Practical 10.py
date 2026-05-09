# 10 Write program in Python to accept the number of terms and x from user and compute sine(x). Write functions for power and factorial computation

def power(base, exp):
    res = 1
    for i in range(exp):
        res *= base
    return res

def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

x = float(input("Enter angle x (in radians): "))
terms = int(input("Enter number of terms: "))

sine_val = 0
sign = 1
for i in range(terms):
    exponent = 2 * i + 1
    term = sign * (power(x, exponent) / factorial(exponent))
    sine_val += term
    sign *= -1

print("Calculated sine value is:", sine_val)
