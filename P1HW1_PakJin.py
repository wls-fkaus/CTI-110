# Jin Pak
# 9/24/2024
# P1HW1
# Get integer input from the user and perform math calculations

# Display output to the user

print("-----Calculating Exponenets-----")
print()
print()

# Get base value

baseValue = int(input("Enter an integer as the base value: "))

# Get exponent

exponent = int(input("Enter an integer as the exponent: "))
print()
print()

# Calaculate the value of the exponent math

result = baseValue ** exponent

# Display the results
print(baseValue, "raised to the power of", exponent, "is", result, "!!")
print()
print()

print("-----Addition and Subtraction-----")
print()
print()

# Get info from user
startint = int(input("Enter a starting integer: "))
add = int(input("Enter an integer to add: "))
sub = int(input("Enter an integer to subtract: "))
print()
print()

# Calculate the additiona and subtraction
total = startint + add - sub

# Display results
print(startint, "+", add, "-", sub, "is equal to", total)
