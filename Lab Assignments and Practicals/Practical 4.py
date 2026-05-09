# 4 Write program in Python to accept two numbers from the user and compute the smallest divisor and Greatest Common Divisor of these two numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Smallest divisor for num1
smallest_div1 = num1
for i in range(2, num1 + 1):
    if num1 % i == 0:
        smallest_div1 = i
        break
print("Smallest divisor of", num1, "is", smallest_div1)

# Smallest divisor for num2
smallest_div2 = num2
for i in range(2, num2 + 1):
    if num2 % i == 0:
        smallest_div2 = i
        break
print("Smallest divisor of", num2, "is", smallest_div2)

# Greatest Common Divisor (GCD)
a = num1
b = num2
while b != 0:
    temp = b
    b = a % b
    a = temp
print("Greatest Common Divisor is", a)
