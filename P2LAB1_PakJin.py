# Jin Pak
# 10/8/24
# P2LAB1
# Mathematical calculations and display information to users

# Import from the library
import math

'''
print (f"The value of pi is {math.pi}")
'''

# Get radius from user
radius = float(input("What is the radius of the circle? "))

print()
# Get the diameter with the radius
diameter = 2 * radius

# Display the diameter
print(f"The diameter of the circle is {diameter:.1f}\n")

# Get the cicumference
circumf = 2 * math.pi * radius

# Display the circumfereence
print(f"The circumference of the circle is {circumf:.2f}\n")

# Get the area of the circle
area = math.pi * math.pow(radius, 2)

# Display the ara of the circle
print(f"The area of the circle is {area:.3f}")
