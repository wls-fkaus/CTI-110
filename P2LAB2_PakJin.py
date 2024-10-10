# Jin Pak
# 10/10/24
# P2LAB2
# Use a dictionary to store user input and displays output to the user

cars = {"Camaro":18.21, "Prius": 52.36, "Model S": 110, "Silverado":26}

# a variable that holds only keys from the dictionary
keys = cars.keys()

# print all the keys to the users

print(keys)
print()
# make the user enter a key 

answer = input("Enter a vehicle to see it's mpg: ")
print()

# Give the value associated with the users answer

print(f"The {answer} gets {cars[answer]} mpg.")
print()

# Get how any miles the user will drive with the car

miles = float(input(f"How many miles will you drive the {answer}? "))
print()

# Calculate the amount of gallons needed for miles

gallons = miles / cars[answer]

# display the amount of gallons they nedd to drive

print(f"{gallons:.2f} gallon(s) of gas are needed to drive the {answer} {miles:.1f} miles.")



