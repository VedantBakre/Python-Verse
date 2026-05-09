# 3 Write program in Python to accept the number, compute and display the following a)square root of number, b) Square of number, c) Cube of number d) check for prime, d) factorial of number e) prime factors

n = int(input("Enter a positive integer: "))

# a) square root
print("Square root:", n ** 0.5)

# b) Square
print("Square:", n ** 2)

# c) Cube
print("Cube:", n ** 3)

# d) check for prime
is_prime = True
if n <= 1:
    is_prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
if is_prime:
    print(n, "is a prime number.")
else:
    print(n, "is not a prime number.")

# e) factorial
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print("Factorial:", factorial)

# f) prime factors
print("Prime factors: ", end="")
temp = n
for i in range(2, temp + 1):
    while temp % i == 0:
        print(i, end=" ")
        temp = temp // i
print()
