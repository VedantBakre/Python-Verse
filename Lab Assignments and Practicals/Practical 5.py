# 5 Write Program in Python to read the number, and check whether the number is the Armstrong number or not. An Armstrong number is an integer with three digits such that the sum of the cubes of its digits is equal to the number itself. Ex. 371.

num = int(input("Enter a 3-digit number: "))
sum_of_cubes = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum_of_cubes += digit ** 3
    temp //= 10

if num == sum_of_cubes:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
