# This program simulates shopping and display receipt

# Get info for item 1
item1 = input("Enter first item: ")
quantity1 = int(input(f"Enter the quantity of {item1}: "))
price1 = float(input(f"Enter the price of {item1}: "))

print()

# Get info for item 2
item2 = input("Enter second item: ")
quantity2 = int(input(f"Enter the quantity of {item2}: "))
price2 = float(input(f"Enter the price of {item2}: "))

print()

# Get info for item 3
item3 = input("Enter third item: ")
quantity3 = int(input(f"Enter the quantity of {item3}: "))
price3 = float(input(f"Enter the price of {item3}: "))

print()

# Display top of the receipt
print("-----------Thanks for shopping!-----------")
print("-*-" * 14)
print()

item = "ITEM"
quantity = "QUANTITY"
item_total = "TOTAL"
print(f"{item:<20}{quantity:<15}{item_total:<10}")
print()
print(f"{item1:<20}{quantity1:<15}${quantity1 * price1:.2f}\n")
print(f"{item2:<20}{quantity2:<15}${quantity2 * price2:.2f}\n")
print(f"{item3:<20}{quantity3:<15}${quantity3 * price3:.2f}\n")
print()

print("-" * 43)

print()
subtotal = (quantity1 * price1) + (quantity2 * price2) + (quantity3 * price3)
print(f"Subtotal: ${subtotal:.2f}")

print()
tax = 0.07 * subtotal
print(f"Tax: ${tax:.2f}")

print()
total = tax + subtotal
print(f"Total: ${total:.2f}")
