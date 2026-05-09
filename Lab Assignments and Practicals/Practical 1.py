# 1 Write Program in Python to accept an object mass in kilograms and velocity in meters per second. Calculate and display momentum. Calculate p=m*v, where: p = momentum, m=mass, and v=velocity.

mass = float(input("Enter mass in kilograms: "))
velocity = float(input("Enter velocity in meters per second: "))
momentum = mass * velocity
print("The momentum is:", momentum, "kg m/s")
