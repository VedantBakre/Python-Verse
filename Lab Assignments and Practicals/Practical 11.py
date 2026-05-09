# 11 Write program in Python with function that returns surface area and volume of the sphere.

def sphere_properties(radius):
    pi = 3.14159
    surface_area = 4 * pi * (radius ** 2)
    volume = (4/3) * pi * (radius ** 3)
    return surface_area, volume

r = float(input("Enter the radius of the sphere: "))
area, vol = sphere_properties(r)
print("Surface Area:", area)
print("Volume:", vol)
