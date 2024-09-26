# Jin Pak
# 9/26/24
# P1HW2
# A program that does some basic math on numbers that are entered.


print("This program calculates and displays travel expenses")
print()

# Have the user input their initial budget
budget = int(input("Enter Budget: "))
print()

# Have the user input their destination
destin = input("Enter your travel destination: ")
print()

# Have the user input how much they think they will spend on fuel or gas
gas = int(input("How much do you think you will spend on gas? "))
print()

# Have the user input how much they think they will spend for accomodations or hotel
hotel = int(input("Approximately, how much will you need for accomodation/hotel? "))
print()

# Have the user input how much they think they will spend for food
food = int(input("Last, how much do you need for food? "))
print()

# This section will display all information needed
print("-----------Travel Expenses----------")

# Display the info the user input above
print("Location:", destin)
print("Initial Budget:", budget)
print()
print("Fuel:", gas)
print("Accomodation:",hotel)
print("Food:", food)
print()

# Calculate the remaining budget after subtracting all the expenses above from the initial budget
total = budget - gas - hotel - food

# Display the results
print("Remaining Balance:", total)
