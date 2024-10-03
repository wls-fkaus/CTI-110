# In-class examples of math equations

# Import random library for use in the program
import random


'''
# Get side 1 first

side1 = float(input("Enter the value for side 1: "))

side2 = float(input("Enter the value for side 2: "))
'''

# Generate random values for side1 and side2

side1 = random.randint(1, 100)
side2 = random.randint(1, 100)

# Calculate the hypotenuse

hypotenuse = (side1 ** 2) + (side2 ** 2)

# Display results

print (f"The hypotenuse of a right triangle with the sides {side1} and {side2} is {hypotenuse}.")
