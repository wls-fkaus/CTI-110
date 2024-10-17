# In-class examples using lists
'''
# Create an empty list

myfam = []

# Add values to the list

myfam.append("Me")
myfam.append("Sister")
myfam.append("Mom")
myfam.append("Dad")
myfam.append("Dog")

# Display list

print(myfam)

# print item at index 3

print(myfam[3])

# Print items from 1-3 (it goes up to, but doesn't inlude 3) 

print(myfam[1:4])

# remove item from list by its value

myfam.remove("Sister")

print(f"\n\n Remove Sister...")


print(myfam)

# remove by index

myfam.pop(3)

print(f"\n\n Remove Dog...")
print(myfam)
'''

num1 = int(input("Give me a number"))
num2 = int(input("Give me a number"))
num3 = int(input("Give me a number"))
num4 = int(input("Give me a number"))

# Create the list with the values in it
numbers = [num1, num2, num3, num4]

print(numbers)

# Functions use lists

# Gives back the number of items in the list
print(f"There are {len(numbers)} items in the list.")

# Get the highest value in the list

print(f"The highest value in the list is {max(numbers)}.")

# get the lowest number
print(f"The lowest value in the list is {min(numbers)}.")

# get the sum
print(f"The sum of values in the lists is {sum(numbers)}.")

# get the average
average = sum(numbers)/len(numbers)

print(f"The average of the values in the list is {average}.")







