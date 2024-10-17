# Jin Pak
# 10/17/24
# P2HW1
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
print(f"{'Location:':<20}{destin}")
print(f"{'Initial Budget:':<20}${budget:,.2f}")
print(f"{'Fuel:':<20}${gas:,.2f}")
print(f"{'Accomodation:':<20}${hotel:,.2f}")
print(f"{'Food:':<20}${food:,.2f}")

print("-" * 36)
# Calculate the remaining budget after subtracting all the expenses above from the initial budget
total = budget - gas - hotel - food

print()
# Display the results
print("Remaining Balance:", total)
