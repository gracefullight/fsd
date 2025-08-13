import math

radius = float(input("Enter the radius: "))
area = math.pi * radius**2
volume = (4 / 3) * math.pi * radius**3


print(f"Circle area of radius {radius} is {area:.2f}")
print(f"Sphere volume of radius {radius} is {volume:.2f}")
